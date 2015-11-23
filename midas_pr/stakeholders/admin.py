from django.contrib import admin
from .models import Stakeholder, StakeholderGroup, Category, SubCategory, MidasOffice, CommunicationPreference

# Register your models here.


def send_xmas(modeladmin, request, queryset):
    queryset.update(christmas_card=True)
send_xmas.short_description = "Send selected stakeholders a Christmas card"


def allow_xchange(modeladmin, request, queryset):
    queryset.update(allow_data_exchange=True)
allow_xchange.short_description = "Allow exchange of data with selected stakeholders"


def disallow_xchange(modeladmin, request, queryset):
    queryset.update(allow_data_exchange=False)
disallow_xchange.short_description = "Disallow exchange of data with selected stakeholders"


class StakeholderGroupAdmin(admin.ModelAdmin):
    search_fields = ['group_name', 'primary_contact__name']
    list_display = ['group_name', 'primary_contact', 'allow_data_exchange']
    list_filter = ['allow_data_exchange']
    ordering = ['group_name']


class StakeholderAdmin(admin.ModelAdmin):
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
