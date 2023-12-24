from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('haqqımızda',about,name='about'),
    path('portfolio',portfolio,name='portfolio'),
    path('portfolio/<slug>',portfolioSingle,name='portfolioSingle'),
    path('xidmetler',services,name='services'),
    path('xidmetler/<slug>',serviceSingle,name='serviceSingle'),
    path('bloqlar',blogs,name='blogs'),
]