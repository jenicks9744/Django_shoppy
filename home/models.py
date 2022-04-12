from django.db import models

# Create your models here.

class item(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    desc=models.CharField(max_length=100)
    feature=models.CharField(max_length=100,default='NULL')

    def __str__(self):
        return str(self.id)+":"+self.name
        



