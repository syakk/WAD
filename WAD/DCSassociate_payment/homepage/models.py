from django.db import models

# Create your models here.
class Associate(models.Model):
    associate_studentID = models.CharField(max_length = 12, primary_key = True)
    username = models.CharField(max_length = 20)
    password = models.TextField()
    name = models.TextField()

class Student(models.Model):
    studentID = models.CharField(max_length = 12, primary_key = True)
    studentName = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length = 12)
    course_code = models.CharField(max_length = 3)
    payment_status = models.CharField(max_length = 6)

class Payment(models.Model):
    paymentID = models.CharField(max_length = 9, primary_key = True )
    studentID = models.ForeignKey(Student, on_delete = models.CASCADE)
    payment_amount = models.FloatField()
    payment_date = models.DateField()

class Affair(models.Model):
    affair_id = models.CharField(max_length = 9, primary_key = True)
    eventName = models.TextField()
    eventDate = models.DateField()
    eventDescription = models.TextField()