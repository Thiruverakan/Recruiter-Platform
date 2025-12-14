import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from recruitment.models import Interviewer, Candidate, Job, Interview
from django.utils import timezone
from datetime import timedelta
import random

# Create Interviewers
interviewers_data = ['Alice Johnson', 'Bob Smith', 'Charlie Brown']
for name in interviewers_data:
    Interviewer.objects.get_or_create(name=name, defaults={'specialization': 'Technical'})
print("Interviewers created.")

# Ensure we have jobs (we know we have some from previous steps, but let's be safe)
jobs = Job.objects.all()
if not jobs.exists():
    print("No jobs found. Please create a job first.")
else:
    # Create some dummy candidates for the first job
    job = jobs.first()
    candidates_data = [
        {'name': 'John Doe', 'email': 'john@example.com', 'status': 'APPLIED'},
        {'name': 'Jane Doe', 'email': 'jane@example.com', 'status': 'SHORTLISTED'},
        {'name': 'Mike Ross', 'email': 'mike@example.com', 'status': 'INTERVIEW_SCHEDULED'},
    ]
    
    for c_data in candidates_data:
        cand, created = Candidate.objects.get_or_create(
            email=c_data['email'],
            defaults={
                'name': c_data['name'], 
                'job': job, 
                'status': c_data['status']
            }
        )
        
        # Schedule interview for the one with INTERVIEW_SCHEDULED
        if c_data['status'] == 'INTERVIEW_SCHEDULED' and not hasattr(cand, 'interview'):
            interviewer = Interviewer.objects.first()
            Interview.objects.create(
                candidate=cand,
                interviewer=interviewer,
                date=timezone.now() + timedelta(days=2)
            )
            print(f"Scheduled interview for {cand.name}")

print("Mock data setup complete.")
