from rest_framework import serializers
from .models import Project, Track, Ticket, Comment, Status
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class StatusSerializes(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields  = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    status = StatusSerializes(many=True)
    class Meta:
        model = Project
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    contributor = UserSerializer()
    class Meta:
        model = Ticket
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer()
    class Meta:
        model = Track
        fields = '__all__'