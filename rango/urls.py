from django.conf.urls import patterns, url
from rango import views
from django.conf import settings # 5.3
from django.conf.urls.static import static # 5.3

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about ,name='name'))

		

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
		
		
		