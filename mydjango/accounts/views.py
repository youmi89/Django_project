
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

# 함수기반 뷰 (Function Based View, FBV)
def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()  # 데이터베이스에 User 레코드가 insert된다.
            return redirect("/login")
    else:
        form = UserCreationForm()
    return render(request,"accounts/register_form.html", 
        {"form": form,
        })

# 클래스기반 뷰를 사용한 회원가입 (Class Based View, CBV)
# form django.views.generic.edit import CreateView

# register = CreateView.as_view(
#     form_class=UserCreationForm,
#     template_name="accounts/register_form.html",)
#     seccess_url="/login"


# def login(request):
# pass

login = LoginView.as_view()