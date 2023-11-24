from django.contrib import admin
from .models import Student, Course, Gradevalue, Classe, Stuclasse


admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Gradevalue)
admin.site.register(Classe)
admin.site.register(Stuclasse)

