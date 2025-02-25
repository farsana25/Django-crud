from django.urls import path
from . import views

urlpatterns = [
  path('', views.phn, name='phn'),
    path('add_student/', views.add_student, name='add_student'),
   path('update/<int:id>', views.updateData, name='update'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
]
