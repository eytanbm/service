'''
Created on Apr 25, 2015

@author: eytan
'''

from rest_framework import serializers

from service_calls.content.serializers import ContentSerializer, \
    ContentDetailSerializer
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_comment import TicketComment
from service_calls.models.ticket_role import TicketRole

class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
    
class TicketRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketRole
    
class TicketSerializer(serializers.ModelSerializer):
       
    content = ContentSerializer(many=False)
    
    class Meta:
        model = Ticket
     
     
class TicketDetailSerializer(serializers.ModelSerializer):
        
    content = ContentDetailSerializer(many=False)
     
    class Meta:
        model = Ticket
        

        


    