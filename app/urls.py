from django.urls import path,include
from .views import *

urlpatterns = [
    path('project/<int:pk>/', ProjectDetails.as_view()),
    path('ticket/<int:pk>/',TicketDetials.as_view(),name='ticket-details')
]