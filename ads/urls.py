from django.urls import path
from .views import all_ads, new_ad


urlpatterns = [
    path('', all_ads, name="all_ads"),
    path('new/', new_ad, name="new_ad")
]