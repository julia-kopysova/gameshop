from django.urls import path,include
from . import views as v
from django.views.generic.base import TemplateView
from django.conf import settings
#from cart import views as views_cart
#from checkout import views as views_checkout
from account import views as v_a

urlpatterns = [
    path('', TemplateView.as_view(template_name ="home.html"), name='home'),
    #path('', v.HomeView.as_view(), name='home'),
]
