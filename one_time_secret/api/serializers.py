from rest_framework import serializers
from .models import Secret


class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ['text', 'password']


class ShowSecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = ['password']
