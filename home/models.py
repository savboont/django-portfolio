from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class User(models.Model):
	name = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)
	phone = PhoneNumberField(unique=True, null=False, blank=False)
	email = models.EmailField()
	telegram = models.CharField(max_length=100)
	hhru = models.CharField(max_length=100)

	def __str__(self):
		return self.name + ' ' + self.surname


class Project(models.Model):
	proj_name = models.CharField(max_length=100)
	description = models.TextField()
	proj_link = models.CharField(max_length=100)
	images = models.ImageField(upload_to='images')
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.proj_name


class Skill(models.Model):
	name_skill = models.CharField(max_length=50)
	grade = models.IntegerField()

	def __str__(self):
		return self.name_skill


class CompletedCourse(models.Model):
	comp_course = models.TextField(null=True)

	def __str__(self):
		return self.comp_course


class UncompletedCourse(models.Model):
	uncomp_course = models.TextField(null=True)

	def __str__(self):
		return self.uncomp_course
