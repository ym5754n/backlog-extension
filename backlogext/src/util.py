from ..models import Setting, Token

class Util:
    def __init__(self, user):
        self.setting = Setting.objects.get(user=user)
        self.token = Token.objects.get(user=user)
        self.base_url = f'https://{self.setting.space_key}.{self.setting.domain}/api/v2/'    

    def get_headers(self):
        """APIリクエストに必要なヘッダーを取得する"""
        return {
            'Authorization': 'Bearer {}'.format(self.token.access_token)
        }

    def get_authentication_code_url(self):
        """認可コードを取得するURLを返却する"""
        return f'https://{self.setting.space_key}.{self.setting.domain}/OAuth2AccessRequest.action?response_type=code&client_id={self.setting.client_id}&redirect_uri=http://localhost:8000/authenticate_success'