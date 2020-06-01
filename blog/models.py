import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='date created')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='date modified')
    pub_date = models.DateTimeField(verbose_name='date published', null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-creation_date']

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now & self.status == STATUS[1]
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
