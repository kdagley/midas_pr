# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the DataExchangeListView
    url(
        regex=r'^$',
        view=views.index,
        name='index'
    ),
    # ex: /polls/5/
    url(r'^aplist/$', views.aplist, name='aplist'),
    url(r'^reportlist/$', views.reportlist, name='reportlist'),
    # ex: /polls/5/
    url(r'^approval/(?P<approval_tracking_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^report/(?P<report_id>[0-9]+)/$', views.report_detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<approval_tracking_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<approval_tracking_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
