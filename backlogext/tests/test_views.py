from django.test import TestCase
from django.urls import reverse

from backlogext.models import Issue, Setting
from django.contrib.auth import get_user_model

User = get_user_model()

class IssueListTests(TestCase):
  """IssueListビューのテストクラス"""

  def setUp(self):
    self.user = User.objects.create(username='test_user', password='1234')

    issue1 = Issue.objects.create(summary='summary1', description='description1', user=self.user)
    issue2 = Issue.objects.create(summary='summary2', description='description2', user=self.user)

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    self.client.force_login(self.user)
    response = self.client.get(reverse('backlogext:issue_list'))
    self.assertEqual(response.status_code, 200)
  
  def test_get_2issues_by_list(self):
    """GET でアクセス時に、setUp メソッドで追加した 2件追加が返されることを確認"""
    self.client.force_login(self.user)
    response = self.client.get(reverse('backlogext:issue_list'))
    self.assertEqual(response.status_code, 200)
    self.assertQuerysetEqual(
      # Issueモデルでは __str__ の結果として件名を返す設定なので、返される件名が投稿通りになっているかを確認
      response.context['issue_list'],
      ['<Issue: summary1>', '<Issue: summary2>'],
      ordered = False # 順序は無視するよう指定
    )
    self.assertContains(response, 'summary1') # html 内に issue1 の summary が含まれていることを確認
    self.assertContains(response, 'summary2') # html 内に issue2 の summary が含まれていることを確認

  def tearDown(self):
      issue1 = Issue.objects.create(summary='summary1', description='description1')
      issue2 = Issue.objects.create(summary='summary2', description='description2')

class IssueCreateTests(TestCase):
    """IssueCreateビューのテストクラス"""

    def setUp(self):
        self.user = User.objects.create(username='test_user', password='1234')

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('backlogext:issue_create'))
        self.assertEqual(response.status_code, 200)

    def test_post_with_data(self):
        """適当なデータでPOSTすると、成功してリダイレクトされることを確認"""
        self.client.force_login(self.user)
        data = {
            'summary': 'test_summary',
            'description': 'test_description',
        }
        response = self.client.post(reverse('backlogext:issue_create'), data=data)
        self.assertEqual(response.status_code, 302)
    
    def test_issue_null(self):
        """空のデータで POST を行うとリダイレクトも無く 200 だけ返されることを確認"""
        self.client.force_login(self.user)
        data = {}
        response = self.client.post(reverse('backlogext:issue_create'), data=data)
        self.assertEqual(response.status_code, 200)

class IssueDetailTests(TestCase):
    """IssueDetailView のテストクラス"""

    def setUp(self):
        self.user = User.objects.create(username='test_user', password='1234')

    def test_not_fount_pk_get(self):
        """課題を登録せず、空の状態で存在しない課題のプライマリキーでアクセスした時に 404 が返されることを確認"""
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('backlogext:issue_detail', kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        self.client.force_login(self.user)
        issue = Issue.objects.create(summary='test_summary', description='test_description')
        response = self.client.get(
            reverse('backlogext:issue_detail', kwargs={'pk': issue.pk}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, issue.summary)
        self.assertContains(response, issue.description)

class IssueUpdateTests(TestCase):
    """IssueUpdateView のテストクラス"""

    def setUp(self):
        self.user = User.objects.create(username='test_user', password='1234')

    def test_not_fount_pk_get(self):
        """課題を登録せず、空の状態で存在しない課題のプライマリキーでアクセスした時に 404 が返されることを確認"""
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('backlogext:issue_update', kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        self.client.force_login(self.user)
        issue = Issue.objects.create(summary='test_summary', description='test_description')
        response = self.client.get(
            reverse('backlogext:issue_update', kwargs={'pk': issue.pk}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, issue.summary)
        self.assertContains(response, issue.description)

class IssueDeleteTests(TestCase):
    """IssueDeleteView のテストクラス"""

    def setUp(self):
        self.user = User.objects.create(username='test_user', password='1234')

    def test_not_fount_pk_get(self):
        """課題を登録せず、空の状態で存在しない課題のプライマリキーでアクセスした時に 404 が返されることを確認"""
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('backlogext:issue_delete', kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        self.client.force_login(self.user)
        issue = Issue.objects.create(summary='test_summary', description='test_description')
        response = self.client.get(
            reverse('backlogext:issue_delete', kwargs={'pk': issue.pk}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, issue.summary)
        self.assertContains(response, issue.description)

class SettingCreateTests(TestCase):
    """SettingCreate のテストクラス"""

    def setUp(self):
        self.user = User.objects.create(username='test_user', password='1234')

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('backlogext:setting_create'))
        self.assertEqual(response.status_code, 200)
    
    def test_issue_null(self):
        """空のデータで POST を行うとリダイレクトも無く 200 だけ返されることを確認"""
        self.client.force_login(self.user)
        data = {}
        response = self.client.post(reverse('backlogext:setting_create'), data=data)
        self.assertEqual(response.status_code, 200)

class SettingUpdateTests(TestCase):
    """SettingUpdateView のテストクラス"""

    def setUp(self):
        self.user = User.objects.create(username='test_user', password='1234')

    def test_not_fount_pk_get(self):
        """課題を登録せず、空の状態で存在しない課題のプライマリキーでアクセスした時に 404 が返されることを確認"""
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('backlogext:setting_update', kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        self.client.force_login(self.user)
        setting = Setting.objects.create(space_key='test_space_key', project_key='test_project_key')
        response = self.client.get(
            reverse('backlogext:setting_update', kwargs={'pk': setting.pk}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, setting.space_key)
        self.assertContains(response, setting.project_key)