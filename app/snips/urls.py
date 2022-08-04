from . import views
from django.urls import re_path
# urls.py
from django.urls import path

from .views import redirect_view

urlpatterns = [ path('/redirect/', redirect_view),re_path(r'^home$', views.home, name='home'), re_path(r'^fight_stage$', views.fight_stage, name='fight_stage')]