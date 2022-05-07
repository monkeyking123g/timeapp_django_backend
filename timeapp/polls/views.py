import datetime
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets, filters, generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
 
from .models import *
from .serializer import *
from .part.last_day import add_total


@api_view(['GET', 'POST'])
def time_list(request):
    """
    List all code time, or create a new time.
    """
    if request.method == 'GET':
        snippets = Time.objects.all()
        serializer = TimeSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def total_list(request):
    """
    List all code total, or create a new total.
    """
    if request.method == 'GET':
        snippets = Totale.objects.all()
        serializer = TotalSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TotalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def sum_time(request):
    """
    List all code time, or create a new time.
    """
    if request.method == 'GET':
        snippets = Time.objects.all()
       
        now = timezone.now()
        year_month = datetime.datetime.strftime(now,'%m-%Y') # date now 
        total = 0
        for time in snippets:
            data_add = datetime.datetime.strftime(time.datetime_add,'%m-%Y')
            if data_add == year_month:
                total += time.ore_lavorative
           
        print(total)
        serializer = TimeSerializer(snippets, many=True)
       
        return Response(total)

@api_view(['GET','PUT', 'DELETE'])
def time_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Time.objects.get(pk=pk)
    except Time.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TimeSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TimeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT', 'DELETE'])
def totale_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Totale.objects.get(pk=pk)
    except Totale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TotalSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TotalSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def check_last_day_for_month(request):
    if request.method == 'GET':
        if add_total() == True:
            total = requests.get('http://127.0.0.1:8000/sum-time').json()    
            post = requests.post('http://127.0.0.1:8000/totale', json={'total_ore': total})
            return Response("Total month add", status=status.HTTP_201_CREATED)
        else:
            return Response("Not add tatale month")


class TimeListView(generics.ListAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['datetime_add',]

