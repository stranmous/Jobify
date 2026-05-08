from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Job, Application, Employer
from .serializers import JobSerializer, ApplicationSerializer

# Create your views here.

# View to list all available jobs (for everyone)
class JobList(generics.ListAPIView):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

# View for authenticated employers to post a new job
class JobCreate(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the logged-in employer
        employer = Employer.objects.get(user=self.request.user)
        serializer.save(posted_by=employer)

# View for anyone to apply for a specific job
class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Automatically link the application to the job from the URL
        job_id = self.kwargs.get('id')
        job = Job.objects.get(id=job_id)
        serializer.save(job=job)
