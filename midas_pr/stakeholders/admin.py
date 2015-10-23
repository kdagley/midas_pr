from django.contrib import admin
from .models import Stakeholder, StakeholderGroup, Category, MidasOffice, CommunicationPreference

# Register your models here.


def make_invite(modeladmin, request, queryset):
    queryset.update(christmas_invite=True)
make_invite.short_description = "Invite selected stakeholders to Christmas Party"


class StakeholderAdmin(admin.ModelAdmin):
    list_display = ['name', 'stakeholder_group', 'christmas_invite']
    ordering = ['stakeholder_group', 'last_name']
    actions = [make_invite]


admin.site.register(Stakeholder, StakeholderAdmin)
admin.site.register(StakeholderGroup)
admin.site.register(Category)
admin.site.register(CommunicationPreference)
admin.site.register(MidasOffice)


# class MidasOfficeAdmin(admin.ModelAdmin):
#    list_display = ('office_name')
