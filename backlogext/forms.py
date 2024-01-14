from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import Issue, Setting

User = get_user_model()

class IssueCreateForm(forms.ModelForm):
    type_id = forms.ChoiceField()

    def __init__(self, type_choices=None, *args, **kwargs):
        self.base_fields['type_id'].choices = type_choices
        super(IssueCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Issue
        fields = ('type_id', 'summary', 'description')

class SettingCreateForm(forms.ModelForm):
    domain = forms.ChoiceField()

    def __init__(self, domain_choices=None, *args, **kwargs):
        self.base_fields['domain'].choices = domain_choices
        super(SettingCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Setting
        fields = ('space_key', 'domain', 'project_key', 'project_id', 'client_id', 'client_secret')

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