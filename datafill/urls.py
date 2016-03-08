from django.conf.urls import url
from views import fill_magazine, fill_games, fill_patches

urlpatterns = [
    url(r'^magazines/$', fill_magazine),
    url(r'^games/$', fill_games),
    url(r'^patches/$', fill_patches),
]
