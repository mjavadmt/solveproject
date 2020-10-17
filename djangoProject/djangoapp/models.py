from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Temp(models.Model):
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.pk} {self.message}"


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True)

    def natural_key(self):
        return (self.user.username)

    def __str__(self):
        return f"{self.pk} {self.user.username}"


class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True)

    def natural_key(self):
        return self.user.username

    def __str__(self):
        return f"{self.pk} {self.user.username}"


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def natural_key(self):
        return self.name

    def __str__(self):
        return f"{self.id} {self.name}"


class Related_subject(models.Model):
    subject = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, related_name="related_subjects", blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.category.name} : {self.subject}"


class Project(models.Model):
    producer = models.ForeignKey(Employer, related_name="projects_produced", on_delete=models.CASCADE, blank=True)
    solver = models.ForeignKey(Freelancer, related_name="projects_solved", on_delete=models.CASCADE, blank=True)
    interested_freelancers = models.ManyToManyField(Freelancer, related_name="interested_projects", blank=True)
    price_employer = models.IntegerField(default=0)
    category = models.ForeignKey(Category, related_name="projects_of_category", on_delete=models.CASCADE, blank=True,
                                 default=None)

    def __str__(self):
        return f"{self.pk} producer= {self.producer} -solver= {self.solver}"


class Price_Suggested_By_Freelancer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, related_name="project_prices")
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE, blank=True, related_name="freelancer_prices")
    price = models.IntegerField(default=0)


