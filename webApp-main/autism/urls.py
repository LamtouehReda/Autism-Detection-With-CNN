from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='autism'
urlpatterns=[
    path('',views.index,name='index'),
]

urlpatterns += staticfiles_urlpatterns()