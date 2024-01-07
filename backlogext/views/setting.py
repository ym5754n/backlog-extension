from django.urls import reverse_lazy
from django.views import generic
from backlogext.models import Setting
from backlogext.forms import SettingCreateForm


class SettingCreateView(generic.CreateView):
    """設定作成ページ"""
    template_name = 'backlogext/setting_form.html'
    form_class = SettingCreateForm
    success_url = reverse_lazy('backlogext:issue_list')

    # userを追加
    def form_valid(self, form):
        q = form.save(commit=False)
        q.user = self.request.user
        q.save()
        return super().form_valid(form)

class SettingUpdateView(generic.UpdateView):
    """設定更新ページ"""
    template_name = 'backlogext/setting_form.html'
    model = Setting
    form_class = SettingCreateForm
    success_url = reverse_lazy('backlogext:issue_list')