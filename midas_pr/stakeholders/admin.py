from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin
from .models import Stakeholder, StakeholderGroup, Category, SubCategory, MidasOffice, CommunicationPreference

# Register your models here.


class StakeholderResource(resources.ModelResource):

    class Meta:
        model = Stakeholder
        fields = ('card_sender__name', 'id', 'created_at', 'subcategory', 'subcategory__subcategory_name',
                  'subcategory__category__category_name', 'name', 'first_name', 'last_name', 'spouse',
                  'stakeholder_group', 'stakeholder_group__group_name', 'communication_preference',
                  'communication_preference__preference_name', 'midas_office', 'midas_office__office_name',
                  'manage_approvals', 'title', 'phone_work', 'phone_mobile', 'phone_fax', 'phone_home',
                  'email_work', 'email_home', 'url', 'work_address1', 'work_address2', 'work_address_city',
                  'work_address_state', 'work_address_zip', 'work_address_country', 'home_address1',
                  'home_address_city', 'home_address_state', 'home_address_zip', 'home_address_country',
                  'stakeholder_notes', 'allow_data_exchange', 'christmas_card', 'card_sender', 'lf_open_house_2012',
                  'ea1_comment', 'ea1_positive', 'ea1_topic_1', 'ea1_topic_2', 'ea1_topic_3', 'ea1_format',
                  'ea2_email', 'ea2_letter', 'ea2_rp', 'ea2_comment', 'ea2_positive', 'ea2_topic_1', 'ea2_topic_2',
                  'ea2_topic_3', 'ea2_format', 'ea3_outreach', 'ea3_rp', 'contacted', 'ea3_email', 'ea3_letter',
                  'site_tour_date', 'tour_group', 'lf_open_house_2013',)


class StakeholderGroupResource(resources.ModelResource):

    class Meta:
        model = StakeholderGroup
        fields = ('id', 'group_name', 'allow_data_exchange', 'primary_contact', 'primary_contact__name',)


def send_xmas(modeladmin, request, queryset):
    queryset.update(christmas_card=True)
send_xmas.short_description = "Send selected stakeholders a Christmas card"


def allow_xchange(modeladmin, request, queryset):
    queryset.update(allow_data_exchange=True)
allow_xchange.short_description = "Allow exchange of data with selected stakeholders"


def disallow_xchange(modeladmin, request, queryset):
    queryset.update(allow_data_exchange=False)
disallow_xchange.short_description = "Disallow exchange of data with selected stakeholders"


class StakeholderGroupAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = StakeholderGroupResource
    search_fields = ['group_name', 'primary_contact__name']
    list_display = ['group_name', 'primary_contact', 'allow_data_exchange']
    list_filter = ['allow_data_exchange']
    ordering = ['group_name']


class StakeholderAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = StakeholderResource
    search_fields = ['name', 'stakeholder_group__group_name']
    list_filter = ['subcategory__category__category_name',
                   'subcategory__subcategory_name',
                   'work_address_city',
                   'allow_data_exchange',
                   'manage_approvals',
                   'christmas_card']
    list_display = ['stakeholder_group',
                    'name',
                    'email_work',
                    'work_address_city',
                    'allow_data_exchange',
                    'manage_approvals',
                    'christmas_card',
                    'card_sender']
    ordering = ['stakeholder_group', 'last_name']
    actions = [allow_xchange, disallow_xchange, send_xmas]


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'subcategory_name']
    ordering = ['category__category_name', 'subcategory_name']

admin.site.register(Stakeholder, StakeholderAdmin)
admin.site.register(StakeholderGroup, StakeholderGroupAdmin)
admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(CommunicationPreference)
admin.site.register(MidasOffice)


# class MidasOfficeAdmin(admin.ModelAdmin):
#    list_display = ('office_name')
