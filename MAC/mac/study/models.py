from django.db import models

# Create your models here.
class studyresource(models.Model):
    courseid = models.AutoField(primary_key=True)
    course = models.CharField(max_length = 255)
    file = models.FileField(upload_to='uploads/')

def __str__(self):
    return "%s %s" %(self.name, self.email)