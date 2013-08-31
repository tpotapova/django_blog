from django.conf.urls import patterns,url
from django.contrib.auth.views import login,logout
from posts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.detail, name='detail'),
    #url(r'^login/$', login, name='login'),
    #url(r'^logout/$', logout,name='logout'))
    (r'^login/$',  login),
    (r'^logout/$', logout)
    #(r"^add_comment/(\d+)/$", "add_comment"),
) 

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))


