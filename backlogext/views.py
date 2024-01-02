from django.shortcuts import render
from django.views import generic
from .models import Issue

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'backlogext/index.html'

class IssueListView(generic.ListView):
    template_name = 'backlogext/issue_list.html'
    model = Issue