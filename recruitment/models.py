from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Job(models.Model):
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Candidate(models.Model):
    STATUS_CHOICES = [
        ('APPLIED', 'Applied'),
        ('SHORTLISTED', 'Shortlisted'),
        ('INTERVIEW_SCHEDULED', 'Interview Scheduled'),
        ('REJECTED', 'Rejected'),
        ('HIRED', 'Hired'),
    ]
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='candidates')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    resume_file = models.FileField(upload_to='resumes/', null=True, blank=True)
    experience_years = models.IntegerField(default=0)
    current_location = models.CharField(max_length=100, default='')
    work_preference = models.CharField(
        max_length=50, 
        choices=[('REMOTE', 'Remote'), ('ONSITE', 'On-site'), ('HYBRID', 'Hybrid')],
        default='REMOTE'
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='APPLIED')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # AI Analysis Fields
    match_score = models.FloatField(default=0.0)
    ai_analysis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Interviewer(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200, default='General')
    
    def __str__(self):
        return self.name

class Interview(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, related_name='interview')
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE, related_name='interviews')
    date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interview: {self.candidate.name} with {self.interviewer.name}"

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient.username}"
