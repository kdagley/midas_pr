# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import MessageForm, ApprovalTrackingForm, ReportForm
from django.http import HttpResponse
from .models import ApprovalTracking, Report


def index(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'dataexchanges/index.html', {'form': MessageForm()})


def aplist(request):
    approval_list = ApprovalTracking.objects.order_by('-date')
    context = {'approval_list': approval_list}
    return render(request, 'dataexchanges/approvallist.html', context)


def detail(request, approval_tracking_id):
    return render(
        request,
        'dataexchanges/index.html',
        {'form': ApprovalTrackingForm(instance=ApprovalTracking.objects.get(pk=approval_tracking_id))})
    #  {'form': MessageForm(), 'approval_tracking_id': approval_tracking_id})
    # return HttpResponse("You're looking at approval_tracking %s." % approval_tracking_id)


def reportlist(request):
    report_list = Report.objects.order_by('-date_sent_received')
    context = {'report_list': report_list}
    return render(request, 'dataexchanges/reportlist.html', context)


def report_detail(request, report_id):
    return render(
        request,
        'dataexchanges/index.html',
        {'form': ReportForm(instance=Report.objects.get(pk=report_id))})


def results(request, approval_tracking_id):
    response = "You're looking at the results of approval_tracking %s."
    return HttpResponse(response % approval_tracking_id)


def vote(request, approval_tracking_id):
    return HttpResponse("You're voting on approval_tracking %s." % approval_tracking_id)
