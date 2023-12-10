from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Status"


class Project(models.Model):
    name = models.CharField(max_length=30)
    status = models.ManyToManyField(Status)
    contributors = models.ManyToManyField(User)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    projet = models.ForeignKey(Project,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    contributor = models.ForeignKey(User,on_delete=models.CASCADE)
    estimation = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    passed_time = models.DecimalField(default=0.01,max_digits=10,decimal_places=2)
    type = models.CharField(max_length=10,choices=[('master','master'),('normal','noraml')])
    date = models.DateTimeField()
    status = models.ForeignKey(Status,on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        if self.status not in self.projet.status.all():
            raise ValueError("The selected status does not belong to the project's available statuses.")
        
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    def no_future(value):
        if value > timezone.now():
            raise ValidationError('cannot be in the future')
        
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
    contributor = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    time = models.DecimalField(default=0.01,max_digits=10,decimal_places=2)
    date = models.DateTimeField(default=datetime.now(),validators=[no_future])

    def __str__(self):
        return str(self.pk)

# Signal to update ticket time
@receiver(post_save,sender=Comment)
def add_passed_time_into_ticket(sender,instance,**kwargs):
    latest_time = instance.time+instance.ticket.passed_time
    Ticket.objects.filter(pk=instance.ticket.pk).update(passed_time=latest_time)