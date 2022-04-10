from django.db import models

# Create your models here.


class UserEmail(models.Model):
    UserId = models.AutoField(primary_key=True, unique=True, default=True)
    user_email = models.CharField(max_length=500)


