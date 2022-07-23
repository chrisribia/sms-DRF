from django.db import models
 

class ClassList(models.Model):
    classNames = models.CharField(max_length=255,unique=True)
    Teacher = models.CharField(max_length=255, default=None)
    def __str__(self):
        return self.classNames
     

class ClassMembers(models.Model):
    classNames = models.ManyToManyField(ClassList)      
    classMemberReg = models.CharField(max_length=50, default=None)