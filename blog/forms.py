from .models import Comment
from django import forms
from django.urls import reverse
from tinymce.widgets import TinyMCE


class CommentForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    # email = forms.EmailField(label="E-Mail (won't show)", max_length=100)
    body = forms.CharField(label="Comment", widget=TinyMCE(
                    attrs={"cols": 80, "rows": 30},
                    mce_attrs={
                        "selector": 'textarea#id_body',
                        "height": 200,
                        "menubar": "false",
                        "plugins": "codesample,tabfocus,advlist,autolink,lists,link,image,imagetools,charmap,print,preview,anchor,searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,code,help,wordcount",
                        "toolbar": "undo redo | fontsizeselect codesample | bold italic backcolor | alignleft aligncenter alignright | bullist numlist outdent indent | removeformat | help",
                        "content_style": "body { font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace; }",
                    },
                ))
    class Meta:
        model = Comment
        fields = ('name', 'body')
        # fields = ('name', 'email', 'body')