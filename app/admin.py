from django.contrib import admin
from .models import Project, Ticket, Comment, Status, Track

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('pk','contributor','status','title','passed_time','estimation')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk','contributor')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    pass