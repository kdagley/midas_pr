from django.contrib import admin
from .models import ApprovalTracking, Report, Category
from import_export import resources
from import_export.admin import ImportExportMixin


class ReportResource(resources.ModelResource):

    class Meta:
        model = Report
        fields = ('id', 'document_data_name', 'document_data_type', 'mg_employee_assigned',
                  'mg_employee_assigned__name', 'third_party_organization', 'third_party_organization__group_name',
                  'third_party_name', 'third_party_name__name', 'date_sent_received',
                  'category', 'category__name', 'purpose', 'approved', 'description', 'response_required',
                  'response_due_date', 'comments', 'data_saved_as', 'attachments',)


class ApprovalTrackingResource(resources.ModelResource):

    class Meta:
        model = ApprovalTracking
        fields = ('id', 'document_data_name', 'from_1', 'from_1__name', 'to', 'cc',
                  'date', 'purpose_of_data_exchange',
                  'third_party_organization_to_receive_data', 'third_party_organization_to_receive_data__group_name',
                  'third_party_requested_to_receive_data', 'third_party_requested_to_receive_data__name',
                  'datasets', 'approved', 'approved_by',)


def data_approved(modeladmin, request, queryset):
    queryset.update(approved=True)
data_approved.short_description = "Approve selected for Data Exchange"


class ApprovalTrackingAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ApprovalTrackingResource
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


class ReportAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ReportResource
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
