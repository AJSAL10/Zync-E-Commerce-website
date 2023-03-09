from django.urls import path
from BACKENDapp import views
urlpatterns =[


    path('viewindexpage/', views.viewindexpage, name="viewindexpage"),



    path('viewadminpage/', views.viewadminpage, name="viewadminpage"),
    path('saveadminpage/', views.saveadminpage, name="saveadminpage"),
    path('displayadminpage/', views.displayadminpage, name="displayadminpage"),
    path('editadminpage/<int:dataid>/', views.editadminpage, name="editadminpage"),
    path('updateadminpage/<int:dataid>/', views.updateadminpage, name="updateadminpage"),
    path('deleteadminpage/<int:dataid>/', views.deleteadminpage, name="deleteadminpage"),

    path('addcategorypage/', views.addcategorypage, name="addcategorypage"),
    path('savecategorypage/', views.savecategorypage, name="savecategorypage"),
    path('displaycategorypage/', views.displaycategorypage, name="displaycategorypage"),
    path('editcategorypage/<int:dataid>/', views.editcategorypage, name="editcategorypage"),
    path('updatecategory/<int:dataid>/', views.updatecategory, name="updatecategory"),
    path('deletecategorypage/<int:dataid>/', views.deletecategorypage, name="deletecategorypage"),


    path('addproductpage/', views.addproductpage, name="addproductpage"),
    path('saveproductpage/',views.saveproductpage, name="saveproductpage"),
    path('displayproductpage/', views.displayproductpage, name="displayproductpage"),
    path('editproductpage/<int:dataid>/', views.editproductpage, name="editproductpage"),
    path('updateproductpage/<int:dataid>/', views.updateproductpage, name="updateproductpage"),
    path('deleteproductpage/<int:dataid>/', views.deleteproductpage, name="deleteproductpage"),

    path('viewgallerypage/', views.viewgallerypage, name="viewgallerypage"),
    path('savegallerypage/', views.savegallerypage, name="savegallerypage"),
    path('displaygallerypage/', views.displaygallerypage, name="displaygallerypage"),
    path('deletegallerypage/<int:dataid>/', views.deletegallerypage, name="deletegallerypage"),

    path('displaymessagepage/', views.displaymessagepage, name="displaymessagepage"),
    path('deletemessage/<int:dataid>/', views.deletemessage, name="deletemessage"),


    path('viewloginpage/', views.viewloginpage, name="viewloginpage"),
    path('adminloginpage/', views.adminloginpage, name="adminloginpage"),
    path('adminlogout/', views.adminlogout, name="adminlogout")

]

