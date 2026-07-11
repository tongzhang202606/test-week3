FROM python:3.11-slim

WORKDIR /app

# 依存ファイルコピー＆インストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 本体コードコピー
COPY main.py .

# Cloud Run Job実行コマンド
CMD ["python", "main.py"]
