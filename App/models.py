from django.db import models

# Create your models here.
class student_model(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return  str(self.pk) + " "+self.name
