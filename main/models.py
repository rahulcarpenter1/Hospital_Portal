from django.db import models

class Crud(models.Model):
    name =  models.CharField(max_length=100)
    admit = models.DateTimeField(auto_now_add=True)
    case = models.CharField(max_length=100)
    refer = models.CharField(max_length=100)
    scheme = models.CharField(max_length=100)
    status = models.CharField(max_length=50)