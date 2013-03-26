from django.contrib.auth.models import User
from django.db import models

class Comment(models.Model):
	username = models.CharField(max_length=30) # unique
 	postid = models.IntegerField()
 	comment = models.TextField()

 	def __unicode__(self):
 		return self.username


class User(models.Model):
	fname = models.CharField(max_length=200) # first name
	lname = models.CharField(max_length=200) # last name
	username = models.CharField(max_length=30) # unique
	posts = models.CommaSeparatedIntegerField(max_length=1000) # The list of posts (by postid)

