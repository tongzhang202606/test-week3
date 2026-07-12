from google.cloud import storage
from datetime import datetime
import os

# 環境変数からバケット名取得（ハードコード廃止・本番規約）
BUCKET_NAME = os.environ.get("GCS_BUCKET_NAME")

def main():
    # 現在日時取得 → batch_yyyymmdd_hhmmss
    now_time = datetime.now()
    file_name = now_time.strftime("batch_%Y%m%d_%H%M%S")

    # GCSアップロード処理
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file_name)
    blob.upload_from_string("Batch Auto Run Success")

    print(f"File uploaded: {file_name}")

if __name__ == "__main__":
    main()