from django.db import models

# Create your models here.

class Sms(models.Model):
    phone = models.CharField(max_length=12, verbose_name="Phone")
    msg = models.TextField(verbose_name="Message")
    app = models.CharField(max_length=100, verbose_name="App name")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Datetime")

    def __str__(self):
        return self.phone