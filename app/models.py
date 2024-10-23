from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.Topic_name
class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.EmailField(default='aravind@gmail.com')
    def __str__(self):
        return self.name
class Accessrecord(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100) 
    date=models.DateField()
    def __str__(self):
        return self.name

