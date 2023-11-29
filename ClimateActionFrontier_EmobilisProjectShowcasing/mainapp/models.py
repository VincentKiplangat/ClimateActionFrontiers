import os
import uuid

from django.db import models


# def unique_img_name(instance, filename):
#     name = uuid.uuid4()
#     print(name)
#     ext = filename.split(".")[-1]
#     print(name)
#     full_name = f"{name}.{ext}"
#     # full_name = "%s.%s" % (name,ext)
#     return os.path.join("employees".full_name)

def unique_img_name(instance, filename):
    # Generate a unique name using UUID
    name = (uuid.uuid4())
    # Extract the file extension from the original filename
    ext = filename.split(".")[-1]

    # Create the full unique image name with the same extension
    full_name = f"{name}.{ext}"
    return os.path.join("employees", full_name)


# Create your models here.
class Employee(models.Model):
    # name, email, dob , salary, disabled
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)  # 67000.58
    disabled = models.BooleanField(default=False)
    profile = models.ImageField(upload_to=unique_img_name, null=True, default="employees/employeeee.png")
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True)  # Every time an update happens

    def __str__(self):
        return self.name

# SCHEDULE A COMMAND USING CELERY TASKS
# # ********************************************************************
# # django_project/users/models.py
# from django.utils import timezone
# ...
# class SubscribedUsers(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True, max_length=100)
#     created_date = models.DateTimeField('Date created', default=timezone.now)
#
#     def __str__(self):
#         return self.email
# # *******************************************
