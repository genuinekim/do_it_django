from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()), #CBV
    # path('', views.index), #FBV

    path('<int:pk>/', views.PostDetail.as_view()), #CBV
    # path('<int:pk>/', views.single_post_page), #FBV
]