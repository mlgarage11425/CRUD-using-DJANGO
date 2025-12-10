from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='student_list'),
    path('add/', views.add_student, name='add_students'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]