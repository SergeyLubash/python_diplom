from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('core.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('api/goals/', include('goals.urls')),
    path('api/bot/', include('bot.urls')),
]
