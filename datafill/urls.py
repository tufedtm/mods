from django.conf.urls import url
from views import fill_magazine, fill_games

urlpatterns = [
    url(r'^magazines/$', fill_magazine),
    url(r'^games/$', fill_games),
]
