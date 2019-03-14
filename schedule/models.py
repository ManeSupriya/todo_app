from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Schedule(models.Model):
	task_id = models.IntegerField(default=-1)
	title = models.CharField(max_length=100)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	user_name = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	completed = models.BooleanField(default=False)
	sign = models.ImageField(default="not_done.png",blank=True)
	delete =models.ImageField(default="delete.png",blank=True)
	def __str__(self):
		return self.title
	
	def snippet(self):
		return self.description[:10]+"..."


class user_list(models.Model):
	user_name = models.CharField(max_length=30, default=None)
	task_index = models.IntegerField(default=-1)

