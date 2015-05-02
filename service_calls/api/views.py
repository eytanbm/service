'''
Created on Apr 26, 2015

@author: eytan
'''

from rest_framework import generics, permissions
from rest_framework.response import Response

from service_calls.api.serializers import TicketSerializer, \
    TicketDetailSerializer
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_role import TicketRole


class TicketList(generics.ListCreateAPIView):
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    serializer_class = TicketDetailSerializer

    def get_queryset(self):
        return Ticket.objects.all()
    
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        user = request.user
        queryset = Ticket.objects.filter(owner__in=TicketRole.objects.filter(user=user).all()).all()
        serializer = TicketDetailSerializer(queryset, many=True)
        return Response(serializer.data)