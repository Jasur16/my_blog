from django.urls import path
from .views import BlogsView, BlogsDetailView

urlpatterns = [
    path('', BlogsView.as_view(), name='blogs'),
    path('<int:pk>/', BlogsDetailView.as_view(), name='blog_detail')
]