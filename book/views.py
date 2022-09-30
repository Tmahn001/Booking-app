from django.contrib.auth.decorators import login_required
from apscheduler.schedulers.background  import BackgroundScheduler
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView 
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from .models import BookSlot, Slot, TopUp, Wallet
from datetime import datetime, timedelta, time, date
from django.utils import timezone
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from django_apscheduler.jobstores import register_events, register_job

from django.conf import settings


# Create your views here.

@login_required
    
def home(request):
    today = datetime.today().date()
    book = BookSlot.objects.filter(slot=1, select_date=today).first()
    book_2 = BookSlot.objects.filter(slot=2, select_date=today).first()
    book_3 = BookSlot.objects.filter(slot=3, select_date=today).first()
    book_4 = BookSlot.objects.filter(slot=4, select_date=today).first()
    book_5 = BookSlot.objects.filter(slot=5, select_date=today).first()
    book_6 = BookSlot.objects.filter(slot=6, select_date=today).first()
    book_7 = BookSlot.objects.filter(slot=7, select_date=today).first()
    book_8 = BookSlot.objects.filter(slot=8, select_date=today).first()
    
    context ={
        "book":book,
        "book_2":book_2,
        "book_3":book_3,
        "book_4":book_4,
        "book_5":book_5,
        "book_6":book_6,
        "book_7":book_7,
        "book_8":book_8,
        "today":today,
    }
        
    
    return render(request, 'home.html', context)
    
def booking_details(request):
    all = BookSlot.objects.filter(email=request.user, verified=True).all()
    context = {
        "all": all
    }
    return render(request, "bookings.html", context)

def initiate_booking(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        booking_form = forms.BookSlotForm(request.POST)

        if booking_form.is_valid():

            booking = booking_form.save(commit=False)
            booking.email = request.user
            booking.save()

            return render(request, 'make_payment.html', {'booking': booking, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
    else:
        booking_form = forms.BookSlotForm()
    
    context = {
        "booking_form":booking_form,
    }
    return render(request, 'initiate_booking.html', context)



def verify_payment(request:HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(BookSlot, ref=ref)
    status = payment.verify_payment()

    if status:
        messages.success(request, "verification Successful")
        return render(request, "payment_success.html", context={"payment": payment})
    else:
        messages.error(request, "verification failed")
    return redirect("initiate-payment")
    
def top_up(request:HttpRequest) -> HttpResponse:
    wallet = get_object_or_404(Wallet, user=request.user)
    if request.method == "POST":
        top_up_form = forms.TopUpForm(request.POST)
        if top_up_form.is_valid():
            top_up = top_up_form.save(commit=False)
            top_up.user = request.user
            top_up.wallet = wallet
            top_up.save()
            return render(request, 'topped_up.html',
                          {'top_up': top_up, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
    else:
        top_up_form = forms.TopUpForm()
    balance = Wallet.objects.get(user=request.user)
    credit = TopUp.objects.filter(user=request.user)
    context = {
        "balance":balance,
        "credit":credit,
        "top_up_form":top_up_form,
    }
    return render(request, 'top_up.html', context)

def verify_top_up(request:HttpRequest, ref:str) -> HttpResponse:
    add = get_object_or_404(TopUp, ref=ref)
    wallet = get_object_or_404(Wallet, user=request.user)
    status = add.verify_payment()
    if status:
        wallet.balance = wallet.balance + int(add.amount)
        wallet.save()
        return redirect("wallet-balance")

    else:
        return render(request, "home.html")
        
def wallet_balance(request):
    balance = Wallet.objects.filter(user=request.user)
    credit = TopUp.objects.filter(user=request.user).order_by('-date_created')
    if not balance:
        activate = Wallet(
            user=request.user

        )
        obj = request.user

        activate.save()
        return redirect("wallet-balance")
    balance = Wallet.objects.get(user=request.user)
    context = {
        "balance":balance,
        "credit":credit
    }

    return render(request, "wallet.html", context)
    
def run():
    now = timezone.now()
    twenty_minutes_ago = now + timedelta(minutes=-20)
    ten_minutes_ago = now + timedelta(minutes=-1)
    check = BookSlot.objects.filter(payment_date_and_time__range=[twenty_minutes_ago, ten_minutes_ago]).all()
    print('start')
    if check:
        for c in check:
            if not c.verified:
                c.delete()
                print("deleted")
            else:
                print("nothing")
    else:
        return ''
        






































    
    