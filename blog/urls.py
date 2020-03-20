from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('whoami', views.WhoamiView.as_view(), name='whoami'),
    path('<slug:slug>/', views.ArticleView.as_view(), name='article')
]
