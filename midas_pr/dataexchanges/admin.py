from django.contrib import admin
from .models import ApprovalTracking, Report, Category


def data_approved(modeladmin, request, queryset):
    queryset.update(approved=True)
data_approved.short_description = "Approve selected for Data Exchange"


class ApprovalTrackingAdmin(admin.ModelAdmin):
    search_fields = ['document_data_name', 'third_party_organization_to_receive_data__group_name']
    list_display = ['document_data_name',
                    'from_1',
                    'third_party_organization_to_receive_data',
                    'approved']
    list_filter = ['approved',
                   'approved_by']
    ordering = ['document_data_name']
    actions = [data_approved]


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['index', 'name']
    ordering = ['index']


class ReportAdmin(admin.ModelAdmin):
    search_fields = ['document_data_name',
                     'mg_employee_assigned__name',
                     'third_party_organization__group_name']
    list_display = ['document_data_name',
                    'mg_employee_assigned',
                    'third_party_organization',
                    'date_sent_received',
                    'category',
                    'approved',
                    'response_required',
                    'attachments']
    list_filter = ['mg_employee_assigned',
                   'third_party_organization',
                   'category',
                   'approved',
                   'response_required']
    ordering = ['document_data_name']


# Register your models here.
admin.site.register(ApprovalTracking, ApprovalTrackingAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Category, CategoryAdmin)
