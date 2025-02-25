# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.phn, name='phn'),  # Or wherever your main view is
    path('addnumber/', views.addnumber, name='addnumber'),
    path('display/', views.display, name='display'),  # This line should exist
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
