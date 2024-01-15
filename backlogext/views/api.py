from django.shortcuts import redirect
from backlogext.models import Setting
from backlogext.src import db
from backlogext.src.api import Api
from backlogext.src.util import Util
from backlogext.src.db import Db
from django.contrib import messages


def authenticate_success(request):
    """oauth2の認可コード取得完了時の処理を行う"""

    api = Api(request.user)
    db = Db(request.user)

    db.update_setting_code(request.GET['code'])
    jsonData = api.create_token(request.GET['code'])
    db.update_token(jsonData)

    messages.info(request, f'backlogとの連携が完了しました。再度｢追加｣を実行してください')
    return redirect('/issue_list')

def create_issue(request):
    """課題をbacklogに追加する"""

    api = Api(request.user)
    util = Util(request.user)
    db = Db(request.user)

    try:
        setting = Setting.objects.get(user=request.user.id)
    except Setting.DoesNotExist:
        messages.info(request, f'はじめに｢設定｣から設定してください')
        return redirect('/issue_list')
    
    # 認可コードが存在しない場合、認可コードを取得する
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

    # tokenが有効期限切れの場合、tokenを再発行する
    if 'errors' in json_response and json_response['errors'][0]['code'] == 11:
        token = api.refresh_token()
        db.update_token(token)
        messages.info(request, f'再度実行してください')
        return redirect('/issue_list')

    # 課題キーをセットする
    db.update_issue(json_response, request.POST['pk'])

    messages.info(request, f'backlogに課題を追加しました')
    return redirect('/issue_list')