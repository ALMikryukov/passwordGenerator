from django.urls import path
from .views import  *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', main, name='home'),
    path('test/', test, name='test'),
    path('test_2/', test, name='test'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
