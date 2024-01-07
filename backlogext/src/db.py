from ..models import Token, Issue, Setting

def update_token(data, user):
    """tokenを更新する"""
    token, created = Token.objects.get_or_create(user=user)
    token.access_token = data['access_token']
    token.expires_in = data['expires_in']
    token.refresh_token = data['refresh_token']
    token.save()

def update_issue(data, pk):
    """issueを更新する"""
    issue = Issue.objects.get(pk=pk)
    issue.key_id = data['keyId']
    issue.save()

def update_setting_code(code, user):
    """setting.codeを更新する"""
    try:
        setting = Setting.objects.get(user=user)
    except Setting.DoesNotExist:
        print('!!ERROR')
    setting.code = code
    setting.save()