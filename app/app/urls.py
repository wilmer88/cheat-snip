"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from importlib.resources import path
from django.urls import re_path, include
from django.contrib import admin
# from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include('snips.urls')),
    # path("edit/<int:id>",views.edit)
]

# from django.urls import re_path
# #the $ sign besides home restrict the path from having home plus characters and still hit the home path
# urlpatterns = [
#  re_path(r'^index$', views.index, name='index'),
#  re_path(r'^fight_stage$', views.fight_stage, name='fight_stage')
#  ]
