from . import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from post.sitemaps import PostSitemap


sitemaps = {
    "posts": PostSitemap,
}



urlpatterns = [
    path('', views.homepage, name='home'),
    path('post/<int:pk>', views.PostDetail, name='post_detail'),
     path('category/<slug:cat_name>', views.categoryview, name='post_category'),
     path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),

]