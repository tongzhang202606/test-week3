from google.cloud import storage
from datetime import datetime
import os

# 環境変数からバケット名取得（コード内直書き禁止・本番規約）
BUCKET_NAME = os.environ.get("my-batch-storage-0712")

def main():
    # 現在日時を指定フォーマットに整形
    now_time = datetime.now()
    file_name = now_time.strftime("batch_%Y%m%d_%H%M%S")

    # GCS接続・ファイルアップロード
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file_name)
    blob.upload_from_string("Batch Auto Run Success | GCS File Generate OK")

    print(f"Success! Upload File: {file_name}")

if __name__ == "__main__":
    main()
