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

