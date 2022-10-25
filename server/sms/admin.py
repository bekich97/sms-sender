from django.contrib import admin
from .models import Sms

# Register your models here.

class SmsAdmin(admin.ModelAdmin):
    list_display = ['phone', 'msg', 'created_date']

    class Meta:
        model = Sms


admin.site.register(Sms, SmsAdmin)