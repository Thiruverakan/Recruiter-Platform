import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from recruitment.models import Job, User, Candidate, Interviewer, Interview
from django.utils import timezone
from datetime import timedelta

# Get the specific recruiter
recruiter = User.objects.get(username='Thiruverakan6')
print(f"recruiter found: {recruiter.username}")

# Get or create a job for this recruiter
job = Job.objects.filter(recruiter=recruiter).first()
if not job:
    print("No job found for this recruiter. Creating one...")
    job = Job.objects.create(
        recruiter=recruiter,
        title="Senior Python Developer",
        description="Test description",
        requirements="Test requirements",
        location="Remote"
    )
print(f"Using job: {job.title} (ID: {job.id})")

# Ensure interviewers exist
interviewers = Interviewer.objects.all()
if not interviewers.exists():
    Interviewer.objects.create(name="Alice Johnson")
    Interviewer.objects.create(name="Bob Smith")
    print("Interviewers created")
interviewer = Interviewer.objects.first()

# Create a candidate for *this* job
candidate, created = Candidate.objects.get_or_create(
    email="test_candidate@example.com",
    defaults={
        'name': "Test Candidate (Mike)",
        'job': job,
        'status': 'INTERVIEW_SCHEDULED'
    }
)
print(f"Candidate: {candidate.name}")

# Schedule interview
if not hasattr(candidate, 'interview'):
    Interview.objects.create(
        candidate=candidate,
        interviewer=interviewer,
        date=timezone.now() + timedelta(days=1, hours=2)
    )
    print("Interview scheduled!")
else:
    print("Interview already exists for this candidate")
    # Update date to ensure it's in the future
    candidate.interview.date = timezone.now() + timedelta(days=1, hours=2)
    candidate.interview.save()
    print("Interview rescheduled to future date")
