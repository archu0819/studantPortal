from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    class meta:
        #verbose_name='Notes'
        verbose_name_plural="Notes"

    def __str__(self):
        return self.title
    
    

 
