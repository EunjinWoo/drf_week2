# articles/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from articles.models import Article
from articles.serializers import ArticleSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
"""
# class ArticleView의 함수형 view.

@api_view(['GET', 'POST'])
def articleAPI(request):
    if request.method == 'GET':
        articles = Article.objects.all() # 이렇게 articles 받아오기
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data) # 꼭 "data = " 부분 추가해 줘야 함. 안 그럼 에러남.
        if serializer.is_valid(): # is_valid를 통해 필요한 것들이 다 들어와있는지, model 정의 시 정해 둔 조건들에 부합하는 지 등 이 데이터의 유효성을 판단함.
            serializer.save() # 꼭 유효성 검사 후 save 해야 함. 그렇지 않으면 에러 남.
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 잘 저장되면, 이렇게 serialized된 데이터를 response로 돌려보내 줌.
        else:
            print(serializer.errors) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all() # 이렇게 articles 받아오기
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request, format=None):
        serializer = ArticleSerializer(data = request.data) # 꼭 "data = " 부분 추가해 줘야 함. 안 그럼 에러남.
        if serializer.is_valid(): # is_valid를 통해 필요한 것들이 다 들어와있는지, model 정의 시 정해 둔 조건들에 부합하는 지 등 이 데이터의 유효성을 판단함.
            serializer.save() # 꼭 유효성 검사 후 save 해야 함. 그렇지 않으면 에러 남.
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 잘 저장되면, 이렇게 serialized된 데이터를 response로 돌려보내 줌.
        else:
            print(serializer.errors) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
# class ArticleDetail의 함수형 view.

@api_view(['GET','PUT','DELETE'])
def articleDetailAPI(request, article_id): # 여기 id 값 안 넣어주면 에러 남!
    if request.method == 'GET':
        # article = Article.objects.get(id=article_id) # Article 모델 테이블에서 id가 article_id인 애를 가져와라.
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        article = get_object_or_404(Article, id=article_id) # 수정도 상세페이지와 마찬가지로 특정 id의 게시글을 가져와야 함.
        serializer = ArticleSerializer(article, data = request.data) 
        # 이렇게 하면 GET과 POST의 짬뽕 느낌으로, serializer가 알아서 앞의 article을 기존 article로 인식하고, 
        # 뒤에 data를 새롭게 들어온 걸로 인식해서 알아서 앞의 article을 뒤에 들어온 data = request.data로 바꿔줌.
        # 이렇게 알아서 수정이 되고, 수정이 되면 나머지는 위의 post와 동일하게 db에 저장해주면 됨.
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            print(serializer.errors) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) # HTTP_200_OK 해도 됨.
"""

class ArticleDetail(APIView):
    def get(self, request, article_id, format=None):
        # article = Article.objects.get(id=article_id) # Article 모델 테이블에서 id가 article_id인 애를 가져와라.
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ArticleSerializer)
    def put(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id) # 수정도 상세페이지와 마찬가지로 특정 id의 게시글을 가져와야 함.
        serializer = ArticleSerializer(article, data = request.data) 
        # 이렇게 하면 GET과 POST의 짬뽕 느낌으로, serializer가 알아서 앞의 article을 기존 article로 인식하고, 
        # 뒤에 data를 새롭게 들어온 걸로 인식해서 알아서 앞의 article을 뒤에 들어온 data = request.data로 바꿔줌.
        # 이렇게 알아서 수정이 되고, 수정이 되면 나머지는 위의 post와 동일하게 db에 저장해주면 됨.
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            print(serializer.errors) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) # HTTP_200_OK 해도 됨.
