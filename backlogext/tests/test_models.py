from django.test import TestCase
from backlogext.models import Issue

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