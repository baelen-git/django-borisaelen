from . import views
from django.urls import include
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('whoami', views.WhoamiView.as_view(), name='whoami'),
    path('<slug:slug>/', views.ArticleView, name='article')
]
