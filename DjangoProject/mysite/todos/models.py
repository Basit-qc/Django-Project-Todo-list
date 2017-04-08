# Third Party
from django.db import models


class TodoTask(models.Model):
    """ Todo task table in database """
    task_name = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name + ' ' + self.description
