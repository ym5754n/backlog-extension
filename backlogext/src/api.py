import requests
from ..models import Setting, Token
from backlogext.src.db import Db

class Api:
    def __init__(self, user):
        self.user = user
        self.db = Db(self.user)
        self.setting = Setting.objects.get(user=user)
        self.base_url = f'https://{self.setting.space_key}.{self.setting.domain}/api/v2/'

    def post(self, url, data, headers=None):
        """POSTでAPIリクエストを実行する"""
        print('request POST url:',url, 'header:',headers, 'data:',data)
        r = requests.post(url, headers=headers, json=data)

        try:
            jsonData = r.json()
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e.response.text)
            # 認証エラーの場合、tokenを再発行する
            if 'errors' in jsonData and r.json()['errors'][0]['code'] == 11:
                token = self.refresh_token()
                self.db.update_token(token)
                header = {
                    'Authorization': 'Bearer {}'.format(token['access_token'])
                }
                print('request POST url:',url, 'header:',headers, 'data:',data)
                r = requests.post(url, headers=header, json=data)
                jsonData = r.json()

        print("response", jsonData)
        return jsonData
    
    def get(self, url, headers=None):
        """GETでAPIリクエストを実行する"""
        print("request GET url:",url, "header:",headers)
        r = requests.get(url, headers=headers)

        try:
            jsonData = r.json()
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e.response.text)
            # 認証エラーの場合、tokenを再発行する
            if 'errors' in jsonData and r.json()['errors'][0]['code'] == 11:
                token = self.refresh_token()
                self.db.update_token(token)
                header = {
                    'Authorization': 'Bearer {}'.format(token['access_token'])
                }
                print("request GET url:",url, "header:",header)
                r = requests.get(url, headers=header)
                jsonData = r.json()

        print("response", jsonData)
        return jsonData

    def create_issue(self, header, data):
        """課題の追加 /api/v2/issues"""
        url = self.base_url + 'issues'

        return self.post(url, data, header)

    def refresh_token(self):
        """アクセストークンの更新 /api/v2/oauth2/token"""
        url = self.base_url + 'oauth2/token'
        token = Token.objects.get(user=self.user)

        data = {
            'grant_type': 'refresh_token',
            'client_id': self.setting.client_id,
            'client_secret': self.setting.client_secret,
            'refresh_token': token.refresh_token,
        }

        return self.post(url, data)

    def create_token(self, code):
        """アクセストークンリクエスト /api/v2/oauth2/token"""
        url = self.base_url + 'oauth2/token'

        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://localhost:8000/authenticate_success',
            'client_id': self.setting.client_id,
            'client_secret': self.setting.client_secret,
        }

        return self.post(url, data)
    
    def get_issue_types(self, header):
        """プロジェクトに登録されている種別の一覧を取得する /api/v2/projects/:projectIdOrKey/issueTypes"""
        url = self.base_url + f'projects/{self.setting.project_id}/issueTypes'

        return self.get(url, header)