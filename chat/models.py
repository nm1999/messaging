from django.db import models

# Create your models here.

class chats(models.Model):
    chat_id = models.CharField(max_length =3)
    name = models.CharField(max_length=20)
    message = models.CharField(max_length = 30)

class online(models.Model):
    user_id = models.CharField(max_length=20)
    name = models.CharField(max_length= 20)
    email = models.EmailField(max_length=30)
    


