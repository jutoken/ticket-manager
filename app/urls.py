from django.urls import path,include
from .views import *
urlpatterns = [
    # list project status
    path('project/<int:pk>/status',StatusByProject.as_view()),
    # list tickets by status
    path('project/<int:pk>/status/<int:pk_status>/tickets/',TicketsByStatus.as_view()),
    # # list all ticket by project
    path('project/<int:pk>/tickets/',ListAllTicketsByProject.as_view()),
    # # list comments by ticket
    path('ticket/<int:pk>/comments/',CommentsByTicket.as_view()),
    # # list tracking by ticket
    path('ticket/<int:pk>/tracking/',TrackingByTicket.as_view()),

]