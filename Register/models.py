from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cnum=models.PositiveBigIntegerField(null=True)
    address=models.TextField(null=True)
    pimg=models.ImageField(upload_to="mdedia/profilepics",default="media/default/def.jpg")
    updated_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username