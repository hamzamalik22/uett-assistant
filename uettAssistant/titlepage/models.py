from django.db import models

# Create your models here.
class TitlePage(models.Model):
    department = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=9)
    date = models.CharField(max_length=100)
    section = models.CharField(max_length=100)

    def __str__(self):
        return self.title
