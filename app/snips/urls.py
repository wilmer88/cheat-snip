from django.urls import re_path
from . import views
#the $ sign besides home restrict the path from having home plus characters and still hit the home path
urlpatterns = [
 re_path(r'^edit/(?P<id>[0-9]+)/$', views.edit, name="edit"),
#  re_path('edit/<int:id>', views.edit, name="edit"),
 re_path(r'^index$', views.index, name='index'),
 re_path(r'^fight_stage$', views.fight_stage, name='fight_stage'),
 re_path(r'^add_snip$', views.add_snip, name="add_snip"),



 ]
# from django.urls import re_path, include
# from django.contrib import admin

# urlpatterns = [
#     re_path(r'^admin/', admin.site.urls),
#     re_path(r'', include('snips.urls')),
# ]