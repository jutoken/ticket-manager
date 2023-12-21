from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    tickets = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='ticket-details')
    class Meta:
        model = Project
        fields = ('id','name','tickets')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')
        
class CommentsSertialzer(serializers.ModelSerializer):
    contributor = UserSerializer()
    class Meta:
        model = Comment
        fields = ('id','content','date','contributor')
                
class TrackSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Track
        fields = ('id','tasks','time','user','date')
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['name']
        
class TicketSerializer(serializers.ModelSerializer):
    comments = CommentsSertialzer(many=True)
    tracks = TrackSerializer(many=True)
    status = StatusSerializer()
    class Meta:
        model = Ticket
        fields = ('id','title','description','estimation','passed_time','type','status','parent_task','comments','tracks')
