from django.shortcuts import render
from django.views.generic import TemplateView


class ShowMap(TemplateView):
    template_name = 'nizhnii/index.html'
