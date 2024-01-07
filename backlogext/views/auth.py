from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from backlogext.forms import LoginForm, SignupForm


class Login(LoginView):
    """ログイン"""
    form_class = LoginForm
    template_name = 'backlogext/login.html'

class Logout(LogoutView):
    """ログアウト"""
    template_name = 'backlogext/login.html'

class Signup(generic.CreateView):
    """会員登録"""
    template_name = 'backlogext/user_form.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save()
        return redirect('backlogext:issue_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context