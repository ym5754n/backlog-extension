from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

# 未ログインでアクセス可能なページリスト
guest_path = ['/login/', '/signup/']

class authMiddleware(MiddlewareMixin):
    """guestユーザがgeest_pathで指定した以外のページにアクセスした場合loginにリダイレクトする"""
    def process_response(self, request, response):
        if not request.user.is_authenticated and request.path not in guest_path:
            return HttpResponseRedirect('/login/')
        return response