from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_student', add_student, name='add_student'),
    path('delete_student/<int:myid>/', delete_student, name='delete_student'),
    path('edit_student/<int:myid>/', edit_student, name='edit_student'),
    path('update_student/<int:myid>/', update_student, name='update_student'),

    path('classes', classes, name='classes'),
    path('add_classes', add_classes, name='add_classes'),
    path('delete_classes/<int:myid>/', delete_classes, name='delete_classes'),
    path('edit_classes/<int:myid>/', edit_classes, name='edit_classes'),
    path('update_classes/<int:myid>/', update_classes, name='update_classes'),

    path('stuclasses', stuclasses, name='stuclasses'),
    path('add_stuclasses', add_stuclasses, name='add_stuclasses'),
    path('delete_stuclasses/<int:myid>/', delete_stuclasses, name='delete_stuclasses'),
    path('edit_stuclasses/<int:myid>/', edit_stuclasses, name='edit_stuclasses'),
    path('update_stuclasses/<int:myid>/', update_stuclasses, name='update_stuclasses')
]
