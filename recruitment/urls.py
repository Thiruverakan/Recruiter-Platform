from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    
    # Recruiter Job Management
    path('recruiter/jobs/', views.JobListView.as_view(), name='job_list'),
    path('recruiter/jobs/create/', views.JobCreateView.as_view(), name='job_create'),
    path('recruiter/jobs/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('recruiter/jobs/<int:pk>/update/', views.JobUpdateView.as_view(), name='job_update'),
    path('recruiter/jobs/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
    
    # Recruiter Candidates
    path('candidates/', views.CandidateListView.as_view(), name='candidate_list'),
    path('candidates/<int:pk>/', views.CandidateDetailView.as_view(), name='candidate_detail'),
    path('candidates/<int:candidate_id>/analyze/', views.analyze_candidate_cv, name='analyze_candidate'),
    path('candidates/<int:candidate_id>/status/', views.update_candidate_status, name='update_candidate_status'),
    path('candidates/<int:candidate_id>/interview/', views.schedule_interview, name='schedule_interview'),
    path('interviews/', views.InterviewListView.as_view(), name='interview_list'),
    path('candidate/<int:candidate_id>/delete/', views.delete_candidate, name='delete_candidate'),
    path('interview/<int:pk>/edit/', views.InterviewUpdateView.as_view(), name='interview_update'),
    path('interview/<int:interview_id>/delete/', views.delete_interview, name='delete_interview'),
    
    # Candidate URLs (Public/User facing)
    path('jobs/', views.CandidateJobListView.as_view(), name='candidate_job_list'),
    path('jobs/<int:job_id>/apply/', views.apply_to_job, name='apply_job'),

    path('api/generate-description/', views.generate_job_description, name='generate_job_description'),
]
