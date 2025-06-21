from django.db import models

# Create your models here.
class StudentRecord(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    mark = models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.subject}"
