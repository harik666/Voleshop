from . import views
from django.urls import path

app_name = "search"
urlpatterns = [
     path('', views.search_res, name="search_res"),
    # path('<slug:c_slug>/', views.fun_all_cats, name="prod_by_cat"),
    # path('<slug:c_slug>/<slug:p_slug>/', views.fun_prod_detail, name="prod_detail"),

]
