from django.contrib import admin
from .models import ApprovalTracking, Report, Category

# Register your models here.
admin.site.register(ApprovalTracking)
admin.site.register(Report)
admin.site.register(Category)
