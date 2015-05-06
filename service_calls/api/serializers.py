'''
Created on Apr 25, 2015

@author: eytan
'''

from rest_framework import serializers

from service_calls.content.serializers import ContentSerializer, \
    ContentDetailSerializer
from service_calls.models.fault import Fault
from service_calls.models.ticket import Ticket


class FaultSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(FaultSerializer, self).__init__(many=many, *args, **kwargs)
    
    class Meta:
        model=Fault
        
class TicketSerializer(serializers.ModelSerializer):
       
    content = ContentSerializer(many=False)
    fault = FaultSerializer
    
    class Meta:
        model = Ticket
     
     
     
class TicketDetailSerializer(serializers.ModelSerializer):
        
    content = ContentDetailSerializer(many=False)
    fault = FaultSerializer
     
    class Meta:
        model = Ticket
        


    