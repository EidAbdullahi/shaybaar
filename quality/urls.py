# from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.welcome, name='welcome'),
    path('team/', views.my_photos, name='myPhotos'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('job/', views.job, name='job'),
    path('thank/', views.thank, name='thank'),
    path('application/', views.application, name='application'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)