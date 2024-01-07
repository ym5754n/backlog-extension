from django.contrib import admin
from .models import Issue, Token, Setting

# Register your models here.
admin.site.register(Issue)
admin.site.register(Token)
admin.site.register(Setting)