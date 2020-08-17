from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('xueyuan/',views.xueyuan),
    path('zhuanye/', views.zhuanye),
    path('hangye/', views.hangye),
    path('index/', views.index),
    path('index2/', views.index2),
    path('yuce/',views.yuce)

]

urlpatterns += staticfiles_urlpatterns()