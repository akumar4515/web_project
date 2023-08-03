from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=255, null=True)
    lname = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True)
    lnkDn = models.URLField(max_length=255, null=True, blank=True)
    bio = models.TextField(default='your bio')
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/', default='img.png')
    created= models.DateTimeField(auto_now=True)
    updated= models.DateTimeField(auto_now_add=True).default=timezone.now()
    
    def __str__(self):
        return f"{self.fname} {self.lname} ({self.birth_date})"
    



class Message(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Task')
    content = models.TextField(verbose_name='Task',null=True)
    def __str__(self):
        return self.user.username

 


class Courses(models.Model):
    name=models.TextField(verbose_name='course',null=True)   
    def __str__(self):
        return self.name
    
    
class Topic(models.Model):
    courses=models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='course' , null=True)
    topic=models.TextField(verbose_name='topic', null=True)

    
    def __str__(self):
        return self.topic
    
class Sub_topic(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='topic' , null=True)
    sub_topic=models.TextField(verbose_name='sub_topic', null=True)
    
    def __str__(self):
        return self.sub_topic
    
    
    
class contents(models.Model):
    sub_topic=models.ForeignKey(Sub_topic, on_delete=models.CASCADE, verbose_name='topic', null=True)
    content=models.TextField(verbose_name='content', null=True)
    image=models.ImageField(upload_to='cont_img', null=True)
    file=models.FileField(upload_to="cont_file", null=True)
   
    
    def __str__(self):
        return f'{self.sub_topic}'