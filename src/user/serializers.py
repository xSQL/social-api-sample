import requests

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    def validate_email(self, email):
        """Check email by api hunter"""
        if settings.EMAILHUNTER_KEY:
            url = 'https://api.hunter.io/v2/'\
            'email-verifier?email={email}&api_key={key}'.format(
                email=email, 
                key=settings.EMAILHUNTER_KEY
            )
            response = requests.get(url)
            data = response.json().get('data', {})
            if data.get('score')<70:
                msg = _('You email look strange')
                raise serializers.ValidationError(msg)
        return email

    def validate_password(self, raw_pass):
        """Before saving password must be hashing"""
        return make_password(raw_pass)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
