from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.snippet_list, name='snippets'),
    path('snippets/<pk>', views.snippet_detail, name='snippets'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
'''
urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
'''