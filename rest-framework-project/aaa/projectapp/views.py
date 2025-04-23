from django.shortcuts import render
from django.views.generic import ListView 
from .models import Post, Ads
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer, AdsSerializer
from rest_framework import viewsets
from .permissions import IsAdminUserOrReadOnly


# Create your views here.
class BookListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = "post"

class AdsListView(ListView):
    model = Ads
    template_name = 'post_list.html'
    context_object_name = "ads"

class AdsApiView(ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

class PostApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AdsPost(ListCreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

class PostCreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class AdsDetail(RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUserOrReadOnly]

