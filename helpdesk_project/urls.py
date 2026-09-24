from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tickets/add/', views.add_ticket, name='add_ticket'),
    path('tickets/<int:ticket_id>/close/', views.close_ticket, name='close_ticket'),
]
