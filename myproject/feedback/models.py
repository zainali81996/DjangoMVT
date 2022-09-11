from django.db import models as mod

# Create your models here.


class feedbackModel(mod.Model):
    username = mod.CharField(max_length=20)
    email = mod.EmailField(null=False,unique=True)
    subject = mod.CharField(max_length=100)
    body = mod.TextField(max_length=500)


