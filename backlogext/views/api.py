from django.shortcuts import redirect
from backlogext.models import Setting
from backlogext.src.api import Api
from backlogext.src.util import Util
from backlogext.src.db import Db
from django.contrib import messages


def authenticate_success(request):
    """oauth2の認可コード取得完了時の処理を行う"""

    api = Api(request.user)
    db = Db(request.user)

    db.update_setting_code(request.GET['code'])
    json_response = api.create_token(request.GET['code'])

    if 'errors' in json_response:
        messages.info(request, f'エラーが発生しました。時間をおいて再度実行してください。')
        return redirect('/issue_list')

    db.update_token(json_response)

    messages.info(request, f'backlogとの連携が完了しました。操作をやり直してください。')
    return redirect('/issue_list')

def create_issue(request):
    """課題をbacklogに追加する"""
    api = Api(request.user)
    util = Util(request.user)
    db = Db(request.user)
    
    # 認可コードが存在しない場合、認可コードを取得する
    setting = Setting.objects.get(user=request.user.id)
    if not setting.code:
        return redirect(util.get_authentication_code_url())

    # 課題追加をbacklogにリクエストする
    header = util.get_headers(request.user)
    body = {
        'projectId': request.POST['projectId'],
        'summary': request.POST['summary'],
        'issueTypeId': request.POST['issueTypeId'],
        'priorityId': request.POST['priorityId'],
    }
    json_response = api.create_issue(header, body)

    if 'errors' in json_response:
        messages.info(request, f'エラーが発生しました。時間をおいて再度実行してください。')
        return redirect('/issue_list')

    # 課題キーをセットする
    db.update_issue(json_response, request.POST['pk'])

    messages.info(request, f'backlogに課題を追加しました')
    return redirect('/issue_list')