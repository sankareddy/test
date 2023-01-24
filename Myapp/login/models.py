from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class loginhistory(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    login_date_time = models.DateTimeField()