from django.contrib import admin
from django.urls import include, path
#from allauth.account.views import SignupView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('', include('news.urls', namespace='news')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
   # path('accounts/', include('allauth.urls')),
    path('about/', include('about.urls', namespace='about')),
]

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)