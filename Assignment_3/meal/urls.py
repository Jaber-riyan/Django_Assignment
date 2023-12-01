from django.urls import path
from . import views


urlpatterns = [
    path('showitem/',views.show_item, name='showitem'),
    path('buynow/',views.buy_now,name="buynow"),
]
