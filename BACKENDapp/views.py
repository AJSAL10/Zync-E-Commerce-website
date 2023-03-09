from django.shortcuts import render,redirect
from BACKENDapp.models import admindb, categorydb, productdb, gallerydb, contactusdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

#------------------------------------------INDEX-PAGE-----------------------------------------------------
def viewindexpage(req):
    return render(req,"indexpage.html")


#------------------------------------------ADMIN-OPERATIONS-----------------------------------------------------

def viewadminpage(req):
    return render(req,"add_admin.html")
def saveadminpage(req):
    if req.method == "POST":
     na = req.POST.get('name')
     em = req.POST.get('email')
     num = req.POST.get('number')
     uname = req.POST.get('username')
     passwrd = req.POST.get('Password')
     img = req.FILES['image']
     obj = admindb(NAME=na, EMAIL=em, NUMBER=num, USERNAME=uname, PASSWORD=passwrd, IMAGE=img)
     obj.save()
     return redirect(viewadminpage)
def displayadminpage(req):
    data = admindb.objects.all()
    return render(req,"display_adminpage.html", {'data':data})
def editadminpage(req,dataid):
    data = admindb.objects.get(id=dataid)
    return render(req,"edit_adminpage.html",{'data':data})
def updateadminpage(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        num = req.POST.get('number')
        uname = req.POST.get('username')
        passwrd = req.POST.get('Password')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).IMAGE
        admindb.objects.filter(id=dataid).update(NAME=na, EMAIL=em, NUMBER=num, USERNAME=uname, PASSWORD=passwrd, IMAGE=file)
        return redirect(displayadminpage)
def deleteadminpage(req,dataid):
    data = admindb.objects.get(id=dataid)
    data.delete()
    return redirect(displayadminpage)



#------------------------------------------END ADMIN-OPERATIONS-----------------------------------------------------


#------------------------------------------CATEGORY-OPERATIONS-----------------------------------------------------


def addcategorypage(req):
    return render(req,"add_categorypage.html")
def savecategorypage(req):
    if req.method =="POST":
        na = req.POST.get('name')
        dis = req.POST.get('discription')
        img = req.FILES['image']
        obj = categorydb(NAME=na, DISCRIPTION=dis, IMAGE=img)
        obj.save()
        return redirect(addcategorypage)
def displaycategorypage(req):
    data = categorydb.objects.all()
    return render(req, "display_categorypage.html", {'data': data})
def editcategorypage(req,dataid):
    data = categorydb.objects.get(id=dataid)
    return render(req, "edit_categorypage.html", {'data': data})
def updatecategory(req,dataid):
    if req.method =="POST":
        na = req.POST.get('name')
        dis = req.POST.get('discription')
        try:
            img = req.FILES['image']
            fs=FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).IMAGE
        categorydb.objects.filter(id=dataid).update(NAME=na, DISCRIPTION=dis, IMAGE=file)
        return redirect(displaycategorypage)
def deletecategorypage(req,dataid):
    data = categorydb.objects.get(id=dataid)
    data.delete()
    return redirect(displaycategorypage)


#------------------------------------------END CATEGORY-OPERATIONS-----------------------------------------------------



#------------------------------------------PRODUCT-OPERATIONS-----------------------------------------------------


def addproductpage(req):
    data = categorydb.objects.all()
    return render(req,"add_productpage.html",{'data':data})
def saveproductpage(req):
    if req.method == "POST":
        cat = req.POST.get('category')
        na = req.POST.get('name')
        quan = req.POST.get('quantity')
        prz = req.POST.get('prize')
        spec = req.POST.get('specification')
        img = req.FILES['image']
        obj = productdb(NAME=na, CATEGORY=cat, PRIZE=prz, QUANTITY=quan, SPECIFICATION=spec, IMAGE=img)
        obj.save()
        return redirect(addproductpage)
def displayproductpage(req):
    data = productdb.objects.all()
    return render(req,"display_productpage.html", {'data':data})
def editproductpage(req,dataid):
    data = productdb.objects.get(id=dataid)
    da = categorydb.objects.all()
    return render(req,"edit_productpage.html",{'data':data,'da':da})
def updateproductpage(req,dataid):
    cat = req.POST.get('category')
    na = req.POST.get('name')
    quan = req.POST.get('quantity')
    prz = req.POST.get('prize')
    spec = req.POST.get('specification')
    try:
        img = req.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    except MultiValueDictKeyError:
        file = productdb.objects.get(id=dataid).IMAGE
    productdb.objects.filter(id=dataid).update(NAME=na, CATEGORY=cat, PRIZE=prz, QUANTITY=quan, SPECIFICATION=spec, IMAGE=file)
    return redirect(displayproductpage)
def deleteproductpage(req,dataid):
    data = productdb.objects.get(id=dataid)
    data.delete()
    return redirect(displayproductpage)

#------------------------------------------END PRODUCT-OPERATIONS-----------------------------------------------------


#----------------------------------------------IMAGE-UPLOAD------------------------------------------------------------

def viewgallerypage(req):
    return render(req,"add_gallery.html")
def savegallerypage(req):
    if req.method == "POST":
        na = req.POST.get('name')
        img = req.FILES['image']
        obj=gallerydb(NAME=na, IMAGE=img)
        obj.save()
        return redirect(viewgallerypage)
def displaygallerypage(req):
    data = gallerydb.objects.all()
    return render(req,"display_gallery.html",{'data':data})
def deletegallerypage(req,dataid):
    data = gallerydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaygallerypage)

#-----------------------------------------------------------END-IMAGE-UPLOAD--------------------------------------------


#-----------------------------------------------------------DISPLAY-MESSAGE---------------------------------------------

def displaymessagepage(req):
    data = contactusdb.objects.all()
    return render(req,"messagepage.html",{'data':data})

def deletemessage(req,dataid):
    data = contactusdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaymessagepage)






#------------------------------------------LOGIN-AND-LOGOUT-----------------------------------------------------
def viewloginpage(req):
    return render(req,"login_page.html")


def adminloginpage(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if admindb.objects.filter(USERNAME=username_r, PASSWORD=password_r).exists():
            req.session['username'] = username_r
            req.session['password'] = password_r
            messages.success(req, "LOGIN SUCCESSFULLY ")
            return redirect(viewindexpage)
        else:
            messages.error(req, "INVALID USER ")
            return render(req, "login_page.html")


def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "LOGOUT SUCCESSFULLY ")
    return redirect(viewloginpage)




# def adminloginpage(req):
#     if req.method == "POST":
#         username_r = req.POST.get('username')
#         password_r = req.POST.get('password')
#
#         if User.objects.filter(username__contains = username_r).exists():
#             user = authenticate(username = username_r, password=password_r)
#             if user is not None:
#                 login(req,user)
#                 req.session['username']=username_r
#                 req.session['password']=password_r
#                 return redirect(viewindexpage)
#             else:
#                 return redirect(viewloginpage)
#         else:
#             return redirect(viewloginpage)