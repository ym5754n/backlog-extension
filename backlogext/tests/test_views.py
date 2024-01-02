from django.test import TestCase
from django.urls import reverse

from ..models import Issue

class IndexTests(TestCase):
  """IndexViewのテストクラス"""

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('backlogext:index'))
    self.assertEqual(response.status_code, 200)

class IssueListTests(TestCase):

  def setUp(self):
    """
    テスト環境の準備用メソッド。名前は必ず「setUp」とすること。
    同じテストクラス内で共通で使いたいデータがある場合にここで作成する。
    """
    issue1 = Issue.objects.create(summary='summary1', description='description1')
    issue2 = Issue.objects.create(summary='summary2', description='description2')

  def test_get(self):
    """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    response = self.client.get(reverse('backlogext:issue_list'))
    self.assertEqual(response.status_code, 200)
  
  def test_get_2issues_by_list(self):
    """GET でアクセス時に、setUp メソッドで追加した 2件追加が返されることを確認"""
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
      """
      setUp で追加したデータを消す、掃除用メソッド。
      create とはなっているがメソッド名を「tearDown」とすることで setUp と逆の処理を行ってくれる＝消してくれる。
      """
      issue1 = Issue.objects.create(summary='summary1', description='description1')
      issue2 = Issue.objects.create(summary='summary2', description='description2')