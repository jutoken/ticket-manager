from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Status)
class StautsAdmin(admin.ModelAdmin):
    pass

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('pk','projet','contributor','status','title','passed_time','estimation')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk','contributor')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    pass