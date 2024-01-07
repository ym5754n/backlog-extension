import requests
from ..models import Setting, Token
from . import util


def post(url, data, headers=None):
    """POSTでAPIリクエストを実行する"""
    r = requests.post(url, headers=headers, json=data)
    jsonData = r.json()

    print("response", jsonData)
    return jsonData

def create_issue(header, data):
    """課題の追加 /api/v2/issues"""
    url = 'https://nulab-exam.backlog.jp/api/v2/issues'

    print("request", data)
    return post(url, data, header)

def refresh_token(user):
    """アクセストークンの更新 /api/v2/oauth2/token"""
    url = 'https://nulab-exam.backlog.jp/api/v2/oauth2/token'
    setting = Setting.objects.get(user=user)
    token = Token.objects.get(user=user)

    data = {
        'grant_type': 'refresh_token',
        'client_id': setting.client_id,
        'client_secret': setting.client_secret,
        'refresh_token': token.refresh_token,
    }

    print("request", data)
    return post(url, data)

def create_token(user):
    """アクセストークンリクエスト /api/v2/oauth2/token"""
    url = 'https://nulab-exam.backlog.jp/api/v2/oauth2/token'
    setting = Setting.objects.get(user=user)

    data = {
        'grant_type': 'authorization_code',
        'code': setting.code,
        'redirect_uri': 'http://localhost:8000/authenticate_success',
        'client_id': setting.client_id,
        'client_secret': setting.client_secret,
    }

    print("request", data)
    return post(url, data)