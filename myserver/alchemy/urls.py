from django.conf.urls import url
from alchemy import views

urlpatterns = [
    url(r'^$', views.Index.as_view()),
]
