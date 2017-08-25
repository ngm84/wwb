"""
urls.py for SEARCH app of WWB project

"""

from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'upload$', views.upload),
url(r'search_results$', views.search_results),
url(r'export$', views.export)
]