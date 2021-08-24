from django.http import HttpResponse
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from uuid import uuid4


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        print(uuid4())
        print(request)
        print("Get")
        return HttpResponse("Get request")

    def create(self, request):
        print(request)
        return HttpResponse(request.data)
