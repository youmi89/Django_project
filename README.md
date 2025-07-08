## Django 이용한 충남 여행코스 추천 blog만들기 project

🎯 주요 기능 구현 목표

-충남 여행지 카테고리선택, 글작성 
-blog login, logout, 회원가입 구현

-사용자 리뷰 및 평점 시스템

-반응형 웹 디자인

## WBS

```mermaid
%%{init: {'gantt': {'useWidth': 1200}}}%%
gantt
    title 충남 여행 코스 추천 프로젝트 일정표 (7/2~7/9)
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d

    section 기획/설정
    요구사항분석+기능설계       :done, req, 2025-07-02, 1d
    Django생성+가상환경        :done, setup1, 2025-07-02, 1d
    PostgreSQL연동            :done, setup2, 2025-07-03, 1d
    
    section 백엔드개발
    모델설계+여행지모델         :active, model, 2025-07-03, 1d
    코스모델+API설계           :api_design, 2025-07-04, 1d
    여행지CRUD API            :api_travel, 2025-07-04, 2d
    코스추천API               :api_course, 2025-07-05, 2d
    
    section 데이터작업
    충남여행지조사             :data_research, 2025-07-03, 2d
    여행지정보입력             :data_input, 2025-07-05, 1d
    코스데이터생성             :course_data, 2025-07-06, 1d
    
    section 프론트엔드
    HTML구조+메인페이지        :html_design, 2025-07-05, 1d
    목록+추천페이지            :html_pages, 2025-07-06, 1d
    CSS스타일링               :css_style, 2025-07-06, 2d
    JavaScript+API연동         :js_function, 2025-07-07, 2d
    
    section 완료단계
    기능테스트+버그수정         :test, 2025-07-08, 1d
    최종점검+문서작성           :final, 2025-07-09, 1d
```





## 🎬 구현 영상
https://github.com/user-attachments/assets/f7264b35-5364-4a9a-9b5d-095e06cd5852

## 📸 주요 화면 스크린샷

### 메인 페이지
<img width="400" height="400" alt="Image" src="https://github.com/user-attachments/assets/dc9be9b1-1b33-4705-80bb-0dfff7f1608c" />

### 로그인 페이지 
<img width="400" height="400" alt="Image" src="https://github.com/user-attachments/assets/54519237-3183-442a-9dcc-e99ed45812c0" />

### 새 글 작성 페이지
<img width="400" height="400" alt="Image" src="https://github.com/user-attachments/assets/46db5e65-cbb7-48c5-a68a-bb1bcc6e90e9" />

### 게시글 목록 페이지
<img width="400" height="400" alt="Image" src="https://github.com/user-attachments/assets/ada5ab1a-4b2b-4ef8-bebc-fc50ff626dd9" />

### 로그아웃 페이지
<img width="400" height="400" alt="Image" src="https://github.com/user-attachments/assets/a8faddd8-e4e7-4293-a8e4-4130b44d2de5" />

## ✨ 주요 기능

- ✅ **로그인/로그아웃**: 안전한 사용자 인증 시스템
- ✅ **게시글 관리**: Django Admin을 통한 게시글 CRUD
- ✅ **반응형 디자인**: 모바일과 데스크톱 모두 지원
- ✅ **메시지 시스템**: 성공/오류 메시지 표시

## 🛠️ 사용된 기술

| 분야 | 기술 스택 |
|------|-----------|
| **Backend** | Django 4.2.7 |
| **Database** | SQLite |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Authentication** | Django Auth |
| **Styling** | Custom CSS |

## 📋 설치 및 실행 방법

### 2️⃣ 가상환경 설정
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux  
source venv/bin/activate
```

### 3️⃣ 패키지 설치
```bash
pip install django
```

### 4️⃣ 데이터베이스 설정
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ 슈퍼유저 생성
```bash
python manage.py createsuperuser
```

### 6️⃣ 서버 실행
```bash
python manage.py runserver
```

### 7️⃣ 웹사이트 접속
- **메인페이지**: http://127.0.0.1:8000/
- **로그인**: http://127.0.0.1:8000/login/
- **게시글작성**: http://127.0.0.1:8000/post/new/
- **게시글보기**: http://127.0.0.1:8000/post/0/
- **로그아웃**: http://127.0.0.1:8000/logout/
## 📂 프로젝트 구조

```
django-blog/
├── 📁 blog/                    # 메인 앱
│   ├── 📁 migrations/
│   ├── 📁 templates/blog/
│   │   ├── 🌐 home.html
│   │   ├── 🌐 signup.html
│   │   └── 🌐 login.html
│   ├── 📄 models.py            # Post 모델
│   ├── 📄 views.py             # 뷰 함수들
│   ├── 📄 forms.py             # 회원가입 폼
│   ├── 📄 admin.py             # 관리자 설정
│   └── 📄 urls.py              # URL 라우팅
├── 📁 myproject/               # 프로젝트 설정
│   ├── 📄 settings.py
│   ├── 📄 urls.py
│   └── 📄 wsgi.py
├── 📁 demo/                    # 데모 영상/GIF
│   ├── 🎬 demo.gif
│   ├── 🎬 signup_demo.gif
│   └── 🎬 admin_demo.gif
├── 📁 images/                  # 스크린샷
│   ├── 🖼️ main.png
│   ├── 🖼️ signup.png
│   └── 🖼️ admin.png
├── 📄 manage.py
├── 📄 db.sqlite3
└── 📄 README.md
```

## 🎯 주요 기능 상세

### 🏠 메인 페이지
- 모든 게시글 목록 표시
- 로그인 상태에 글작성가능
- 반응형 카드 레이아웃

## 🌟 향후 개발 계획

- [ ] 댓글 시스템
- [ ] 카테고리 분류
- [ ] 태그 기능
- [ ] 검색 기능
- [ ] 프로필 이미지 업로드
- [ ] 이메일 인증
- [ ] 소셜 로그인 (Google, GitHub)

---



