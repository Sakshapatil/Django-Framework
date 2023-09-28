from django.contrib import admin
from django.urls import path
from student.views import *
admin.site.site_header = "Sakshi Admin"
admin.site.site_title = "Sakshi Admin Portal"
admin.site.index_title = "Welcome to Sakshi's Portal"




urlpatterns = [
    path('',student,name="student"),
    path('tutor/', tutor,name="tutor"),
    path('admin1/',admin1,name="Admin"),
    path('admin/', admin.site.urls),
]