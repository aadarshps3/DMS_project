from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_student=models.BooleanField(default=False)
    name = models.CharField(max_length=25,null=True)
    guardian_name = models.CharField(max_length=25,null=True)
    gender = models.CharField(max_length=25,null=True)
    date_of_birth = models.DateField(null=True)
    department = models.CharField(max_length=25,null=True)
    mobile_no = models.CharField(max_length=25,null=True)
    address = models.TextField(null=True)
    photo = models.ImageField(upload_to='photos',null=True)
    blood_group = models.CharField(max_length=10)
    Admission_No = models.CharField(max_length=10)



class Notification(models.Model):
    to = models.CharField(max_length=25)
    subject = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.subject

class Attendance(models.Model):
    student = models.ForeignKey(Login, on_delete=models.CASCADE)
    date = models.DateField()
    attendance = models.CharField(max_length=100)
    time = models.TimeField()


class internal_mark(models.Model):
    student = models.ForeignKey(Login,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    seminar_mark = models.IntegerField()
    assignment_mark = models.IntegerField()
    testpaper_mark = models.IntegerField()

