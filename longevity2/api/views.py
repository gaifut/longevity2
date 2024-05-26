from rest_framework import viewsets

from users.models import User
from .serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
