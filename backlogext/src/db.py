from ..models import Token, Issue, Setting

class Db:
    def __init__(self, user):
        self.user = user

    def update_token(self, data):
        """tokenを更新する"""
        token, created = Token.objects.get_or_create(user=self.user)
        token.access_token = data['access_token']
        token.expires_in = data['expires_in']
        token.refresh_token = data['refresh_token']
        token.save()

    def update_issue(self, data, pk):
        """issueを更新する"""
        issue = Issue.objects.get(pk=pk)
        issue.key_id = data['keyId']
        issue.save()

    def update_setting_code(self, code):
        """setting.codeを更新する"""
        try:
            setting = Setting.objects.get(user=self.user)
        except Setting.DoesNotExist:
            print('ERROR: Setting does not exist.')
        setting.code = code
        setting.save()