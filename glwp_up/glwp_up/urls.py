from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from uploader import views


urlpatterns = [
    url(r'^uploader/', include('uploader.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, {'template_name': 'uploader/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'uploader/logout.html'},name='logout'),
    url(r'^download/(?P<file_name>.+)$', views.download, name='download'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
