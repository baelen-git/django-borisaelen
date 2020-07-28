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
                        "block_formats": "Paragraph=p; Heading 1=h1; Heading 3=h3; Pre=pre",
                        "plugins": "code,tabfocus,advlist,autolink,lists,link,charmap,preview,anchor,searchreplace,visualblocks,fullscreen,insertdatetime,paste,help,wordcount",
                        "toolbar": "undo | formatselect | bold italic backcolor codesample | bullist numlist help",
                        "content_style": "body { font-family: 'Ubuntu Mono', monospace; }",
                    },
                ))
    class Meta:
        model = Comment
        fields = ('name', 'body')
        # fields = ('name', 'email', 'body')