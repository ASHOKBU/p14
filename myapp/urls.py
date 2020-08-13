from django.urls import path
app_name="myapp"
from myapp import views

urlpatterns=[
    path('img_upld/', views.img_upld,name="img_upload"),
    path('img_disp/',views.img_disp,name='img_disp'),
]