import clearbit

from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView

from .serializers import UserSerializer

User = get_user_model()


class UserListView(ListCreateAPIView):
    """SignUp & List users"""

    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Try to get user info from clearbit.com"""

        instance = serializer.save()
        if settings.CLEARBIT_KEY:
            clearbit.key = settings.CLEARBIT_KEY
            response = clearbit.Enrichment.find(
                email=instance.email,
                stream=False
            )
            if response.get('name'):
                first_name = response['name'].get('givenName')
                last_name = response['name'].get('familyName')

                serializer.save(
                    first_name=first_name,
                    last_name=last_name
                )

