from django.shortcuts import render

# 게시글 작성 기능 구현
# blog/write

def post_new(request):
    pass

#  뷰 함수 이름은 현재 py 파일 내에서만 유일하면 된다.
#  다른 이름과 겹치면, 다른 함수를 덮어쓴다. 주의!!

# 게시글 목록 기능 구현
# /blog
def post_list(request):
    pass

# 게시글 상세보기 기능 구현
#  /blog/<int:id>
def post_detail(request, id: int):
    pass

# 게시글 검색 기능 구현
#  /blog/search/<str:tag>
def post_search(request, tag: str):
    pass

# 게시글 수정 기능 구현
#  /blog/edit/<int:id>
def post_edit(request, id: int):
    pass

# 게시글 삭제 기능 구현
#  /blog/delete/<int:id>
def post_delete(request, id: int):
    pass