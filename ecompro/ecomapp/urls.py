from . import views
from django.urls import path

app_name = "online"
urlpatterns = [
    path('', views.fun_all_cats, name="all_cats"),
    path('<slug:c_slug>/', views.fun_all_cats, name="prod_by_cat"),
    path('<slug:c_slug>/<slug:p_slug>/', views.fun_prod_detail, name="prod_detail"),

]
