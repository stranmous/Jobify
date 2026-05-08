# Jobify - Job Listing Platform

A full-stack job listing platform built with:

- **Frontend:** React + Vite (`job-listing-frontend`)
- **Backend:** Django + Django REST Framework (`job_platform`)
- **Database:** SQLite (local dev)

This project shows job listings from a Django API in a React UI.

---

## Features

### Working now
- Fetch and display job listings on the frontend
- Backend API to list jobs (`GET /api/jobs/`)
- Backend API to create jobs (`POST /api/jobs/post/`) *(requires authenticated employer)*
- Backend API to submit applications (`POST /api/jobs/<id>/apply/`)
- Django admin setup for managing models

### Current limitations
- Frontend **Apply** button currently shows an alert only (does not call backend apply API)
- No frontend UI for posting jobs
- Minimal test coverage (placeholder tests only)

---

## Project Structure

```text
Final-Project/
├─ job-listing-frontend/     # React + Vite frontend
│  ├─ src/
│  ├─ package.json
│  └─ ...
└─ job_platform/             # Django backend
   ├─ jobs/                  # app: models, serializers, views
   ├─ job_platform/          # settings, urls, wsgi/asgi
   ├─ manage.py
   └─ requirements.txt
