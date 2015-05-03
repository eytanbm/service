'''
Created on Apr 29, 2015

@author: eytan
'''
from rest_framework import serializers

from service_calls.content.models.content import Content
from service_calls.content.models.guest import Guest
from service_calls.content.models.location import Location
from service_calls.models.ticket_event import TicketAttrChange


class LocationSerializer(serializers.ModelSerializer):
    
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(LocationSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Location
        
class GuestSerializer(serializers.ModelSerializer):
    
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(GuestSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Guest
        
class ContentSerializer(serializers.ModelSerializer):
#     guest = serializers.PrimaryKeyRelatedField()
#     location = serializers.PrimaryKeyRelatedField()
    
    class Meta:
        model = Content
#         fields = ("id", "guest", "location")
                
class ContentDetailSerializer(serializers.ModelSerializer):
    guest = GuestSerializer(many=False)
    location = LocationSerializer(many=False)
    
    class Meta:
        model = Content
        fields = ("id", "guest", "location")
        
class TicketAttrChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketAttrChange
        
class TicketEventSerializer(serializers.ModelSerializer):
    
    atrributes = TicketAttrChangeSerializer(many=True)
    
    class Meta:
        model = TicketAttrChange
    
                
