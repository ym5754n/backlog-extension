from django.urls import path
from . import views

app_name = 'backlogext'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('issue_list', views.IssueListView.as_view(), name='issue_list'),
    path('issue_create', views.IssueCreateView.as_view(), name='issue_create'),
]