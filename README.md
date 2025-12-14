# AI-Smart Recruiter Platform

## Project Overview
The **AI-Smart Recruiter Platform** is a Django-based web application designed to streamline the hiring process. It connects Recruiters and Candidates through an intelligent interface that automates resume screening, manages interview schedules, and provides real-time status updates.

## Key Features

### 1. Recruiter Dashboard
*   **Job Management**: Create, update, and delete job postings with rich descriptions and requirements.
*   **Candidate Tracking**: View all applicants per job, filter by status (Applied, Shortlisted, Interview, Hired, Rejected).
*   **AI-Powered Resume Analysis**: Automatically parses candidate resumes and assigns a "Match Score" based on job requirements. Provides detailed semantic analysis (matched keywords, missing terms).
*   **Interview Management**: Schedule interviews with specific interviewers, dates, and notes.

### 2. Candidate Experience
*   **Job Portal**: Clean, responsive interface for candidates to browse and filter available jobs.
*   **Easy Application**: Simple one-click application process with resume upload.
*   **Smart Notifications**: Candidates receive **instant pop-up updates** upon login when their application status changes (e.g., "Interview Scheduled", "Rejected").

### 3. Privacy & Security
*   **Role-Based Access**: Strict separation between Recruiter and Candidate views.
*   **Private Notifications**: Alerts are strictly linked to specific user accounts. Candidates never see messages intended for others, even if they share similar data in testing scenerios.

---

## Design Decisions & Architecture

### 1. User Role Separation
We implemented a hard separation between the Recruiter and Candidate workflows:
*   **Recruiters** (`Thiruverakan6`) have full access to the backend dashboard (`/dashboard/`).
*   **Candidates** (`user01`, `user02`) are automatically redirected to the Job List (`/jobs/`) upon login. They cannot access the recruiter dashboard.

### 2. Notification System Philosophy
*   **Pop-up Only Approach**: To keep the candidate interface minimal and stress-free, we removed the persistent "Inbox" list.
*   **"Latest Update" Logic**: When a candidate logs in, the system checks for unread notifications. It intelligently displays **only the single most recent update** as a toast message and marks all older notifications as read. This prevents users from being bombarded with out-of-date alerts (e.g., seeing an "Interview" alert after already being "Rejected").
*   **Account Linking**: Notifications are generated based on a strict `User` Foreign Key link in the database, rather than just email matching. This ensures robust privacy in multi-user test environments.

### 3. Fail-Safe Operations
*   **Automated Interview Cleanup**: If a candidate with a scheduled interview is marked as **REJECTED**, the system automatically deletes the interview record to maintain data consistency.
*   **Robust Navigation**: Actions like "Reject Candidate" or "Confirm Interview" force explicit redirects to the appropriate list views (Candidate List or Interview List), preventing users from getting stuck on stale pages.

### 4. UI/UX Design
*   **Modern Aesthetics**: The application uses a "Glassmorphism" design capability with dark mode aesthetics (Tailwind CSS), ensuring a premium feel.
*   **Interactive Elements**: Hover effects, smooth transitions (fade-in-up), and responsive grids are used throughout.

---

## Assumptions

*   **User Management**: We assume candidates create accounts (or accounts are provisioned for them) before applying, allowing for the secure tracking of their status.
*   **Resume Parsing**: The AI analysis assumes resumes are uploaded in standard text-readable formats.
*   **Single Recruiter View**: The current iteration is optimized for a single recruiter or a small team sharing the recruiter view.

## Technology Stack
*   **Backend**: Django 6.0 (Python 3.13)
*   **Frontend**: HTML5, Tailwind CSS
*   **Database**: SQLite (Development)
*   **AI Engine**: Gemini API (Configurable)
