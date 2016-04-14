#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import api
from django.conf.urls import url, include

from django.conf.urls import url
from views import UserControl


urlpatterns = [
        url(r'^usercontrol/(?P<slug>\w+)$', UserControl.as_view()),
]

urlpatterns += [
    url(r'^api/account/', include(api.router.urls)),
]