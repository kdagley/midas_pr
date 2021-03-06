from django.db import models
import datetime
from django.db.models import Q


def nostakeholder():
    return Q(name__exact='None') & Q(stakeholder_group__group_name__exact='Unknown')


def midas_group_query():
    return Q(stakeholder_group__group_name__startswith='Midas Gold') | nostakeholder()


def allowed():
    return Q(allow_data_exchange=True) | nostakeholder()


class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True, default='Unknown')

    def __unicode__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'categories'


class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=200, default='None')
    category = models.ForeignKey(Category, default=1, null=True)

    def __unicode__(self):
        return str(self.category) + ' - ' + self.subcategory_name

    class Meta:
        verbose_name_plural = 'subcategories'


class StakeholderGroup(models.Model):
    group_name = models.CharField(max_length=200, unique=True, default='Unknown')
    allow_data_exchange = models.BooleanField(default=False)
    primary_contact = models.ForeignKey('Stakeholder',
                                        limit_choices_to=allowed,
                                        null=True)

    def __unicode__(self):
        return self.group_name

    class Meta:
        verbose_name = 'organization'


class CommunicationPreference(models.Model):
    preference_name = models.CharField(max_length=200, unique=True, default='None')

    def __unicode__(self):
        return self.preference_name


class MidasOffice(models.Model):
    office_name = models.CharField(max_length=200, unique=True, default='None')

    def __unicode__(self):
        return self.office_name


# nostakeholder = Q(name__exact='None') & Q(stakeholder_group__group_name__exact='Unknown')
# midas_group_query = Q(stakeholder_group__group_name__startswith='Midas Gold') | nostakeholder
# nostakeholder = 1
# midas_group_query = {'stakeholder_group__group_name__startswith': 'Midas Gold'}
class Stakeholder(models.Model):
    nostakeholder = 1439
    created_at = models.DateTimeField(auto_now_add=True)
    subcategory = models.ForeignKey(SubCategory, null=True)
    name = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    spouse = models.CharField(max_length=200, blank=True)
    stakeholder_group = models.ForeignKey(StakeholderGroup, verbose_name='organization', null=True)
    communication_preference = models.ForeignKey(CommunicationPreference, null=True)
    midas_office = models.ForeignKey(MidasOffice, null=True)
    manage_approvals = models.BooleanField(default=False)
    title = models.CharField(max_length=200, blank=True)
    phone_work = models.CharField(max_length=200, blank=True)
    phone_mobile = models.CharField(max_length=200, blank=True)
    phone_fax = models.CharField(max_length=200, blank=True)
    phone_home = models.CharField(max_length=200, blank=True)
    email_work = models.EmailField(blank=True)
    email_home = models.EmailField(blank=True)
    url = models.URLField(blank=True)
    work_address1 = models.CharField(max_length=200, blank=True)
    work_address2 = models.CharField(max_length=200, blank=True)
    work_address_city = models.CharField(max_length=200, blank=True)
    work_address_state = models.CharField(max_length=200, blank=True)
    work_address_zip = models.CharField(max_length=200, blank=True)
    work_address_country = models.CharField(max_length=200, blank=True)
    home_address1 = models.CharField(max_length=200, blank=True)
    home_address_city = models.CharField(max_length=200, blank=True)
    home_address_state = models.CharField(max_length=200, blank=True)
    home_address_zip = models.CharField(max_length=200, blank=True)
    home_address_country = models.CharField(max_length=200, blank=True)
    stakeholder_notes = models.TextField(blank=True)
    allow_data_exchange = models.BooleanField(default=False)
    christmas_card = models.BooleanField(default=False)
    card_sender = models.ForeignKey('self', default=nostakeholder, limit_choices_to=midas_group_query, null=True)
    lf_open_house_2012 = models.BooleanField(default=False)
    ea1_comment = models.BooleanField(default=False)
    ea1_positive = models.NullBooleanField()
    ea1_topic_1 = models.CharField(max_length=200, blank=True)
    ea1_topic_2 = models.CharField(max_length=200, blank=True)
    ea1_topic_3 = models.CharField(max_length=200, blank=True)
    ea1_format = models.CharField(max_length=200, blank=True)
    ea2_email = models.BooleanField(default=False)
    ea2_letter = models.BooleanField(default=False)
    ea2_rp = models.CharField(max_length=200, blank=True)
    ea2_comment = models.BooleanField(default=False)
    ea2_positive = models.NullBooleanField()
    ea2_topic_1 = models.CharField(max_length=200, blank=True)
    ea2_topic_2 = models.CharField(max_length=200, blank=True)
    ea2_topic_3 = models.CharField(max_length=200, blank=True)
    ea2_format = models.CharField(max_length=200, blank=True)
    ea3_outreach = models.BooleanField(default=False)
    ea3_rp = models.CharField(max_length=200, blank=True)
    contacted = models.BooleanField(default=False)
    ea3_email = models.BooleanField(default=False)
    ea3_letter = models.BooleanField(default=False)
    site_tour_date = models.DateField(default=datetime.date(2000, 1, 1))
    tour_group = models.CharField(max_length=200, blank=True)
    lf_open_house_2013 = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name + ' - ' + str(self.stakeholder_group)
