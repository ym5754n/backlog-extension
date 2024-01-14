import requests
from ..models import Setting, Token

class BacklogApi:
    def __init__(self, user):
        self.setting = Setting.objects.get(user=user)
        self.token = Token.objects.get(user=user)
        self.base_url = f'https://{self.setting.space_key}.backlog.jp/api/v2/'

    def post(self, url, data, headers=None):
        """POSTでAPIリクエストを実行する"""
        r = requests.post(url, headers=headers, json=data)
        jsonData = r.json()

        print("response", jsonData)
        return jsonData

    def create_issue(self, header, data):
        """課題の追加 /api/v2/issues"""
        url = self.base_url + 'issues'

        print("request", data)
        return self.post(url, data, header)

    def refresh_token(self):
        """アクセストークンの更新 /api/v2/oauth2/token"""
        url = self.base_url + 'oauth2/token'

        data = {
            'grant_type': 'refresh_token',
            'client_id': self.setting.client_id,
            'client_secret': self.setting.client_secret,
            'refresh_token': self.token.refresh_token,
        }

        print("request", data)
        return self.post(url, data)

    def create_token(self):
        """アクセストークンリクエスト /api/v2/oauth2/token"""
        url = self.base_url + 'oauth2/token'

        data = {
            'grant_type': 'authorization_code',
            'code': self.setting.code,
            'redirect_uri': 'http://localhost:8000/authenticate_success',
            'client_id': self.setting.client_id,
            'client_secret': self.setting.client_secret,
        }

        print("request", data)
        return self.post(url, data)