"""
WSGI config for workoutProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from django.contrib import admin
from django.urls import path, include
from workout import views
from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    path('', include("workout.urls")),
    path('admin/', admin.site.urls),
]


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workoutProject.settings')

application = get_wsgi_application()
