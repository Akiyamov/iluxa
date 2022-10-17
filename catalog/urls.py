from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^live_idea/$', views.ilaksaListView.as_view(), name='ilaksas'),
    re_path(r'^dead_idea/$', views.ilaksdListView.as_view(), name='ilaksad'),
    re_path(r'^new_idea/$', views.ilaksa_new, name='ilaksa_new'),
]