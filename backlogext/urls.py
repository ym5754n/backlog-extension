from django.urls import path
from .views import auth, issue, api, setting

app_name = 'backlogext'

urlpatterns = [
    # guest user
    ## auth
    path('signup/', auth.Signup.as_view(), name='signup'),
    path('login/', auth.Login.as_view(), name='login'),

    # auth user
    ## auth
    path('logout/', auth.Logout.as_view(), name='logout'),
    ## issue
    path('issue_list', issue.IssueListView.as_view(), name='issue_list'),
    path('issue_create', issue.IssueCreateView.as_view(), name='issue_create'),
    path('issue_detail/<int:pk>/', issue.IssueDetailView.as_view(), name='issue_detail'),
    path('issue_update/<int:pk>/', issue.IssueUpdateView.as_view(), name='issue_update'),
    path('issue_delete/<int:pk>/', issue.IssueDeleteView.as_view(), name='issue_delete'),
    ## api
    path('create_issue', api.create_issue, name='create_issue'),
    path('authenticate_success', api.authenticate_success, name='authenticate_success'),
    ## setting
    path('setting_create', setting.SettingCreateView.as_view(), name='setting_create'),
    path('setting_update/<int:pk>/', setting.SettingUpdateView.as_view(), name='setting_update'),
]