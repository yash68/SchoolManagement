from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	address = models.TextField()
	image = models.ImageField(upload_to="studentimages",blank=True,null=True)

	def __str__(self):
		return self.name
		

class TeacherProfile(models.Model):

	APPROVAL_CHOICES = (('APPROVED', 'Approved'),
						('PENDING','Pending'),
						('REJECTED','Rejected'),
						)

	user = models.OneToOneField(User, on_delete = models.CASCADE)
	name = models.CharField(max_length=20)
	age = models.IntegerField(null = True)
	subject = models.CharField(max_length=20, null = True)
	contact_no = models.IntegerField(null = True)
	address = models.TextField(max_length=20, null = True)
	approval_status = models.CharField(max_length=8,null=False,blank=False,choices=APPROVAL_CHOICES, default='Pending')
