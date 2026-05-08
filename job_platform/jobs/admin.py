from django.contrib import admin
from .models import Employer, Job, Application

admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(Application)

admin.site.site_header = "Jobify Admin Panel"
admin.site.site_title = "Jobify Admin"
admin.site.index_title = "Welcome to Jobify Admin"
