# from home.views import homeone
from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.homeone),
    path('addnum',views.add),
    path('dbitem',views.dbitem),
    path('details/<str:pid>',views.productdetaildisp),
    path('tocart',views.addtocart),
    path('viewcart',views.viewCart),
    
]