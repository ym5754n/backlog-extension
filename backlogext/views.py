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

class IssueDetailView(generic.DetailView):
    template_name = 'backlogext/issue_detail.html'
    model = Issue
    
class IssueUpdateView(generic.UpdateView):
    template_name = 'backlogext/issue_form.html'
    model = Issue
    form_class = IssueCreateForm
    success_url = reverse_lazy('backlogext:issue_list')

class IssueDeleteView(generic.DeleteView):
    template_name = 'backlogext/issue_confirm_delete.html'
    model = Issue
    success_url = reverse_lazy('backlogext:issue_list')