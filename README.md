# bot

## Flask app 起動手順
```bash
pip install pipenv
(or you'll do "pip3 install pipenv")

pipenv install --dev
(if you'll occur error, do "pipenv install --python=<your/python/path>")

pipenv run flask run --host=0.0.0.0 --port=10090
```

## API確認手順
```bash
curl http://localhost:10090/hello/
```
