# =============================================
# 경제 뉴스 브리핑 봇 - API 키 설정
# 우선순위: 환경 변수 > 프로젝트 루트의 .env 파일 > 아래 기본값
# GitHub Actions: Repository Secrets를 env로 넣으면 config.py 없이 동작합니다.
# =============================================

import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def _cfg(key: str, default: str) -> str:
    v = os.environ.get(key)
    if v is not None and str(v).strip():
        return str(v).strip()
    return default


NAVER_CLIENT_ID     = _cfg("NAVER_CLIENT_ID", "YOUR_NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = _cfg("NAVER_CLIENT_SECRET", "YOUR_NAVER_CLIENT_SECRET")
NEWSAPI_KEY         = _cfg("NEWSAPI_KEY", "YOUR_NEWSAPI_KEY")
OPENAI_API_KEY      = _cfg("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")
NOTION_TOKEN        = _cfg("NOTION_TOKEN", "YOUR_NOTION_TOKEN")
NOTION_DATABASE_ID  = _cfg("NOTION_DATABASE_ID", "YOUR_NOTION_DATABASE_ID")
