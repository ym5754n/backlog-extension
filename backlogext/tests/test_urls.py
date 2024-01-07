from django.test import TestCase
from django.urls import reverse, resolve
from backlogext.views.issue import IssueListView, IssueCreateView, IssueDetailView, IssueUpdateView, IssueDeleteView
from backlogext.views.auth import Signup, Login, Logout
from backlogext.views.api import create_issue, authenticate_success
from backlogext.views.setting import SettingCreateView, SettingUpdateView

class TestUrls(TestCase):
  def test_signup_url(self):
      url = reverse('backlogext:signup')
      self.assertEqual(resolve(url).func.view_class, Signup)

  def test_login_url(self):
      url = reverse('backlogext:login')
      self.assertEqual(resolve(url).func.view_class, Login)

  def test_logout_url(self):
      url = reverse('backlogext:logout')
      self.assertEqual(resolve(url).func.view_class, Logout)

  def test_issue_list_url(self):
      url = reverse('backlogext:issue_list')
      self.assertEqual(resolve(url).func.view_class, IssueListView)

  def test_issue_create_url(self):
      url = reverse('backlogext:issue_create')
      self.assertEqual(resolve(url).func.view_class, IssueCreateView)
  
  def test_issue_detail_url(self):
     url = reverse('backlogext:issue_detail', kwargs={'pk': 1})
     self.assertEqual(resolve(url).func.view_class, IssueDetailView)

  def test_issue_update_url(self):
     url = reverse('backlogext:issue_update', kwargs={'pk': 1})
     self.assertEqual(resolve(url).func.view_class, IssueUpdateView)

  def test_issue_delete_url(self):
     url = reverse('backlogext:issue_delete', kwargs={'pk': 1})
     self.assertEqual(resolve(url).func.view_class, IssueDeleteView)

  def test_create_issue_url(self):
     url = reverse('backlogext:create_issue')
     self.assertEqual(resolve(url).func, create_issue)

  def test_authenticate_success_url(self):
     url = reverse('backlogext:authenticate_success')
     self.assertEqual(resolve(url).func, authenticate_success)

  def test_setting_create_url(self):
     url = reverse('backlogext:setting_create')
     self.assertEqual(resolve(url).func.view_class, SettingCreateView)
  
  def test_setting_update_url(self):
     url = reverse('backlogext:setting_update', kwargs={'pk': 1})
     self.assertEqual(resolve(url).func.view_class, SettingUpdateView)