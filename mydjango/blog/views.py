from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.middleware.csrf import get_token
from datetime import datetime
# from .models import Category 

# 게시글 작성 기능 구현
# blog/write
# blog/views.py
# # 메모리에 게시글 저장 (임시)
users = {'admin': 'password123', 'user1': '1234'}
posts_memory = []
current_user = None

def post_list(request):
    """메인 페이지 - 게시글 목록"""
    global current_user
    # 로그인 상태 확인
    login_status = ""
    if current_user:
        login_status = f"""
        <div style="text-align: right; margin-bottom: 10px;">
            <span style="color: #007bff;">환영합니다, {current_user}님!</span> | 
            <a href="/logout/" style="color: #dc3545; text-decoration: none;">로그아웃</a>
        </div>
        """

    # 새 게시글 작성 버튼 (로그인한 사용자만)
    write_button = ""
    if current_user:
        write_button = '<a href="/post/new/" class="btn">새 게시글 작성</a>'
    else:
        write_button = '<p style="color: #666;">게시글을 작성하려면 <a href="/login/">로그인</a>하세요.</p>'
    
    html = f"""
    <html>
    <head>
        <title>내 블로그</title>
        <style>
            body {{ font-family: Arial; margin: 20px; background-color: #f5f5f5; }}
            .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
            h1 {{ color: #333; text-align: center; border-bottom: 2px solid #007bff; padding-bottom: 10px; }}
            .post {{ border-bottom: 1px solid #eee; padding: 15px 0; margin-bottom: 10px; }}
            .post-title {{ font-size: 1.2em; font-weight: bold; color: #333; }}
            .post-author {{ color: #007bff; font-size: 0.9em; }}
            .post-date {{ color: #666; font-size: 0.9em; margin: 5px 0; }}
            .post-content {{ margin: 10px 0; line-height: 1.6; }}
            .btn {{ padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; display: inline-block; margin: 5px; }}
            .btn:hover {{ background-color: #0056b3; }}
            .stats {{ text-align: center; margin: 20px 0; padding: 15px; background-color: #f8f9fa; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <div class="container">
            {login_status}
            <h1>내 블로그</h1>
            
            <div class="stats">
                <strong>📊 블로그 통계</strong><br>
                총 게시글: {len(posts_memory)}개 | 등록된 사용자: {len(users)}명
            </div>
            
            <div style="text-align: center; margin: 20px;">
                {write_button}
                <a href="/admin/" class="btn" style="background-color: #28a745;">관리자 페이지</a>
            </div>
            
            <h2>📝 게시글 목록</h2>
    """
    
    if posts_memory:
        for i, post in enumerate(reversed(posts_memory)):  # 최신글이 위로
            html += f"""
            <div class="post">
                <div class="post-title">{post['title']}</div>
                <div class="post-author">✍️ 작성자: {post['author']}</div>
                <div class="post-date">📅 작성일: {post['date']}</div>
                <div class="post-content">{post['content'][:150]}{'...' if len(post['content']) > 150 else ''}</div>
                <a href="/post/{i}/" style="color: #007bff; text-decoration: none; font-size: 0.9em;">자세히 보기 →</a>
            </div>
            """
    else:
        html += """
        <div style="text-align: center; padding: 40px; color: #666;">
            <h3>📭 아직 게시글이 없습니다</h3>
            <p>첫 번째 게시글을 작성해보세요!</p>
        </div>
        """
    
    html += """
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def login_page(request):
    """로그인 페이지"""
    global current_user
    
    error_message = ""
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        if username in users and users[username] == password:
            current_user = username
            return redirect('/')
        else:
            error_message = '<div style="color: red; text-align: center; margin: 10px;">❌ 사용자명 또는 비밀번호가 틀렸습니다.</div>'
    
    html = f"""
    <html>
    <head>
        <title>로그인 - 내 블로그</title>
        <style>
            body {{ font-family: Arial; margin: 20px; background-color: #f5f5f5; }}
            .container {{ max-width: 400px; margin: 100px auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
            h1 {{ text-align: center; color: #333; margin-bottom: 30px; }}
            .form-group {{ margin-bottom: 15px; }}
            label {{ display: block; margin-bottom: 5px; font-weight: bold; color: #333; }}
            input {{ width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; font-size: 14px; }}
            .btn {{ width: 100%; padding: 12px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; font-weight: bold; }}
            .btn:hover {{ background-color: #0056b3; }}
            .back-link {{ text-align: center; margin-top: 20px; }}
            .back-link a {{ color: #007bff; text-decoration: none; }}
            .demo-info {{ background-color: #e7f3ff; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔐 로그인</h1>
            
            <div class="demo-info">
                <strong>📋 테스트 계정:</strong><br>
                사용자명: admin, 비밀번호: password123<br>
                사용자명: user1, 비밀번호: 1234
            </div>
            
            {error_message}
            
            <form method="post">
                <div class="form-group">
                    <label>👤 사용자명:</label>
                    <input type="text" name="username" required>
                </div>
                <div class="form-group">
                    <label>🔑 비밀번호:</label>
                    <input type="password" name="password" required>
                </div>
                <button type="submit" class="btn">로그인</button>
            </form>
            
            <div class="back-link">
                <a href="/">🏠 메인 페이지로 돌아가기</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def logout_page(request):
    """로그아웃"""
    global current_user
    current_user = None
    
    html = """
    <html>
    <head>
        <title>로그아웃 완료</title>
        <style>
            body { font-family: Arial; margin: 20px; background-color: #f5f5f5; }
            .container { max-width: 400px; margin: 100px auto; background: white; padding: 30px; border-radius: 8px; text-align: center; }
            .btn { padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>👋 로그아웃 완료</h1>
            <p>안전하게 로그아웃되었습니다.</p>
            <a href="/" class="btn">메인 페이지로 이동</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def post_new(request):
    """새 게시글 작성"""
    global current_user
    
    # 로그인 체크
    if not current_user:
        return redirect('/login/')
    
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        
        if title and content:
            post = {
                'title': title,
                'content': content,
                'author': current_user,
                'date': datetime.now().strftime('%Y년 %m월 %d일 %H:%M')
            }
            posts_memory.append(post)
            return redirect('/')
    
    html = f"""
    <html>
    <head>
        <title>새 게시글 작성 - 내 블로그</title>
        <style>
            body {{ font-family: Arial; margin: 20px; background-color: #f5f5f5; }}
            .container {{ max-width: 600px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; }}
            h1 {{ color: #333; text-align: center; border-bottom: 2px solid #007bff; padding-bottom: 10px; }}
            .form-group {{ margin-bottom: 15px; }}
            label {{ display: block; margin-bottom: 5px; font-weight: bold; }}
            input[type="text"], textarea {{ width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }}
            .btn {{ padding: 10px 20px; margin: 5px; border-radius: 5px; border: none; cursor: pointer; text-decoration: none; display: inline-block; }}
            .btn-success {{ background-color: #28a745; color: white; }}
            .btn-secondary {{ background-color: #6c757d; color: white; }}
            .btn:hover {{ opacity: 0.8; }}
            .author-info {{ background-color: #e7f3ff; padding: 10px; border-radius: 5px; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✍️ 새 게시글 작성</h1>
            
            <div class="author-info">
                📝 작성자: <strong>{current_user}</strong>
            </div>
            
            <form method="post">
                <div class="form-group">
                    <label>📌 제목:</label>
                    <input type="text" name="title" required placeholder="게시글 제목을 입력하세요">
                </div>
                <div class="form-group">
                    <label>📄 내용:</label>
                    <textarea name="content" rows="15" required placeholder="게시글 내용을 입력하세요"></textarea>
                </div>
                <button type="submit" class="btn btn-success">💾 저장</button>
                <a href="/" class="btn btn-secondary">❌ 취소</a>
            </form>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def post_detail(request, pk):
    """게시글 상세 보기"""
    try:
        post = posts_memory[int(pk)]
        html = f"""
        <html>
        <head>
            <title>{post['title']} - 내 블로그</title>
            <style>
                body {{ font-family: Arial; margin: 20px; background-color: #f5f5f5; }}
                .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; }}
                h1 {{ color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }}
                .post-info {{ background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0; }}
                .post-content {{ margin: 20px 0; line-height: 1.6; }}
                .btn {{ padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; margin: 5px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{post['title']}</h1>
                <div class="post-info">
                    👤 작성자: <strong>{post['author']}</strong> | 
                    📅 작성일: <strong>{post['date']}</strong>
                </div>
                <div class="post-content">
                    {post['content'].replace(chr(10), '<br>')}
                </div>
                <a href="/" class="btn">← 목록으로 돌아가기</a>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html)
    except:
        return HttpResponse("<h1>게시글을 찾을 수 없습니다.</h1><a href='/'>돌아가기</a>")

def post_edit(request, pk):
    """게시글 수정 (추후 구현)"""
    return HttpResponse("<h1>수정 기능은 추후 구현 예정입니다.</h1><a href='/'>돌아가기</a>")