# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Fork and clone the repositary in to your IDE.
### STEP 2:
Create a django project and an app and a superuser account and run the server.
### STEP 3:
Modify changes in settings and write ur code on models and admin and run the server.
### STEP 4:
 Login in to admin using your superuser account and populate the records.

## PROGRAM

```
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
```

## OUTPUT
![1](https://user-images.githubusercontent.com/120539823/230255980-ddb87acb-04bf-410e-9a55-9e6be66b70d3.jpg)
![2](https://user-images.githubusercontent.com/120539823/230255995-5f6af6e1-6529-4a9e-b346-8a8c3857ab2b.jpg)


## RESULT:
Thus we developed a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).
