from . import views
from django.urls import path


urlpatterns = [
    path('', views.homepage, name='home'),
    path('post/<int:pk>', views.PostDetail, name='post_detail'),
     path('category/<slug:cat_name>', views.categoryview, name='post_category'),

]