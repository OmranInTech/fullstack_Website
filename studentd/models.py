from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    student_id = models.CharField(max_length=20, unique=True)  # Making student_id unique
    address = models.TextField()

    def __str__(self):
        return self.full_name
