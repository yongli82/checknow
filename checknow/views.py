#!/usr/bin/env python
# -*- coding:utf-8 -*-


from __future__ import unicode_literals

from django.views.generic import ListView, DetailView, View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect

class FrontendIndex(TemplateView):
    template_name = "frontend/index.html"

class BackendIndex(TemplateView):
    template_name = "backend/index.html"

class LoginView(TemplateView):
    template_name = "login.html"
