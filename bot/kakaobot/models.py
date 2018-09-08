from django.db import models

class DomesticClinic(models.Model):
	name=models.CharField(max_length=200)
	location=models.CharField(max_length=500)
	phone=models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Message(models.Model):
	message=models.CharField(max_length=500)

	def __str__(self):
		return self.message
