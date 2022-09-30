from django import forms
from .models import BookSlot, TopUp
from .widgets import DatePickerInput

class BookSlotForm(forms.ModelForm):
    class Meta:
        model = BookSlot
        fields = ("slot", "select_date", "amount", "select_plan")
        widgets = {
            'select_date': DatePickerInput()
        }
        
class TopUpForm(forms.ModelForm):
    class Meta:
        model = TopUp
        fields = ("amount",)
        widgets = {
            'date_created': DatePickerInput()
        }
        labels = {
            "amount": (""),
        }
        

        
        
        
        

        
        
