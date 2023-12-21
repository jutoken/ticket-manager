from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError

class Status(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=30)
    contributors = models.ManyToManyField('auth.User',related_name='projects')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    projet = models.ForeignKey(Project,related_name='tickets',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    contributor = models.ForeignKey('auth.User',related_name='tickets',on_delete=models.CASCADE)
    estimation = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    passed_time = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    type = models.CharField(max_length=10,choices=[('master','master'),('normal','noraml')])
    date = models.DateTimeField(default=timezone.now)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    parent_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='child_tasks')
        
    def __str__(self):
        return self.title

class Track(models.Model):
    # tracking the past time not coming time
    def no_future(value):
        if value > timezone.now():
            raise ValidationError('cannot be in the future')
        
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name='tracks')
    tasks = models.TextField(max_length=2000)
    time = models.DecimalField(default=0.01,max_digits=10,decimal_places=2)
    user = models.ForeignKey('auth.User',related_name='tracks',on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now,validators=[no_future])

    def __str__(self):
        return self.ticket.title

class Comment(models.Model):
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name='comments')
    contributor = models.ForeignKey('auth.User',related_name='comments',on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.pk)

# Signal to update ticket time
@receiver(post_save,sender=Track)
def add_passed_time_into_ticket(sender,instance,**kwargs):
    latest_time = instance.time+instance.ticket.passed_time
    Ticket.objects.filter(pk=instance.ticket.pk).update(passed_time=latest_time)