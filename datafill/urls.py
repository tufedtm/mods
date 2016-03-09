from django.conf.urls import url
from views import fill_magazine, fill_games, fill_patches, fill_demos

urlpatterns = [
    url(r'^magazines/$', fill_magazine),
    url(r'^games/$', fill_games),
    url(r'^patches/$', fill_patches),
    url(r'^demos/$', fill_demos),
]
