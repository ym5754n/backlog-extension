from django.test import TestCase
from backlogext.models import Issue, Token, Setting
from django.contrib.auth import get_user_model

user = get_user_model()

class IssueModelTest(TestCase):
    def test_is_empty(self):
        """初期状態では何も登録されていないことをチェック"""
        saved_issues = Issue.objects.all()
        self.assertEqual(saved_issues.count(), 0)
    
    def test_is_count_one(self):
        """1つレコードを適当に作成すると、レコードが1つだけカウントされることをテスト"""
        issue = Issue(summary='test_summary', description='test_description')
        issue.save()
        saved_issues = Issue.objects.all()
        self.assertEqual(saved_issues.count(), 1)

    def test_saving_and_retrieving_post(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
        issue = Issue()
        summary = 'test_summary_to_retrieve'
        description = 'test_description_to_retrieve'
        issue.summary = summary
        issue.description = description
        issue.save()

        saved_issues = Issue.objects.all()
        actual_issue = saved_issues[0]

        self.assertEqual(actual_issue.summary, summary)
        self.assertEqual(actual_issue.description, description)

class TokenModelTest(TestCase):
    def test_is_empty(self):
        """初期状態では何も登録されていないことをチェック"""
        saved_token = Token.objects.all()
        self.assertEqual(saved_token.count(), 0)
    
    def test_is_count_one(self):
        """1つレコードを適当に作成すると、レコードが1つだけカウントされることをテスト"""
        token = Token(access_token='test_access_token', refresh_token='test_refresh_token', expires_in=999)
        token.save()
        saved_token = Token.objects.all()
        self.assertEqual(saved_token.count(), 1)

    def test_saving_and_retrieving_post(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
        token = Token()
        access_token='test_access_token'
        refresh_token='test_refresh_token'
        expires_in=999
        token.access_token = access_token
        token.refresh_token = refresh_token
        token.expires_in = expires_in
        token.save()

        saved_token = Token.objects.all()
        actual_token = saved_token[0]

        self.assertEqual(actual_token.access_token, access_token)
        self.assertEqual(actual_token.refresh_token, refresh_token)
        self.assertEqual(actual_token.expires_in, expires_in)

class SettingModelTest(TestCase):
    def test_is_empty(self):
        """初期状態では何も登録されていないことをチェック"""
        saved_setting = Setting.objects.all()
        self.assertEqual(saved_setting.count(), 0)
    
    def test_is_count_one(self):
        """1つレコードを適当に作成すると、レコードが1つだけカウントされることをテスト"""
        setting = Setting(space_key='test_space_key', project_key='test_project_key', project_id=1, code='test_code', client_id='test_client_code', client_secret='test_client_secret')
        setting.save()
        saved_setting = Setting.objects.all()
        self.assertEqual(saved_setting.count(), 1)

    def test_saving_and_retrieving_post(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
        setting = Setting()
        space_key='test_space_key'
        project_key='test_project_key'
        project_id=1
        code='test_code'
        client_id='test_client_code'
        client_secret='test_client_secret'
        setting.space_key=space_key
        setting.project_key=project_key
        setting.project_id=project_id
        setting.code=code
        setting.client_id=client_id
        setting.client_secret=client_secret
        setting.save()

        saved_setting = Setting.objects.all()
        actual_setting = saved_setting[0]

        self.assertEqual(actual_setting.space_key, space_key)
        self.assertEqual(actual_setting.project_key, project_key)
        self.assertEqual(actual_setting.project_id, project_id)
        self.assertEqual(actual_setting.code, code)
        self.assertEqual(actual_setting.client_id, client_id)
        self.assertEqual(actual_setting.client_secret, client_secret)