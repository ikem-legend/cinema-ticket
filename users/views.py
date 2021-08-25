# from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from .models import User
from .serializers import UserSerializer
from uuid import uuid4


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [OrderingFilter]
    ordering_fields = ["date_created"]
    ordering = ["-date_created"]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()

    # def list(self, request):
    #     print(uuid4())
    #     print(request)
    #     print("Get")
    #     return HttpResponse("Get request")
    #
    # def create(self, request):
    #     print(request)
    #     return HttpResponse(request.data)
