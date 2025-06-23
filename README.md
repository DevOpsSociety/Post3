# 📅 2025년 3 – 6월 스터디 진행 일정표

| 기간 | 학습·활동 내용 | 결과물 / 체크포인트 |
|------|---------------|---------------------|
| **3월 1주 ~ 4월 중간고사 전** | - 파이썬 기초 문법<br>  (변수·자료형·연산자·조건문·반복문·기본 함수) | ✅ 주요 예제 코드 완성<br>✅ 기초 문제 풀이 20선 |
| **4월 중간고사 직후 (4월 3주)** | - Git & GitHub 기본 사용법 학습<br>  (git init, add, commit, push, pull, clone 등) | ✅ 개인 테스트 리포지토리 생성<br>✅ 첫 커밋 & 원격 푸시 |
| **4월 4주 ~ 5월 1주** | - GitHub 협업 흐름 실습<br>  (레포지토리 조직, 브랜치 전략, PR·Merge) | ✅ 팀 리포지토리 개설<br>✅ feature 브랜치 → PR → Merge 경험 |
| **5월 2주** | - 백엔드 아키텍처·REST 흐름 이론 강의 수강 | ✅ REST 설계 원칙 요약 노트<br>✅ HTTP 메서드·상태코드 정리 |
| **5월 2주 말 ~ 5월 3주 초** | - 데이터베이스 스키마 설계<br>  - ERD 작성 (MySQL Workbench / draw.io) | ✅ 테이블 정의서(DDL 초안)<br>✅ ERD 다이어그램 |
| **5월 3주** | - FastAPI 프레임워크 기초 개념 학습<br>  (라우팅, 의존성 주입, Pydantic 모델) | ✅ FastAPI 스캐폴딩 완료<br>✅ Hello World 서버 구동 |
| **5월 4주 ~ 6월 말** | - 블로그 프로젝트 본격 개발 시작<br>  • 기본 Auth: 회원가입·로그인<br>  • 게시물 CRUD API<br>  • 댓글 기능<br>  • GitHub Flow 기반 협업 지속 | ✅ `/users`, `/auth` 엔드포인트 완성<br>✅ `/posts`, `/comments` 엔드포인트 완성<br>✅ README & API 명세 초안 |

# 팀원 각자 ERD 설계 

<img width="722" alt="image" src="https://github.com/user-attachments/assets/82c7eb15-d683-424c-922d-b2cb052b4b3c" />

<img width="881" alt="image" src="https://github.com/user-attachments/assets/4c039fb9-74e7-4fd9-9668-e12edef01c71" />

<img width="711" alt="image" src="https://github.com/user-attachments/assets/14bf8ba6-606d-4634-8a78-6da7db318772" />

<img width="711" alt="image" src="https://github.com/user-attachments/assets/b3f28b39-ccc1-4cc6-9389-408c65dc0c20" />

# 🖥️ 백엔드(Back-End)란?

백엔드는 **클라이언트(브라우저·모바일 앱 등)가 보낸 요청을 처리해 적절한 데이터를 만들어서 다시 응답해 주는** 서버 측 영역입니다.

---

## ✅ 백엔드가 하는 일

| 역할 | 설명 |
|------|------|
| **데이터 관리** | 데이터베이스에 정보 **저장·조회·수정·삭제(CRUD)** |
| **비즈니스 로직** | 서비스 규칙·계산 수행 <br> 예) 조회수 +1, 재고 부족 시 주문 거절 |
| **요청 ↔ 응답** | 클라이언트의 **HTTP 요청** 수신 → 결과를 **JSON·HTML** 등으로 반환 |
| **보안·검증** | 입력값 검증, 접근 권한 확인, 예외 처리 |
| **인프라 운영** | 서버 실행·모니터링·로그 관리 → 24시간 안정적 서비스 유지 |

> **한마디로**  
> **“사용자가 필요로 하는 데이터를 안전하고 정확하게 준비해 돌려주는 것”**




# 📝 간단 블로그 프로젝트

> **Flask + FastAPI** 스터디 산출물  
> 게시글 CRUD, 조회수 증가, 상태 관리 기능이 포함된 **블로그 서비스**입니다.

---

## 📁 프로젝트 구조
<img src="img.png" alt="프로젝트 구조" width="400"/>

---

```markdown

## ✨ 주요 기능

| 구분 | 엔드포인트 | 설명 |
|-----|------------|------|
| 게시글 작성 | `POST /posts` | 새 게시글 등록 |
| 게시글 목록 | `GET /posts` | 전체 게시글 조회 |
| 게시글 상세 | `GET /posts/<id>` | 단일 게시글 및 조회수 +1 |
| 게시글 수정 | `PUT /posts/<id>` | 내용·상태 변경 |
| 게시글 삭제 | `DELETE /posts/<id>` | 게시글 제거 |
| 게시글 상태 | — | `공개`, `비공개`, `임시` 관리 가능 |

```

## 🛠️ 설치 & 실행


# 의존성 설치
pip install -r requirements.txt

# 개발 서버 실행
python run.py

기본 접속 주소: http://127.0.0.1:5000

```bash

# 원격 저장소 확인
git remote -v

# 브랜치 최신화
git fetch
git checkout master
git pull origin master

# 개인 브랜치 생성·이동
git checkout -b <username>

# 작업 후 커밋 & 푸시
git status
git add .
git commit -m "feat: <설명>"
git push origin <username>
충돌 해결
git merge master 후 충돌 파일 확인

<<<<<<<, =======, >>>>>>> 구간 정리

git add <파일> → git commit -m "merge: 충돌 해결"

```
# 저장소
https://github.com/chuawj/fast_api/tree/seungjun?tab=readme-ov-file

# 스터디 회고


| 이름  | 느낀 점                      | 아쉬운 점              |
| --- | ------------------------- | ------------------ |
| 친   | 혼자였다면 하지 않았을 공부를 하게 되어 만족 | 시험·축제로 흐름이 끊김      |
| 최현준 | 새로운 학습·도전을 경험             | 전원 참여가 부족해 결과물 아쉬움 |
| 송승준 | 다양한 경험·학습이 뜻깊음            | 바쁜 일정으로 완성도 부족     |
| 김혜연 | 새롭게 알게 된 부분이 많음           | 적극적인 의견 교류 부족      |
| 황원준 | 새로운 언어 학습 기회              | 일정 겹침으로 완성도 낮음     |
| 홍주희 | 공부 방향을 잡는 데 도움            | 참여율 낮아 아쉬움         |

