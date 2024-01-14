from django.urls import reverse_lazy
from django.views import generic
from backlogext.models import Issue, Setting
from backlogext.forms import IssueCreateForm
from backlogext.src.api import Api
from backlogext.src.util import Util


class IssueListView(generic.ListView):
    """課題一覧ページ"""
    template_name = 'backlogext/issue_list.html'

    # settingを追加
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        try:
            ctx['setting'] = Setting.objects.get(user=self.request.user.id)
        except Setting.DoesNotExist:
            ctx['setting'] = None
            print('no setting')
        
        return ctx
    
    # ユーザに紐づくissueを表示
    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            issue = Issue.objects.all()
        else:
            issue = Issue.objects.filter(user=current_user.id)

        return issue.order_by('-id')

class IssueCreateView(generic.CreateView):
    """課題作成ページ"""
    template_name = 'backlogext/issue_form.html'
    form_class = IssueCreateForm
    success_url = reverse_lazy('backlogext:issue_list')

    # userを追加
    def form_valid(self, form):
        q = form.save(commit=False)
        q.user = self.request.user
        q.save()
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(IssueCreateView, self).get_form_kwargs()

        user = self.request.user
        api = Api(user)
        util = Util(user)
        self.header = util.get_headers()
        self.issue_types = api.get_issue_types(self.header)
        type_choices = [(issue_type['id'], issue_type['name']) for issue_type in self.issue_types]
        kwargs['type_choices'] = type_choices

        return kwargs

class IssueDetailView(generic.DetailView):
    """課題詳細ページ"""
    template_name = 'backlogext/issue_detail.html'
    model = Issue
    
class IssueUpdateView(generic.UpdateView):
    """課題更新ページ"""
    template_name = 'backlogext/issue_form.html'
    model = Issue
    form_class = IssueCreateForm
    success_url = reverse_lazy('backlogext:issue_list')

    def get_form_kwargs(self):
        kwargs = super(IssueUpdateView, self).get_form_kwargs()

        user = self.request.user
        api = Api(user)
        util = Util(user)
        self.header = util.get_headers()
        self.issue_types = api.get_issue_types(self.header)
        type_choices = [(issue_type['id'], issue_type['name']) for issue_type in self.issue_types]
        kwargs['type_choices'] = type_choices

        return kwargs

class IssueDeleteView(generic.DeleteView):
    """課題削除ページ"""
    template_name = 'backlogext/issue_confirm_delete.html'
    model = Issue
    success_url = reverse_lazy('backlogext:issue_list')