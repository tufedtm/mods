from django.conf.urls import url
from views import fill_magazine

urlpatterns = [
    url(r'^$', fill_magazine),
]
