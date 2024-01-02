from django.test import TestCase
from django.urls import reverse, resolve
from ..views import IndexView, IssueListView

class TestUrls(TestCase):

  """index ページへのURLでアクセスする時のリダイレクトをテスト"""
  def test_index_url(self):
    view = resolve('/backlogext/')
    self.assertEqual(view.func.view_class, IndexView)

  """Issue 一覧ページへのリダイレクトをテスト"""
  def test_issue_list_url(self):
    view = resolve('/backlogext/issue_list')
    self.assertEqual(view.func.view_class, IssueListView)