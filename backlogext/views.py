from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Issue
from .forms import IssueCreateForm

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'backlogext/index.html'

class IssueListView(generic.ListView):
    template_name = 'backlogext/issue_list.html'
    model = Issue

class IssueCreateView(generic.CreateView):
    template_name = 'backlogext/issue_form.html'
    form_class = IssueCreateForm
    success_url = reverse_lazy('backlogext:issue_list')