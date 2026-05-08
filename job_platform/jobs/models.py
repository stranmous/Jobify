from django.db import models
from django.contrib.auth.models import User

# Employer model linked to Django's User model
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

# Job model with all required fields
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    company_name = models.CharField(max_length=100)
    posted_by = models.ForeignKey(Employer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Application model to store job applications
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant_name = models.CharField(max_length=100)
    cover_letter = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application for {self.job.title} by {self.applicant_name}"
