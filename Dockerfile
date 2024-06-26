FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# ポート公開
EXPOSE 5000

# アプリケーションのエントリーポイントを指定
CMD ["flask", "run", "--host=0.0.0.0"]

