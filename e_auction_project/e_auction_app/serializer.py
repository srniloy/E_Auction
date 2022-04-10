from rest_framework import serializers
from .models import *


class UserEmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmail
        fields = ('user_id', 'user_email')
