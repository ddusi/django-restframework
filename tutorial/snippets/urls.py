from django.urls import path
from . import views

urlpatterns = [
    path('snippets/', views.JSONResponse.snippet_list, name='snippets'),
    path('snippets/<pk>', views.JSONResponse.snippet_detail, name='snippets'),
]

'''
urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
'''