================================================================================
                    경제 뉴스 브리핑 봇 - 사용 설명서
                 Economic News Briefing Bot for Beginners
================================================================================

■ 이 봇이 하는 일
--------------------------------------------------------------------------------
이 프로그램은 아래 순서대로 자동으로 경제 뉴스를 수집하고 정리합니다:

  1) 국내·글로벌 경제 뉴스 수집 (네이버 API + NewsAPI)
  2) 주요 시장 지표 수집 (S&P500, 나스닥, 엔비디아, 환율, 원유 등)
  3) OpenAI GPT-4o-mini로 뉴스 요약 및 브리핑 작성
  4) Notion 데이터베이스에 자동 저장

실행하면 Notion에 "오늘의 경제 뉴스 브리핑" 페이지가 하나 생성됩니다.


■ 사전 준비 (필수)
--------------------------------------------------------------------------------
  □ Python 3.8 이상 설치
  □ 필요한 API 키 5종 발급 (아래 'API 키 발급' 섹션 참고)
  □ Notion 계정


================================================================================
                        처음 설치 및 실행 방법
================================================================================

[1단계] Python 설치 확인
--------------------------------------------------------------------------------
  Windows 명령 프롬프트(CMD) 또는 PowerShell을 열고 다음을 입력하세요:

    python --version

  예: Python 3.11.0 이렇게 뜨면 정상입니다.
  없다면 https://www.python.org/downloads/ 에서 다운로드 후 설치하세요.
  설치 시 "Add Python to PATH"를 반드시 체크하세요.


[2단계] 프로젝트 폴더로 이동
--------------------------------------------------------------------------------
  CMD/PowerShell에서:

    cd d:\j\cursor\economic_news_bot

  (실제 프로젝트가 있는 경로로 바꾸세요.)


[3단계] 가상환경 생성 (선택, 권장)
--------------------------------------------------------------------------------
  같은 폴더에서:

    python -m venv venv

  그 다음, 가상환경 활성화:

    venv\Scripts\activate

  (PowerShell에서 실행 권한 오류가 나면: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser)


[4단계] 패키지 설치
--------------------------------------------------------------------------------
  가상환경이 활성화된 상태에서:

    pip install -r requirements.txt

  설치되는 패키지: openai, requests, yfinance, python-dotenv


[5단계] API 키 설정 (가장 중요!) — .env 파일 사용
--------------------------------------------------------------------------------
  ① 프로젝트 폴더에 .env 파일을 만듭니다.

       copy .env.example .env

     (PowerShell에서는: Copy-Item .env.example .env)

  ② .env 를 메모장이나 VS Code로 열어 빈 칸에 실제 값을 넣습니다.
     (변수 이름은 그대로 두고, = 뒤에만 붙여 넣으면 됩니다.)

  필요한 항목:
    - NAVER_CLIENT_ID, NAVER_CLIENT_SECRET  (네이버 개발자 센터)
    - NEWSAPI_KEY                            (newsapi.org)
    - OPENAI_API_KEY                         (platform.openai.com)
    - NOTION_TOKEN, NOTION_DATABASE_ID       (notion.so)

  각 API 키 발급 방법은 "apikey_how.md" 파일에 자세히 적혀 있습니다.


[6단계] 실행
--------------------------------------------------------------------------------
  같은 폴더에서:

    python main.py

  정상 동작 시:
    - 콘솔에 "경제 뉴스 브리핑 시작" 메시지가 보이고
    - 뉴스 수집 → 시장 데이터 수집 → GPT 요약 → Notion 저장 순으로 진행됩니다.
    - 마지막에 "Notion 저장 완료!" 및 페이지 URL이 출력됩니다.

  로그는 logs 폴더에 월별로 저장됩니다 (예: logs/2026-03.log).


================================================================================
                        API 키 발급 간단 가이드
================================================================================

