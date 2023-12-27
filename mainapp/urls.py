from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('haqqımızda',about,name='about'),
    path('portfolio',portfolio,name='portfolio'),
    path('portfolio/<slug>',portfolioSingle,name='portfolioSingle'),
    path('blog/<slug>',blogSingle,name='blogSingle'),
    path('xidmetler',services,name='services'),
    path('xidmetler/<slug>',serviceSingle,name='serviceSingle'),
    path('bloqlar',blogs,name='blogs'),
    path('bloqlar/<slug>',blogSingle,name='blogSingle'),
    path('elaqe',contact,name='contact'),
    path('message',message,name='message'),
]