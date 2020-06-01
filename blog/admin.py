from django.contrib import admin
from django.urls import reverse
from tinymce.widgets import TinyMCE
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'creation_date')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ("content"):
            return db_field.formfield(
                widget=TinyMCE(
                    attrs={"cols": 80, "rows": 30},
                    mce_attrs={"external_link_list_url": reverse("tinymce-linklist")},
                )
            )
        return super(ArticleAdmin, self).formfield_for_dbfield(db_field, **kwargs)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'article', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.app_list = 'blog'
admin.site.site_header = 'Administration'
admin.site.index_title = 'borisaelen.nl'
admin.site.register(Article, ArticleAdmin)

