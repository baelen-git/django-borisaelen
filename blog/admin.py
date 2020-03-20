
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Article

class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'creation_date')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')

admin.site.app_list = 'blog'
admin.site.site_header = 'Administration'
admin.site.index_title = 'borisaelen.nl'
admin.site.register(Article, ArticleAdmin)
