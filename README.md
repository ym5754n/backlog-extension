# Backlog Extensiton
Backlog APIを使用してメモしておいた内容をbacklogに追加できるWEBアプリケーション

## Features
- ユーザーの認証機能
  - ID/Passwordによる会員登録
  - ID/Passwordによるログイン/ログアウト
  - 認可されたユーザ以外はサービス利用不可
- 課題
  - 課題の追加/編集/削除
  - 課題の一覧表示/詳細表示
- Backlog連携
  - Backlog連携に必要な設定の保存
  - 作成した課題をBacklogに追加
 
## Environment
- Docker Desktop (4.24.0)
- Django (3.2.23)
  - Python (3.12.1)
  - SQLite3 (3.40.1)

## Usage
※事前に[こちら](https://docs.docker.jp/get-docker.html)を参照してDockerを導入してください。

ローカル環境で動作を確認する場合は下記の手順でアプリを起動し、[localhost:8000](localhost:8000)にアクセスしてください。
```
# Clone this repository
$ git clone nulab-exam@nulab-exam.git.backlog.jp:/YAMASHITA/app.git

# Go into the repository
$ cd app

# Run the app
$ docker-compose up
$ docker exec -it app-web-1 sh
$ python manage.py migrate
```

## Author
- 作成者: ym5754n
- E-mail: ym5754n@gmail.com
