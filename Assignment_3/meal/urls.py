from django.urls import path
from . import views


urlpatterns = [
    path('showitem/',views.show_item, name='showitem'),
    path('aboutus/',views.about_us,name="aboutus"),
    path('buynow/',views.buy_now,name="buynow"),
]
