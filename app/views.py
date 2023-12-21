from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.response import Response

class ProjectDetails(APIView):
    def get(self,request, pk,format=None):
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project,context={'request':request})
            return Response(serializer.data)
        except Project.DoesNotExist:
            raise Http404

class TicketDetials(APIView):
    def get(self,request,pk,format=None):
        try:
            ticket = Ticket.objects.get(pk=pk)
            serializer = TicketSerializer(ticket,context={'request':request})
            return Response(serializer.data)
        except Ticket.DoesNotExist:
            raise Http404
        
class StatusDetails(APIView):
    def get(self,request,pk,format=None):
        pass
