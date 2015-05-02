'''
Created on Apr 29, 2015

@author: eytan
'''
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models.aggregates import Max, Min
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from service_calls.content.models.guest import Guest
from service_calls.content.models.location import Location
from service_calls.content.serializers import GuestSerializer, \
    LocationSerializer


@transaction.atomic
def safe_upload(request, model, serializer_class):
    try:
        count_all = model.objects.count()
        if count_all <= 2000:
            model.objects.all().delete()
        else:
            max_id = model.objects.aggregate(Max('id'))['id__max']
            min_id = model.objects.aggregate(Min('id'))['id__min']
            for safe_id in xrange(min_id, max_id, 2000):
                model.objects.filter(id__lt=safe_id).all().delete()
        
        serializer = serializer_class(data=request.DATA, files=request.FILES, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@csrf_exempt  
@api_view(['POST'])
def load_guests(request):
    return safe_upload(request, Guest, GuestSerializer)
    
@api_view(['POST'])
def load_locations(request):
    return safe_upload(request, Location, LocationSerializer)
