# Deployment Guide

I have successfully prepared your project for permanent 24/7 deployment. 
Because I cannot create a cloud account for you, you must perform the final "upload" step.

**Why is this necessary?**
Running `runserver` on your laptop only works while your laptop is ON and the terminal is OPEN. To have it work for 5 days autonomously, the code must live on a server (like Render, Railway, or Heroku).

## Option A: Deploy to Render (Free & Permanent) - Recommended

1.  **Push your code to GitHub** (Create a repository and upload all files).
2.  Go to [dashboard.render.com](https://dashboard.render.com/).
3.  Click **New +** -> **Web Service**.
4.  Connect your GitHub repository.
5.  Render will auto-detect the configuration because I created the `Procfile` and `requirements.txt` for you.
6.  Click **Deploy**.

## Option B: Deploy to PythonAnywhere (Easiest for Beginners)

1.  Sign up at [pythonanywhere.com](https://www.pythonanywhere.com/).
2.  Upload your folder.
3.  Run `pip install -r requirements.txt`.
4.  Reload the web app.

## Files Created for You
*   `Procfile`: Tells the cloud server how to run Gunicorn.
*   `requirements.txt`: Lists all libraries needed (Django, WhiteNoise, etc).
*   `runtime.txt`: Specifies the Python version.
*   `config/settings.py`: Configured to use WhiteNoise for static files.
