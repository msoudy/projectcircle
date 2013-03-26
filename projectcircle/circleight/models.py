from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=200)
    userid = models.IntegerField()
    comment = models.TextField()
    
    def __unicode__(self):
        return self.name
# Create your models here.
