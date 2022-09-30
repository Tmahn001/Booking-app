from django.urls import path
from . import views


urlpatterns =[
    path('', views.home, name='home'),
    path('book/', views.initiate_booking, name='initiate-payment'),
    path('bookings/', views.booking_details, name='all_bookings'),
    path('wallet/', views.wallet_balance, name='wallet-balance'),
    path('top/', views.top_up, name='initiate-topup'),
    path('verify/<str:ref>/', views.verify_top_up, name='verify-top-up'),
    path('<str:ref>/', views.verify_payment, name='verify-payment'),
    path('<str:ref>/success', views.verify_payment, name='payment-success'),
  
    ]