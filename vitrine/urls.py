from django.urls import path
from. import views

urlpatterns = [
    path("merci",views.merci_site, name='merci-url'),
    path("bmr",views.bmr_site, name='bmr-url'),
    path("",views.accueil_site, name='accueil-url'),
]
