from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileuploadView.as_view()),
    path('index', views.FileuploadView.as_view(),
        name = 'site_index'),
    path('result', views.ResultView.as_view(),
        name = 'site_result'),
]
