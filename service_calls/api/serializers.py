'''
Created on Apr 25, 2015

@author: eytan
'''

from rest_framework import serializers

from service_calls.content.serializers import ContentSerializer, \
    ContentDetailSerializer
from service_calls.models.ticket import Ticket


class TicketSerializer(serializers.ModelSerializer):
       
    content = ContentSerializer(many=False)
    
    class Meta:
        model = Ticket
     
     
     
class TicketDetailSerializer(serializers.ModelSerializer):
        
    content = ContentDetailSerializer(many=False)
     
    class Meta:
        model = Ticket
    