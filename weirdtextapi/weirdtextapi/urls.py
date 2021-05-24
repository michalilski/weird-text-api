from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .settings import VERSION_TAG

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{VERSION_TAG}/', include('textprocessing.urls'))
]
