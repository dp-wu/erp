import os
from pathlib import Path
from dotenv import load_dotenv
import sys

BASE_DIR = Path(__file__).resolve().parent

# 获取当前环境，默认 development
env_name = os.getenv("DJANGO_ENV", "development")
env_file = BASE_DIR / f".env.{env_name}"

if not env_file.exists():
    print(f"❌ Missing env file: {env_file}")
    sys.exit(1)

print(f"🔍 Loading environment: {env_file}")
load_dotenv(env_file)

# 必填项（按环境可扩展）
required_vars = [
    "DJANGO_SECRET_KEY",
    "DEBUG",
    "DB_NAME",
    "DB_USER",
    "DB_PASSWORD",
    "DB_HOST",
    "DB_PORT",
    "ALLOWED_HOSTS",
    "CSRF_TRUSTED_ORIGINS",
]

missing = [var for var in required_vars if not os.getenv(var)]

if missing:
    print(f"❌ Missing required variables: {', '.join(missing)}")
    sys.exit(1)

print("✅ All required env variables are set.")


# GPT 还建议：
# 可扩展
# 	•	你可以根据 DJANGO_ENV 动态调整必填项，比如 prod 环境下还要校验邮件服务、S3 配置。
# 	•	还可以加一个 默认值提醒：如果 SECRET_KEY 还是 dev-change-me 就报错。
# 要不要我帮你把 check_env.py 再升级一下，支持 根据环境自动切换不同的必填项（比如 dev 少一些，prod 多一些）？
# 后面有需要怎们再找它讨论更多的，目前mvp先不整