# from django.db import models

# # Create your models here.

# class Student(models.Model):
#     name = models.CharField(max_length=50)
#     student_email = models.EmailField(max_length=100)
#     personal_email = models.EmailField(max_length=100)
#     locker_number = models.IntegerField()
#     locker_combination = models.CharField(max_length=8)
#     good_student = models.BooleanField()


from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False)
    student_email = models.EmailField(null = False, blank = False, unique=True)
    personal_email = models.EmailField(null = True, blank = True, unique=True)
    locker_number = models.IntegerField(default=110, null = False, blank = False, unique=True)
    locker_combination = models.CharField(max_length=255, null = False, blank = False, default="12-12-12")
    good_student = models.BooleanField(default=True, null=False)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker}"
    
    def locker_reassignment(self, num):
        self.locker_number = num
        self.save()
      
        
    def student_status(self, booly):
        self.good_student = booly
        self.save()
       