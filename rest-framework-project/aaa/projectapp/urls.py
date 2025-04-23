from django.urls import path
from .views import BookListView, AdsListView, AdsApiView, PostApiView, AdsPost, PostCreate, PostDetail, AdsDetail, PostUpdate

urlpatterns = [
    path('',BookListView.as_view()),
    path('ads',AdsListView.as_view()),
    path('adsapi',AdsApiView.as_view()),
    path('postapi',PostApiView.as_view()),
    path('adspost',AdsPost.as_view()),
    path('postapiview',PostCreate.as_view()),
    path('postdetails/<int:pk>',PostDetail.as_view()),
    path('adsdetails/<int:pk>',AdsDetail.as_view()),
    path('update/<int:pk>',PostUpdate.as_view())
]