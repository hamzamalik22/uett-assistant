from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=10)

    def __str__(self):
        return self.nickname
    
class Subject(models.Model):
    name = models.CharField(max_length=200)
    associated_name = models.CharField(max_length=200, default="not_assigned")  # Change default value
    credit_hour = models.IntegerField(default=3)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,default=1)  # Add this line

    def __str__(self):
        return self.associated_name
    
    def save(self, *args, **kwargs):
        if self.associated_name == 'not_assigned':  # If associated_name is not provided, set it to the associated department's nickname
            self.associated_name = f'{self.name} - {self.department.nickname}'
        super().save(*args, **kwargs)



# class Subject(models.Model):
#     name = models.CharField(max_length=200)
#     associated_name = models.CharField(max_length=200, default="not_assigned")  # Change default value
#     credit_hour = models.IntegerField(default=3)

#     def __str__(self):
#         return self.name
    
# class Semester(models.Model):
#     name = models.CharField(max_length=200)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     associated_name = models.CharField(max_length=200,default=department.nickname)
#     subjects = models.ManyToManyField(Subject)

#     def __str__(self):
#         return self.associated_name

class Semester(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    associated_name = models.CharField(max_length=200, default="not_assigned")  # Change default value
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.associated_name

    def save(self, *args, **kwargs):
        if self.associated_name == 'not_assigned':  # If associated_name is not provided, set it to department's nickname
            self.associated_name = f'{self.name} - {self.department.nickname}'
        super().save(*args, **kwargs)
