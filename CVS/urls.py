from django.urls import path
from . import views
from Tawassam.settings import DEBUG, STATIC_URL,  MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),

    #Cardio_micro
    path('Microbiology/', views.micro, name="micro"),
    path('Microbiology/<int:set_id>', views.micro_show, name="micro_show"),
    path('Microbiology/upload', views.upload, name="micro_upload"),
    path('Microbiology/<int:set_id>/update/', views.micro_update, name="micro_update"),
    path('Microbiology/<int:set_id>/delete/', views.micro_delete, name="micro_delete"),
]

#DataFlair
if DEBUG:
    # urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
