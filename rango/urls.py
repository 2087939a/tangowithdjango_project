from django.conf.urls import patterns, url
from rango import views
from django.conf import settings # 5.3
from django.conf.urls.static import static # 5.3

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about ,name='name'),
        url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
		url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
		url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'), # 7.3.5
		url(r'^register/$', views.register, name='register'), #  9.4.4
		url(r'^login/$', views.user_login, name='login'), #9.5.3
		url(r'^restricted/', views.restricted, name='restricted'), #9.6.1
		url(r'^logout/$', views.user_logout, name='logout'), #9.7
		)

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
		
		
		