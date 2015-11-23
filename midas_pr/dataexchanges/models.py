from django.db import models
from ..stakeholders.models import Stakeholder, StakeholderGroup, nostakeholder, midas_group_query, allowed
import datetime
from django.db.models import Q
from django.utils import timezone


class Category(models.Model):
    index = models.IntegerField(default=0)
    name = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return str(self.index) + " " + self.name

    class Meta:
        verbose_name_plural = 'categories'


# allowed = {'allow_data_exchange': True}
def allowed_group():
    return Q(allow_data_exchange=True) | Q(group_name='Unknown')


def manager():
    return Q(manage_approvals=True) | nostakeholder()


class ApprovalTracking(models.Model):
    nostakeholder = 1439
    document_data_name = models.CharField(max_length=200)
    from_1 = models.ForeignKey(Stakeholder, related_name='from_1',
                               limit_choices_to=midas_group_query)
    to = models.ManyToManyField(Stakeholder, related_name='to', limit_choices_to=midas_group_query)
    cc = models.ManyToManyField(Stakeholder, related_name='cc', limit_choices_to=midas_group_query)
    date = models.DateField(default=timezone.now)
    purpose_of_data_exchange = models.CharField(max_length=200)
    third_party_organization_to_receive_data = models.ForeignKey(
        StakeholderGroup, limit_choices_to=allowed_group)
    third_party_requested_to_receive_data = models.ForeignKey(
        Stakeholder, related_name='third_party_requested_to_receive_data',
        default=nostakeholder, limit_choices_to=allowed)
    datasets = models.TextField(blank=True)
    approved = models.NullBooleanField()
    approved_by = models.ManyToManyField(Stakeholder, related_name='approved_by', limit_choices_to=manager)

    def __unicode__(self):
        return self.document_data_name


def duedate():
    return timezone.now() + datetime.timedelta(30)


class Report(models.Model):
    nostakeholder = 1439
    document_data_name = models.CharField(max_length=200)
    document_data_type = models.CharField(max_length=200, blank=True)
    mg_employee_assigned = models.ForeignKey(Stakeholder, related_name='mg_employee_assigned',
                                             limit_choices_to=midas_group_query, default=nostakeholder)
    third_party_organization = models.ForeignKey(StakeholderGroup, limit_choices_to=allowed_group)
    third_party_name = models.ForeignKey(Stakeholder, default=nostakeholder, limit_choices_to=allowed)
    date_sent_received = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, default=1)
    purpose = models.CharField(max_length=200, blank=True)
    approved = models.NullBooleanField()
    description = models.CharField(max_length=200, blank=True)
    response_required = models.BooleanField(default=False)
    response_due_date = models.DateField(default=duedate)
    comments = models.TextField(blank=True)
    data_saved_as = models.TextField(blank=True)
    attachments = models.FileField(upload_to='attachments', max_length=100, blank=True)

    def __unicode__(self):
        return self.document_data_name
