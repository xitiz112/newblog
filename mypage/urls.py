from . import views
from django.urls import path



urlpatterns = [
    path('page/<slug:slug>', views.pageview, name='mypage')
    ]
