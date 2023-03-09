from django.urls import path
from FRONTapp import views
urlpatterns =[
    path('viewhomepage/', views.viewhomepage, name="viewhomepage"),
    path('viewaboutuspage/', views.viewaboutuspage, name="viewaboutuspage"),
    path('viewservicepage/', views.viewservicepage, name="viewservicepage"),
    path('viewcontactuspage/', views.viewcontactuspage, name="viewcontactuspage"),
    path('viewportfoliopage/', views.viewportfoliopage, name="viewportfoliopage"),
    path('viewcategorypage/', views.viewcategorypage, name="viewcategorypage"),
    path('displayproductpage/<itemcatg>',views.displayproductpage,name="displayproductpage"),
    path('viewsingleproductpage/<int:dataid>/', views.viewsingleproductpage, name="viewsingleproductpage"),
    path('webloginpage/', views.webloginpage, name="webloginpage"),
    path('saveloginpage/', views.saveloginpage, name="saveloginpage"),
    path('custumerlogin/', views.custumerlogin, name="custumerlogin"),
    path('custumerlogout/', views.custumerlogout, name="custumerlogout"),
    path('savecontactuspage/', views.savecontactuspage, name="savecontactuspage"),


    path('savecartpage/', views.savecartpage, name="savecartpage"),
    path('viewcartpage/', views.viewcartpage, name="viewcartpage"),
path('viewfinalcartpage/', views.viewfinalcartpage, name="viewfinalcartpage"),
    path('displaycart', views.displaycart, name="displaycart"),
    path('deletecart/<int:dataid>/', views.deletecart, name="deletecart"),
    path('deletecartfont/<int:dataid>/', views.deletecartfont, name="deletecartfont"),
    path('viewcheckout/', views.viewcheckout, name="viewcheckout"),
    path('viewreviewpage/', views.viewreviewpage, name="viewreviewpage"),
    path('savereviewpage/', views.savereviewpage, name="savereviewpage"),
    path('deletereview/<int:dataid>/', views.deletereview, name="deletereview")



    ]




