## 📁 프로젝트 구조

post/<br>
│<br>
├── app/ # 애플리케이션 주요 코드 폴더<br>
│ ├── init.py # Flask 앱 생성 및 설정<br>
│ ├── models/ # DB 모델 정의<br>
│ │ └── post.py # Post 모델 (게시글 테이블)<br>
│ ├── routes/ # API 라우터 정의<br>
│ │ └── post_routes.py # 게시글 관련 API (등록, 조회, 수정 등)<br>
│ └── database.py # SQLAlchemy DB 객체 생성<br>
│<br>
├── config.py # 앱 환경설정 (DB URI, 시크릿 키 등)<br>
├── run.py # Flask 앱 실행 진입점<br>
├── requirements.txt # 필요한 라이브러리 목록<br>
└── .venv/ # Python 가상환경 폴더 (PyCharm에서 자동 생성)
---
## 📌 주요 기능 요약

- 게시글 작성 (POST)
- 게시글 목록 조회 (GET)
- 단일 게시글 상세 조회 (GET)
- 게시글 수정 (PUT)
- 게시글 삭제 (DELETE)
- 조회수 자동 증가 기능
- 게시글 상태(`공개`, `비공개`, `임시`) 관리
---
### 📦 패키지 설치

`
pip install -r requirements.txt
`
---
### 🚀 Flask 서버 실행

`
python run.py
` 서버 주소: http://127.0.0.1:5000