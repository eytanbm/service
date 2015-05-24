'''
Created on Apr 26, 2015

@author: eytan
'''

from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from service_calls.api.serializers import TicketSerializer, \
    TicketDetailSerializer, TicketCommentSerializer
from service_calls.content.serializers import TicketEventSerializer
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_comment import TicketComment
from service_calls.models.ticket_event import TicketEvent
from service_calls.models.ticket_role import TicketRole

class TicketList(generics.ListAPIView):
    
    serializer_class = TicketDetailSerializer

    def get_queryset(self):
        return Ticket.objects.all()
    
    def get(self, request):
        return self.list(request)
    
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        
        user = request.user
        queryset = Ticket.objects.filter(owner__in=TicketRole.objects.filter(user=user).all()).all()
        serializer = TicketDetailSerializer(queryset, many=True)
        return Response(serializer.data)
    
class TicketHistory(generics.ListAPIView):
     
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
     
    serializer_class = TicketEventSerializer
 
    def get_queryset(self, pk):
        return TicketEvent.objects.filter(ticket=Ticket.objects.get(pk=pk)).all()
     
    def list(self, request, pk):
        # Note the use of `get_queryset()` instead of `self.queryset`
        user = request.user
        queryset = self.get_queryset(pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


 
class CreateTicketView(CreateAPIView):
    model = Ticket
    serializer_class = TicketSerializer
    
class UpdateTicketView(UpdateAPIView):
#     model = Ticket
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
class AddTicketComment(CreateAPIView):
    model = TicketComment
    serializer_class = TicketCommentSerializer
        
@api_view(['POST'])
def ticket_comments(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    serializer = TicketCommentSerializer(ticket.comments.all(), many=True)
    return Response(serializer.data)
    
    
    