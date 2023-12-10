from django.shortcuts import render
from rest_framework import generics
from .models import Ticket, Track, Comment, Status, Project
from .serializers import *

class StatusByProject(generics.ListAPIView):
    serializer_class = StatusSerializes

    def get_queryset(self):
        project = Project.objects.filter(pk=self.kwargs['pk'])
        return project[0].status
    
class TicketsByStatus(generics.ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        projectId = self.kwargs['pk']
        statusId = self.kwargs['pk_status']
        return Ticket.objects.filter(projet=projectId,status=statusId)
    
class ListAllTicketsByProject(generics.ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.filter(projet=self.kwargs['pk'])
    
class CommentsByTicket(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(ticket=self.kwargs['pk'])
    
class TrackingByTicket(generics.ListCreateAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        return Track.objects.filter(ticket=self.kwargs['pk'])