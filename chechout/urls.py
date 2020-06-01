from django.urls import path,include
from django.conf.urls.static import static
from . import views as v
from django.conf import settings
from chechout import views as views_checkout

urlpatterns = [
    path('checkout/', views_checkout.create_order, name='checkout'),
    #path('success/', views_checkout.display_info, name='success'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
