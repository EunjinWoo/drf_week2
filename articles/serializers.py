from rest_framework import serializers
from articles.models import Article

# Article 모델을 기반으로 하는 시리얼라이저를 만들기 위함
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__" # 모든 필드를 다 다뤄주겠다는 의미.
        