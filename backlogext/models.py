from django.db import models
from django.contrib.auth import get_user_model

class Issue(models.Model):
    key_id = models.IntegerField('課題キー', blank=True, null=True)
    type_id = models.IntegerField('課題種別キー', blank=True, null=True)
    project_key = models.CharField('project key', max_length=255, blank=True, null=True)
    summary = models.CharField('件名', max_length=255)
    description = models.TextField('詳細')
    created_at = models.DateTimeField('作成日時', auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.summary
    
class Token(models.Model):
    access_token = models.CharField('token', max_length=255, blank=True, null=True)
    refresh_token = models.CharField('refresh_token', max_length=255, blank=True, null=True)
    expires_in = models.IntegerField('expires_in', blank=True, null=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.access_token
    
class Setting(models.Model):
    space_key = models.CharField('space key', max_length=255)
    domain = models.CharField('domain', max_length=255, blank=True, null=True)
    project_key = models.CharField('project key', max_length=255)
    project_id = models.IntegerField('project id', blank=True, null=True)
    code = models.CharField('code', max_length=255, blank=True, null=True)
    client_id = models.CharField('client id', max_length=255)
    client_secret = models.CharField('client secret', max_length=255)
    updated_at = models.DateTimeField('updated_at', auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.space_key