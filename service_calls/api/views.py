'''
Created on Apr 26, 2015

@author: eytan
'''

from django.http.response import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
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
    
@csrf_exempt  
@api_view(['POST'])    
def create_ticket(request):
    serializer = TicketSerializer(data=request.DATA, many=False)
    try:
        if serializer.is_valid():
            instance = serializer.save()
            return HttpResponse("Created")
        else:
            return HttpResponse(serializer.error_messages, status=400)
    except Exception as e:
        return HttpResponse(str(e), status=500)
@csrf_exempt  
@api_view(['POST'])    
def update_ticket(request, pk):
    try:
        ticket = Ticket.objects.get(pk=pk)
        serializer = TicketSerializer(ticket, data=request.DATA, many=False)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Updated")
        else:
            return HttpResponse(serializer.error_messages, status=400)
    except Ticket.DoesNotExist:
        return HttpResponse("Ticket not found! - pk: %d" % pk, status=400)
    except Exception as e:
        return HttpResponse(str(e), status=500)
    