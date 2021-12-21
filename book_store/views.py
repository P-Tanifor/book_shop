from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from book_store.models import AvailableBooks, ConfirmedOrders
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
import django
from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'book_store/main_page.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'signup.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'login.html'


class MyLogoutView(LogoutView):
    next_page = None
    template_name = 'logout.html'


class AvailableBooksView(View):
    def get(self, request, *args, **kwargs):
        context = {'available_books': AvailableBooks.objects.all()}
        return render(request, 'book_store/available_books.html', context=context)


class OrdersView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'book_store/order_form.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            item = request.POST.get('book_title')
            order_qty = request.POST.get('quantity')
            book = AvailableBooks.objects.get(book_title=item)
            if book.quantity >= int(order_qty):
                AvailableBooks.objects.filter(book_title=item).update(book_title=item,
                                                                      quantity=book.quantity - int(order_qty),
                                                                      inventory_date=datetime.now())
                ConfirmedOrders.objects.create(book_title=item, ordered_by=request.user, ordered_qty=order_qty)
                return redirect('/')
            else:
                return HttpResponse(' Unavailable order')

        else:
            raise PermissionDenied()


class RemoveBookView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'book_store/del.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                AvailableBooks.objects.filter(book_title=request.POST.get("book_title")).delete()
                return redirect('/')
            else:
                raise PermissionDenied()
        else:
            raise PermissionDenied()


class UpdateBooks(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'book_store/update.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                title = request.POST.get('book_title')
                qty = request.POST.get('quantity')
                book = AvailableBooks.objects.get(book_title=title)
                AvailableBooks.objects.filter(book_title=title).update(book_title=title,
                                                                       quantity=book.quantity + int(qty),
                                                                       inventory_date=datetime.now())
                return redirect('/')
            else:
                raise PermissionDenied()
        else:
            raise PermissionDenied()


class AddBooks(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'book_store/add_books.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                AvailableBooks.objects.create(book_title=request.POST.get("book_title"),
                                              quantity=request.POST.get('quantity'),
                                              inventory_date=datetime.now())
                return redirect('/')
            else:
                raise PermissionDenied()
        else:
            raise PermissionDenied()


class ConfirmedOrdersView(View):
    def get(self, request, *args, **kwargs):
        context = {'confirmed_orders': ConfirmedOrders.objects.all()}
        return render(request, 'book_store/confirmed_orders.html', context=context)