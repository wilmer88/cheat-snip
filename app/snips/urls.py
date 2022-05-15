from . import views
from django.urls import re_path

urlpatterns = [re_path(r'^home$', views.home, name='home'), re_path(r'^fight_stage$', views.fight_stage, name='fight_stage')]