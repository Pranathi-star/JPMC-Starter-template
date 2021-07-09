from django.db import models
from rest_framework import serializers
from .models import custom_user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = custom_user
        fields = "__all__"
