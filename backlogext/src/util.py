from ..models import Token

def get_headers(user):
    """APIリクエストに必要なヘッダーを取得する"""
    token = Token.objects.get(user=user)

    return {
        'Authorization': 'Bearer {}'.format(token.access_token)
    }

def get_authentication_code_url(setting):
    """認可コードを取得するURLを返却する"""
    return f'https://{setting.space_key}.backlog.jp/OAuth2AccessRequest.action?response_type=code&client_id={setting.client_id}&redirect_uri=http://localhost:8000/authenticate_success'