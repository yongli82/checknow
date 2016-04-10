#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import api
from django.conf.urls import url, include



# urlpatterns = [
#     url(r'^page/userlist/$', page_views.UserListView.as_view(), name="user-list-page"),
# ]


urlpatterns = [
    url(r'^', include(api.router.urls)),
]