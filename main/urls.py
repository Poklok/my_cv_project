from django.urls import path
from main.views import MainPage, ProjectPage, AboutPage
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', MainPage.as_view(), name='main',),
    path('projects', ProjectPage.as_view(), name='projects'),
    path('about', AboutPage.as_view(), name='about')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
