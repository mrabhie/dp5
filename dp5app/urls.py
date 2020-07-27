from django.urls import path
from dp5app import views

app_name="dp5app"

urlpatterns=[
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('fact/<n>',views.fact,name="fact"),
    path('child/',views.child,name="child"),
]