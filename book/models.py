from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib.auth import get_user_model
import secrets
from .paystack import Paystack

from django.db import models
from django.urls import reverse
from django.utils import timezone
import uuid

# Create your models here.

plans = (
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly'),

)

class Slot(models.Model):
    name = models.CharField(max_length=50)
    index = models.PositiveIntegerField()

    def __str__(self):
        return self.name





class Plan(models.Model):
    plan = models.CharField(max_length=40, choices=plans)
    amount = models.PositiveIntegerField()
    def __str__(self):
        return self.plan


class BookSlot(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE,)
    email = models.ForeignKey(get_user_model(),
                                    on_delete=models.CASCADE, null=True, blank=True)
    select_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default= plans)
    select_date = models.DateField()
    amount = models.PositiveIntegerField(default=2000)
    ref = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4, max_length=13)
    date_created = models.DateTimeField(auto_now_add=True)
    payment_date_and_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    verified = models.BooleanField(default=False)
    class Meta:
        ordering = ('-date_created',)
        unique_together = ('slot', 'select_date',)

    def __str__(self):
        return str(self.slot)
    def unique_error_message(self, model_class, unique_check):
        if model_class == type(self) and unique_check == ('slot', 'select_date'):
            return "Sorry this slot has been booked for this date already."
        else:
            return super(BookSlot, self).unique_error_message(model_class, unique_check)
        

  
    def amount_value(self) -> int:
        return self.amount * 100

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount']/100 == self.amount:
                self.verified = True
            self.save()
            if self.verified:
                return True

        return False
        

class Wallet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    wallet_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    def __str__(self):
        return str(self.user)
        
class TopUp(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, null=True, blank=True)
    ref = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4, max_length=13)
    amount = models.PositiveIntegerField(default=2000)

    date_created = models.DateField(auto_now_add=True)
    payment_time = models.TimeField(auto_now_add=True)
    
    payment_date_and_time_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    verified = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    def amount_value(self) -> int:
        return self.amount * 100

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount']/100 == self.amount:
                self.verified = True
            self.save()
            if self.verified:
                return True

        return False
        
    
            








    


    
