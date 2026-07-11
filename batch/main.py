from google.cloud import storage
from datetime import datetime

# ========== 这里改成你自己的GCS存储桶名 ==========
BUCKET_NAME = "my-batch-storage-0712"
# ==============================================

def main():
    # 1. 获取当前系统时间，转换成 年月日_时分秒 格式
    now_time = datetime.now()
    file_name = now_time.strftime("batch_%Y%m%d_%H%M%S")

    # 2. 连接GCP云存储
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)

    # 3. 生成文件并上传（文件内写入执行成功提示）
    blob = bucket.blob(file_name)
    blob.upload_from_string("Batch 定时任务执行成功！")

    print(f"执行成功，已上传文件：{file_name}")

if __name__ == "__main__":
    main()
