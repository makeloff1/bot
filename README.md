# bot

## git,docker,docker-composeのインストール
```bash
sudo yum install -y git
# docker、docker-composeに関しては以下を参考にする
https://qiita.com/subretu/items/549bc720165004bca3c3
```

## git repository
```bash
git clone https://github.com/makeloff1/bot.git
cd bot
```

## Flask app 起動手順
```bash
# pipenvをインストールしていない場合
pip install pipenv
(or you'll do "pip3 install pipenv")

# pipenvをインストールした後はここから
pipenv install --dev
(if you'll occur error, do "pipenv install --python=<your/python/path>")

# flask app起動
pipenv run flask run --host=0.0.0.0 --port=10090
```

## API確認手順
```bash
curl http://localhost:10090/hello/
```

## これが終わった後の段階的な練習（これが全部できたら、NTTPCの開発にも参加可能）
- Slack連携(Bot作成)
  - https://api.slack.com/apps
- Postgresql or Mysql(MariaDB)と連携してみる
  - docker-compose で立てると一瞬なため、コンテナで立てる
  - Flask-SQLAlchemy
  - Flask-Migrate
- Docker, docker-compose
  - すべてをコンテナ化する、起動順序など気を付ける
  - コンテナ間連携にはネットワークの知識が多少必要（Port-forwarding）
  - （超発展のため、今回は不要）前段にgunicorn, nginxを配置する
- Slackに自分で面白い機能を探してみる
  - ログイン機能、API利用可能ユーザ管理機能
  - Google APIとの連携（google console）
- その他　単語として最近の流行り（開発のいろんな分野）
　- テスト自動化 jenkins, seleniumなど
  - git(source treeやgit krakenなど)
  - 機械学習
  - GUI（React,typescript）
