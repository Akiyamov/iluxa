from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^live_idea/$', views.LiveIdeaListView.as_view(), name='living_idea'),
    re_path(r'^dead_idea/$', views.DeadIdeaListView.as_view(), name='dead_idea'),
    re_path(r'^new_idea/$', views.ilaksa_new, name='new_idea'),
]