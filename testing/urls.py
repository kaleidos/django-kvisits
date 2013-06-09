# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url, include
from kvisits.tests.views import view_test_object

urlpatterns = patterns('',
    url('^visit/(?P<id>\d+)/$', view_test_object, name='visit')
)
