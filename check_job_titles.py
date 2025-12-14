import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from recruitment.models import Job

print("--- Checking Jobs in Database ---")
for job in Job.objects.all():
    print(f"ID: {job.id}")
    print(f"Title Raw: '{job.title}'")
    print(f"Location Raw: '{job.location}'")
    print("-" * 20)
