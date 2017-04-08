""" Model for Todo list """
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
#from django.template.defaultfilters import default

# Create your models here.
class Todo_task(models.Model):
    """ Todo task table in database """
    summary = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    user = models.ForeignKey(User)
    url_address = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True, default=datetime.now())
    
    def __unicode__(self):
        return self.summary+' '+self.description+' '+self.url_address
