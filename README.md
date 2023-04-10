# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here
![entity](https://user-images.githubusercontent.com/120539823/230928210-ba2e7080-1c76-4e5c-bbd9-e7905df14fb1.png)

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

```python
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
![Screenshot (138)](https://user-images.githubusercontent.com/120539823/230928444-c076a369-5156-4638-8a66-07b0ee20d498.png)
##Verifying Primary-Key
![Screenshot (137)](https://user-images.githubusercontent.com/120539823/230928468-609da2e3-d242-4bd3-a5dd-569d8719d1b0.png)






## RESULT:
Thus we developed a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).
