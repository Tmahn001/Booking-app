from django.forms import DateInput
from django import forms

class BookInput(DateInput):
    template_name = 'bookings.html'
    
class DatePickerInput(forms.DateInput):
    input_type = 'date'