from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=20,primary_key=True) #ID는 유일키 식별가능해야 함.
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.id
