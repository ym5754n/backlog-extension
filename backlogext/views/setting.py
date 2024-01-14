from django.urls import reverse_lazy
from django.views import generic
from backlogext.models import Setting
from backlogext.forms import SettingCreateForm
from django.shortcuts import redirect

DOMAIN_CHOICES = [
    ('backlog.jp', 'backlog.jp'),
    ('backlog.com', 'backlog.com'),
    ]

class SettingCreateView(generic.CreateView):
    """設定作成ページ"""
    template_name = 'backlogext/setting_form.html'
    form_class = SettingCreateForm
    success_url = reverse_lazy('backlogext:issue_list')

    # settingが存在する場合、setting_updateにリダイレクトする
    def get(self, request, *args, **kwargs):
        try:
            setting = Setting.objects.get(user=self.request.user.id)
        except Setting.DoesNotExist:
            return super().get(request, *args, **kwargs)
        
        return redirect(f'/setting_update/{setting.pk}')
            
    # userを追加
    def form_valid(self, form):
        q = form.save(commit=False)
        q.user = self.request.user
        q.save()
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(SettingCreateView, self).get_form_kwargs()
        kwargs['domain_choices'] = DOMAIN_CHOICES
        return kwargs

class SettingUpdateView(generic.UpdateView):
    """設定更新ページ"""
    template_name = 'backlogext/setting_form.html'
    model = Setting
    form_class = SettingCreateForm
    success_url = reverse_lazy('backlogext:issue_list')

    def get_form_kwargs(self):
        kwargs = super(SettingUpdateView, self).get_form_kwargs()
        kwargs['domain_choices'] = DOMAIN_CHOICES
        return kwargs