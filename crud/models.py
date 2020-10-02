from django.db import models

class About(models.Model):
	name=models.CharField(max_length=100)
	sub=models.CharField(max_length=100)
	num=models.IntegerField()