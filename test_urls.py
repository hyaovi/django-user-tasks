"""
URLs for user_tasks test suite.
"""

from django.conf.urls import url
from django.contrib import admin

from user_tasks.urls import urlpatterns

urlpatterns += [url(r'^admin/', admin.site.urls)]
