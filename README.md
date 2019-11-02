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
