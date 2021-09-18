from django.conf.urls.static import static
from django.urls import path
from persons import views
from person_manager import settings


urlpatterns = [
    path('', views.home_page),
    path('create', views.create_person),
    path('delete/<pk>', views.delete_person),
    path('update/<pk>', views.update_person),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
