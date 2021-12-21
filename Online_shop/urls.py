"""Online_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book_store.views import MainPageView, MyLogoutView, MyLoginView, OrdersView, AvailableBooksView, SignUpView,\
    RemoveBookView, UpdateBooks, AddBooks, ConfirmedOrdersView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('login/', MyLoginView.as_view()),
    path('available_books/', AvailableBooksView.as_view()),
    path('order/', OrdersView.as_view()),
    path('update/', UpdateBooks.as_view()),
    path('add_book/', AddBooks.as_view()),
    path('confirmed_orders/',ConfirmedOrdersView.as_view()),
    path('delete/', RemoveBookView.as_view()),
    path('logout/', MyLogoutView.as_view()),





]