자세한 내용은 apikey_how.md를 참고하세요. 여기서는 요약만 적습니다.

  1) 네이버 API
     - https://developers.naver.com
     - Application 등록 → 검색 API 체크 → Client ID, Client Secret 복사

  2) NewsAPI
     - https://newsapi.org
     - 회원가입 → Get API Key → API Key 복사

  3) OpenAI API
     - https://platform.openai.com
     - 회원가입 → 전화번호 인증 → 결제카드 등록 및 $5 충전 → API Keys에서 키 생성

  4) Notion
     - https://www.notion.so/my-integrations
     - New integration 생성 → Token 복사
     - Notion에서 새 페이지에 Table 데이터베이스 만들기
     - 페이지 우측 ... → Connections → 방금 만든 Integration 연결
     - 브라우저 URL에서 ?v= 앞 32자리 = DATABASE_ID


================================================================================
                        프로젝트 파일 구조
================================================================================

  main.py           - 실행 진입점 (여기서 python main.py 실행)
  config.py         - 환경 변수 / .env 에서 키를 읽어 오는 코드 (저장소에 포함)
  .env.example      - .env 만들 때 복사할 템플릿 (키 이름만, 값은 비움)
  .env              - 실제 키 (직접 만듦, Git 에 올리지 않음)

  news_fetcher.py   - 뉴스 수집 (네이버, NewsAPI)
  market_fetcher.py - 시장 데이터 수집 (yfinance)
  summarizer.py     - GPT로 뉴스 요약
  notion_writer.py  - Notion 저장

  requirements.txt  - pip 패키지 목록
  apikey_how.md     - API 키 발급 상세 가이드
  logs/             - 실행 로그 저장 폴더


================================================================================
                        자주 발생하는 오류와 해결
================================================================================

  ■ "ModuleNotFoundError: No module named 'config'"
    → 프로젝트 루트에 config.py 가 없습니다. 저장소에서 다시 받거나 복구하세요.

  ■ "수집된 뉴스가 없습니다. API 키를 확인하세요."
    → NAVER_CLIENT_ID, NEWSAPI_KEY 등이 올바르지 않습니다.
    → .env 파일 경로·변수 이름·값을 다시 확인하고, apikey_how.md 대로 재발급하세요.

  ■ "Notion 저장 실패 (상태코드: 401)" 또는 "403"
    → NOTION_TOKEN이 틀리거나, 해당 페이지에 Integration이 연결되지 않았습니다.
    → Notion 페이지 우측 ... → Connections → Integration 연결을 확인하세요.

  ■ "Notion 저장 실패 (상태코드: 400)"
    → NOTION_DATABASE_ID가 잘못되었거나, DB 속성이 다를 수 있습니다.
    → DB에 "날짜" 속성(Date 타입)이 있어야 합니다. apikey_how.md 참고.

  ■ "openai.AuthenticationError" 또는 API 키 오류
    → OPENAI_API_KEY를 확인하세요. sk-proj- 로 시작하는 형식이어야 합니다.
    → platform.openai.com에서 카드 등록 및 크레딧 충전이 되어 있어야 합니다.


================================================================================
                        보안 주의사항
================================================================================

  ⚠ 실제 키는 .env 에만 두세요. .env 는 .gitignore 되어 있어 보통 Git 에 안 올라갑니다.
  ⚠ config.py 에 YOUR_* 대신 진짜 키를 넣었다면 그 내용을 커밋·푸시하지 마세요.
  ⚠ GitHub Actions 는 Repository Secrets 만 사용하는 편이 안전합니다.


================================================================================
                        실행 요약 (한 번에 보기)
================================================================================

  1. python -m venv venv
  2. venv\Scripts\activate
  3. pip install -r requirements.txt
  4. copy .env.example .env
  5. .env 열어서 API 키 입력 (apikey_how.md 참고)
  6. python main.py

  → Notion에서 오늘의 경제 뉴스 브리핑 페이지 확인!


================================================================================
