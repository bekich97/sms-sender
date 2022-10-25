from rest_framework import serializers
from sms.models import Sms
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username"]


class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sms
        fields = "__all__"
