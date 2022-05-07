from django.db import models

# Create your models here.

#model with an image, name of the college, and name of the highschool
class HSAdmissions(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    highschool = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    def __str__(self):
        return self.name