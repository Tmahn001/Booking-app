from django.contrib import admin

from .models import BookSlot, Plan, Slot, TopUp, Wallet
# Register your models here.

class BookSlotAdmin(admin.ModelAdmin):
    list_display = ['slot', 'email', 'select_date', 'verified']
    list_filter = ['slot', 'email', 'verified']
    search_fields = ['slot', 'email', 'verified']
    
class SlotAdmin(admin.ModelAdmin):
    list_display = ['name', 'index']
    list_filter = ['name', 'index']
    search_fields = ['name', 'index']


class PlanAdmin(admin.ModelAdmin):
    list_display = ['plan', 'amount']
    list_filter = ['plan', 'amount']
    search_fields = ['plan', 'amount']

class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'wallet_id', 'balance']
    list_filter = ['user', 'wallet_id']
    search_fields = ['user', 'wallet_id']

class TopUpAdmin(admin.ModelAdmin):
    list_display = ['user', 'wallet', 'amount']
    list_filter = ['user', 'wallet', 'amount']
    search_fields = ['user', 'wallet', 'amount']


admin.site.register(BookSlot, BookSlotAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(TopUp, TopUpAdmin)



