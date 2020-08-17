from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('add/',views.add_test),
    path('edit/', views.edit_test),
    path('del/', views.del_test),
    path('select/', views.select_test),
    path('testApp2/',views.appTest),

]

urlpatterns += staticfiles_urlpatterns()