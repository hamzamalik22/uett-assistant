import uuid
from django.db import models

class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=10)

    def __str__(self):
        return self.nickname
    

class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    credit_hour = models.IntegerField(default=3)
    associated_name = models.CharField(max_length=200, default="not_assigned")  
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.associated_name if self.associated_name != 'not_assigned' else f'{self.name} - {self.department.nickname}'  # Use associated_name if available, otherwise generate from name and department nickname
    
    def save(self, *args, **kwargs):
        if not self.associated_name:  # Check if associated_name is not set
            self.associated_name = f'{self.name} - {self.department.nickname}'
        super().save(*args, **kwargs)

class Semester(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f'{self.name} : {self.department.name}' 
