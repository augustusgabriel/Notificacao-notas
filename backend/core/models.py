from django.db import models

# Temporário para testes
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
