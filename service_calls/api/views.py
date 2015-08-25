'''
Created on Apr 26, 2015

@author: eytan
'''

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.forms.models import ModelForm
from django.http.response import HttpResponse, Http404
from django.shortcuts import render_to_response, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import ntpath
import os
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK
import shutil
import zipfile

from service_calls.api.serializers import TicketSerializer, \
    TicketDetailSerializer, TicketCommentSerializer
from service_calls.content import TICKET_ROLE, TICKET_DEPARTMENT
from service_calls.content.serializers import TicketEventSerializer
from service_calls.models.files import TicketFile, FILES_ROOT
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_comment import TicketComment
from service_calls.models.ticket_event import TicketEvent
from service_calls.models.ticket_role import TicketRole
from service_calls.settings import BASE_DIR
from django.views.static import serve

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
    
class AllTicketList(generics.ListAPIView):
    
    serializer_class = TicketDetailSerializer

    def get_queryset(self):
        return Ticket.objects.all()
    
    def get(self, request):
        return self.list(request)
    
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`     
        queryset = Ticket.objects.all()
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
    
    def post(self, request, *args, **kwargs):
        if not "initiator" in request.DATA.keys():
            user = request.user
            role = user.ticket_roles.all()[0]
            request.DATA["initiator"] = role.id
        return CreateAPIView.post(self, request, *args, **kwargs)
    
class UpdateTicketView(UpdateAPIView):
#     model = Ticket
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return UpdateAPIView.put(self, request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return UpdateAPIView.patch(self, request, *args, **kwargs)
    
class AddTicketComment(CreateAPIView):
    model = TicketComment
    serializer_class = TicketCommentSerializer
        
@api_view(['POST'])
def ticket_comments(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    serializer = TicketCommentSerializer(ticket.comments.all(), many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def user_info(request, username):
    
    if not request.user or not request.user.is_authenticated():
        return HttpResponse(status = HTTP_403_FORBIDDEN)
    
    try:
        user = User.objects.get(username=username)
        roles = user.ticket_roles.all()
        
        data = {'first_name': user.first_name, \
                'last_name': user.last_name,\
                'roles': [{'role': TICKET_ROLE.name(role.role), 'department': TICKET_DEPARTMENT.name(role.department)} for role in roles]}
        return HttpResponse(content = json.dumps(data), content_type="application/json", status=HTTP_200_OK)
        
    except TicketRole.DoesNotExist:
        return HttpResponse(status = HTTP_403_FORBIDDEN)
    
@api_view(['POST', 'GET'])
def roles(request):
    
    if not request.user or not request.user.is_authenticated():
        return HttpResponse(status = HTTP_403_FORBIDDEN)
    
    try:
        data = [{'username':role.username,\
                 'first_name': role.first_name, \
                'last_name': role.last_name,\
                'role': TICKET_ROLE.name(role.role),\
                'department': TICKET_DEPARTMENT.name(role.department),
                'id':role.id} for role in TicketRole.objects.all()]
        return HttpResponse(content = json.dumps(data), content_type="application/json", status=HTTP_200_OK)
        
    except TicketRole.DoesNotExist:
        return HttpResponse(status = HTTP_403_FORBIDDEN)
    
        
@api_view(['POST', 'GET'])
def role_info(request, role_id):
    
    if not request.user or not request.user.is_authenticated():
        return HttpResponse(status = HTTP_403_FORBIDDEN)
    
    try:
        role = TicketRole.objects.get(id=role_id)
        
        data = {'first_name': role.first_name, \
                'last_name': role.last_name,\
                'role': TICKET_ROLE.name(role.role),\
                'department': TICKET_DEPARTMENT.name(role.department)}
        return HttpResponse(content = json.dumps(data), content_type="application/json", status=HTTP_200_OK)
        
    except TicketRole.DoesNotExist:
        return HttpResponse(status = HTTP_403_FORBIDDEN)

class TicketFieldForm(ModelForm):
    class Meta:
        model = TicketFile
        fields = ('ticket', 'file')
        
    
@api_view(['GET', 'POST'])    
def upload_ticket_file(request,):    
    if request.method == 'POST':
        form = TicketFieldForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = TicketFieldForm()
    return render(request, 'ticket_file_upload.html', {'form': form})
        
@api_view(['GET', 'POST'])
def download_ticket_files(request):
    def clean_folder(folder):
        for path in os.listdir(folder):
            file_path = os.path.join(folder, path)
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path, ignore_errors=True)
            except Exception as e:
                print e

    def ticket_file_name(path):
        ticket_dir, file_name = ntpath.split(path)
        return "_".join([ntpath.split(ticket_dir)[1], file_name])

    def zipdir(path, zip):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                zip.write(file_path, arcname=ticket_file_name(file_path))

    zip_filename = os.path.join(BASE_DIR, 'ticket_files.zip')
    zipf = zipfile.ZipFile(zip_filename, 'w')
    zipdir(FILES_ROOT, zipf)
    zipf.close()
    clean_folder(FILES_ROOT)
    
    return serve(request, os.path.basename(zip_filename), os.path.dirname(zip_filename))
    
    