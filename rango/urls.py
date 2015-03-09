from django.conf.urls import patterns, url
from rango import views
from django.conf import settings # 5.3
from django.conf.urls.static import static # 5.3
from registration.backends.simple.views import RegistrationView


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about ,name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
		url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
		url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'), # 7.3.5
		url(r'^restricted/', views.restricted, name='restricted'), #9.6.1
		#url(r'search/', views.search, name = 'search'),
		url(r'^goto/$', views.track_url, name='goto'),
        url(r'^add_profile/', views.register_profile, name='add_profile'),
		)
		
if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
		
		
		