# articles/urls.py

from django.urls import path, include
from articles import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name="ArticleList"),
    path('<int:article_id>/', views.ArticleDetail.as_view(), name="ArticleDetail"), # <int:pk> 라고 해도 상관 없음. 그냥 변수 명을 article_id로 받은 것.
]