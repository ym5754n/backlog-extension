from django.test import TestCase
from django.urls import reverse, resolve
from ..views import IssueListView

class TestUrls(TestCase):
  """Issue 一覧ページへのリダイレクトをテスト"""
  def test_issue_list_url(self):
    view = resolve('/backlogext/issue_list')
    self.assertEqual(view.func.view_class, IssueListView)