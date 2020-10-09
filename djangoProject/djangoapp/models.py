from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Temp(models.Model):
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.pk} {self.message}"


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000,blank=True)


    def __str__(self):
        return f"{self.pk} {self.user.username}"


class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.pk} {self.user.username}"

class Project(models.Model):
    producer = models.ForeignKey(Employer, related_name="projects_produced", on_delete=models.CASCADE, blank=True)
    solver = models.ForeignKey(Freelancer, related_name="projects_solved", on_delete=models.CASCADE, blank=True)
    interested_freelancers = models.ManyToManyField(Freelancer, related_name="interested_projects", blank=True)
    price_employer = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pk} producer= {self.producer} -solver= {self.solver}"


class Price_Suggested_By_Freelancer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE,blank=True)
    price = models.IntegerField(default=0)

# class Client(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     mobile_number = models.IntegerField(blank=True)
#     # interested_projects = models.ForeignKey(Project, related_name="interested_freelancer")
#     # projects = models.ForeignKey(Project , on_delete=models.CASCADE)
