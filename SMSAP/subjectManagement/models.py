from django.db import models
# from classManagement.models import 

class SubjectList(models.Model):
    SubjectName = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.SubjectName

class SubjectSelectionList(models.Model):
    Subject = models.ManyToManyField(SubjectList)
    