
import datetime
import requests
from rest_framework import filters
from rest_framework import filters, generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import permissions

 
from .models import *
from .serializer import *
from .part.last_day import add_total
from .part.permissions import IsOwnerOrReadOnly, IsAuthor

class TimeDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Delete and Update time """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TimeList(generics.ListCreateAPIView):
    """ Time list and create new time"""
    permission_classes = [IsAuthor]
   
    serializer_class = TimeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['datetime_add',]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Time.objects.filter(owner=self.request.user)
      

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TotaleList(generics.ListCreateAPIView):
    """
    List all code total, or create a new total.

    """
    permission_classes = [IsAuthor]
    
    serializer_class = TotalSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Totale.objects.filter(owner=self.request.user)

class TotaleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    PUT code total, or DELETE a  total.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Totale.objects.all()
    serializer_class = TotalSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RegisterView(generics.ListCreateAPIView):
    """ Registration new 'User' """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
             

class SunTimeList(generics.ListAPIView):
    
    permission_classes = [IsAuthor]
    serializer_class = TimeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Time.objects.filter(owner=self.request.user)

    def get(self, request):
        """
        List all code time, return sum totale time from user request
        """
        snippets = Time.objects.filter(owner=self.request.user)
        now = timezone.now()
        year_month = datetime.datetime.strftime(now,'%m-%Y') # date now 
        total = 0
        for time in snippets:
            data_add = datetime.datetime.strftime(time.datetime_add,'%m-%Y')
            if data_add == year_month:
                total += time.ore_lavorative

        return Response(total)
      
@api_view(['GET'])
def check_last_day_for_month(request):
    if request.method == 'GET':
        if add_total() == True:
            total = requests.get('http://127.0.0.1:8000/sum-time').json()    
            post = requests.post('http://127.0.0.1:8000/totale', json={'total_ore': total})
            return Response("Total month add", status=status.HTTP_201_CREATED)
        else:
            return Response("Not add tatale month")


#class TimeListView(generics.ListAPIView):
 #   queryset = Time.objects.all()
  #  serializer_class = TimeSerializer
   # filter_backends = [filters.SearchFilter]
   # search_fields = ['datetime_add',]

