from django.db import models
from django.contrib import admin
# Create your models here.
class Student(models.Model):
    class Meta():
        permissions = (("view_labs", "Can view lab details."),
                ("view_marks", "can view semester marks"),
                )
    studentname = models.CharField(max_length=100,primary_key= True)
    refno = models.CharField(max_length=100)
    lastname= models.CharField(max_length=80)
    emailid = models.EmailField()
    age=models.CharField(max_length=10)
    mobile=models.CharField(max_length=10)

    
class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentname','refno','lastname','emailid','age','mobile')