from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    
class Server(models.Model):
    serverno=models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    desc=models.TextField()
    slug=models.CharField(max_length=130)

    def __str__(self) -> str:
            return 'Server for ' + self.name 

class ServerRoom(models.Model):
    sno= models.AutoField(primary_key=True)
    message=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Server, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username 