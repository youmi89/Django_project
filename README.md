## Django 이용한 충남 여행코스 추천 blog만들기 project

🎯 주요 기능 구현 목표

-충남 여행지 검색 및 필터링

-여행 코스 추천 시스템

-지역별 카테고리 분류

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
    최종점검+문서작성           :final, 2025-07-09, 1d ```
