from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import Issue, Setting

User = get_user_model()

class IssueCreateForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('summary', 'description')

class SettingCreateForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ('space_key', 'project_key', 'project_id', 'client_id', 'client_secret')

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'