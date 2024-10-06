from django.db import models

class SignUp(models.Model):
    username = models.CharField(max_length = 30, null=False, blank=False, unique=True)
    password = models.CharField(max_length = 50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    first_name = models.CharField(max_length = 50, null=False, blank=False)
    last_name = models.CharField(max_length = 50, null=False, blank=False)

    def __str__(self):
        return self.username

# Create your models here.
