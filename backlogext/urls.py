from django.urls import path
from . import views

app_name = 'backlogext'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('issue_list', views.IssueListView.as_view(), name='issue_list'),
    path('issue_create', views.IssueCreateView.as_view(), name='issue_create'),
    path('issue_detail/<int:pk>/', views.IssueDetailView.as_view(), name='issue_detail'),
    path('issue_update/<int:pk>/', views.IssueUpdateView.as_view(), name='issue_update'),
    path('issue_delete/<int:pk>/', views.IssueDeleteView.as_view(), name='issue_delete'),
]