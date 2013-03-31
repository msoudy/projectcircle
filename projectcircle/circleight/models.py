from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
	firstname = models.CharField(max_length=30) # first name
	lastname = models.CharField(max_length=30) # last name
	username = models.CharField(max_length=30, unique = True) # unique
	email = models.EmailField(unique = True) # unique
    profileimage = models.ImageField(upload_to='circleight/profilePicutres') # the image itself
	posts = models.CommaSeparatedIntegerField(max_length=1000) # The list of posts published by the user (by postid)

	def __unicode__(self):
		return u"%s %s" % (self.firstname, self.lastname)

class Comment(models.Model):
	user = models.ForeignKey(User) # owner of the comment
 	postid = models.IntegerField() # to which post it belongs
 	subject = models.TextField() # the subject of the comment
 	comment = models.TextField() # the content of the comment
 	pub_date = models.DateTimeField('date published') # publication date of the comment

 	def __unicode__(self):
 		return self.subject

class Interest(models.Model):
    interest = models.CharField(max_length=100) # the interest itself
    users = models.ManyToManyField(User) # list of users who share this interest

    def __unicode__(self):
        return self.interest

class ImagePost(models.Model):
    user = models.ForeignKey(User) # owner of the post
    image = models.ImageField(upload_to='circleight/images') # the image itself
    mimeType = models.CharField(max_length=20)
    text = models.TextField() # text attached to the post (description?)
    subject = models.TextField() # the subject of the post
    pub_date = models.DateTimeField('date published') # publication date of the post

    def __unicode__(self):
        return self.subject

class TextPost(models.Model):
    user = models.ForeignKey(User) # owner of the post
    subject = models.TextField() # the subject of the post
    text = models.TextField() # text attached to the post (description?)
    pub_date = models.DateTimeField('date published') # publication date of the post

    def __unicode__(self):
        return self.subject

class FilePost(models.Model):
    user = models.ForeignKey(User) # owner of the post
    myfile = models.FileField(upload_to='circleight/files') # the image itself
    text = models.TextField() # text attached to the post (description?)
    subject = models.TextField() # the subject of the post
    pub_date = models.DateTimeField('date published') # publication date of the post

    def __unicode__(self):
        return self.subject

