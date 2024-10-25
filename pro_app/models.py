from django.db import models

# Create your models here.

class Commant(models.Model):
   
    email = models.EmailField(max_length=254)
    your_comment = models.TextField()
    