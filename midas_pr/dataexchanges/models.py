from django.db import models
from ..stakeholders.models import Stakeholder
import datetime
# from django.db.models import Q
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    index = models.IntegerField(default=0)
    name = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return str(self.index) + " " + self.name

    class Meta:
        verbose_name_plural = 'categories'


# nostakeholder = Q(name__exact='None') & Q(stakeholder_group__group_name__exact='Unknown')
# midas_group_query = Q(stakeholder_group__group_name__startswith='Midas Gold') | nostakeholder
# allowed = Q(allow_data_exchange=True) | nostakeholder
nostakeholder = 1
midas_group_query = {'stakeholder_group__group_name__startswith': 'Midas Gold'}
allowed = {'allow_data_exchange': True}


class ApprovalTracking(models.Model):
    document_data_name = models.CharField(max_length=200, blank=True)
    from_1 = models.ForeignKey(Stakeholder, related_name='from_1', default=nostakeholder,
                               limit_choices_to=midas_group_query)
    to = models.ForeignKey(Stakeholder, related_name='to', default=nostakeholder, limit_choices_to=midas_group_query)
    cc = models.ForeignKey(Stakeholder, related_name='cc', default=nostakeholder, limit_choices_to=midas_group_query)
    date = models.DateField(default=timezone.now)
    purpose_of_data_exchange = models.CharField(max_length=200, blank=True)
    third_party_requested_to_receive_data = models.ForeignKey(
        Stakeholder, related_name='third_party_requested_to_receive_data',
        default=nostakeholder, limit_choices_to=allowed)
    datasets = models.TextField(blank=True)
    approved = models.NullBooleanField()
    approved_by = models.ForeignKey(Stakeholder, related_name='approved_by',
                                    limit_choices_to=midas_group_query, default=nostakeholder)
    approved_by_2 = models.ForeignKey(Stakeholder, related_name='approved_by_2',
                                      limit_choices_to=midas_group_query, default=nostakeholder)
    field1 = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.document_data_name


def duedate():
    return timezone.now() + datetime.timedelta(30)


class Report(models.Model):
    document_data_name = models.CharField(max_length=200, blank=True)
    document_data_type = models.CharField(max_length=200, blank=True)
    mg_employee_assigned = models.ForeignKey(Stakeholder, related_name='mg_employee_assigned',
                                             limit_choices_to=midas_group_query, default=nostakeholder)
    third_party_name = models.ManyToManyField(Stakeholder, limit_choices_to={'allow_data_exchange': True})
    date_sent_received = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, null=True)
    purpose = models.CharField(max_length=200, blank=True)
    approved = models.NullBooleanField()
    description = models.CharField(max_length=200, blank=True)
    response_required = models.BooleanField(default=False)
    response_due_date = models.DateField(default=duedate)
    comments = models.TextField(blank=True)
    data_saved_as = models.TextField(blank=True)
    attachments = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.document_data_name
