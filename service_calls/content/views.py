'''
Created on Apr 29, 2015

@author: eytan
'''
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from service_calls.api.serializers import TicketDetailSerializer
from service_calls.content import TICKET_STATIC_DATA
from service_calls.content.models.fault import Fault
from service_calls.content.models.guest import Guest
from service_calls.content.models.location import Location
from service_calls.content.serializers import GuestSerializer, \
    LocationSerializer, FaultSerializer
from service_calls.utils.gui import safe_upload


@api_view(['POST'])
def load_guests(request):
    return safe_upload(request, Guest, GuestSerializer)
    
@api_view(['POST'])
def load_locations(request):
    return safe_upload(request, Location, LocationSerializer)

@api_view(['POST'])
def load_faults(request):
    return safe_upload(request, Fault, FaultSerializer)

@api_view(['GET'])
def get_static_content(request):
    return Response(TICKET_STATIC_DATA)

@api_view(['POST'])
def locations(request):
    serializer = LocationSerializer(Location.objects.all(), many=True)
    return Response(serializer.data)


class LocationList(generics.ListAPIView):
    
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.all()
    
    def get(self, request):
        return self.list(request)

class GuestList(generics.ListAPIView):
    
    serializer_class = GuestSerializer

    def get_queryset(self):
        return Guest.objects.all()
    
    def get(self, request):
        return self.list(request)

class FaultList(generics.ListAPIView):
    
    serializer_class = FaultSerializer

    def get_queryset(self):
        return Fault.objects.all()
    
    def get(self, request):
        return self.list(request)
