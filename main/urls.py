from django.urls import path
from main.views import MainPage, ProjectPage, AboutPage, DetailPost, ContactPage
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', MainPage.as_view(), name='main', ),
    path('post/<int:pk>', DetailPost.as_view(), name='post_detail'),
    path('projects', ProjectPage.as_view(), name='projects'),
    path('about', AboutPage.as_view(), name='about'),
    path('contact', ContactPage.as_view(), name='contact')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
