from django.shortcuts import render,redirect
from BACKENDapp.models import categorydb,productdb,contactusdb,gallerydb,cartdb
from FRONTapp.models import weblogindb,reviewdb
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages



# Create your views here.

#-------------------------------------------------------HOME-PAGE------------------------------------------------------------------
def viewhomepage(req):
    data = categorydb.objects.all()
    return render(req,"homepage.html", {'data':data})

#-------------------------------------------------------RENDER-PAGES---------------------------------------------------------------
def viewaboutuspage(req):
    return render(req,"aboutus_page.html")
def viewcontactuspage(req):
    return render(req,"contactus.html")
def viewportfoliopage(req):
    data = gallerydb.objects.all()
    return render(req,"portfolio.html",{'data':data})
def viewservicepage(req):
    return render(req,"service_page.html")
def viewreviewpage(req):
    data=reviewdb.objects.all()
    return render(req,"reviewpage.html", {'data':data})

def savereviewpage(req):
    if req.method == "POST":
     na = req.POST.get('firstname')
     ctry = req.POST.get('contry')
     feed = req.POST.get('subject')
     obj = reviewdb(NAME=na, COUNTRY=ctry, FEEDBACK=feed)
     obj.save()
     return redirect(viewreviewpage)

def deletereview(req, dataid):
    data = reviewdb.objects.get(id=dataid)
    data.delete()
    return redirect(viewreviewpage)


#---------------------------------------------------------DISPLAY-CATEGORY--------------------------------------------------------

def displayproductpage(request,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = productdb.objects.filter(CATEGORY=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(request,"service_page.html",context)
def viewcategorypage(req):
    data = categorydb.objects.all()
    return render(req,"category_page.html",{'data':data})

#--------------------------------------------------------------SINGLE-PRODUCT-----------------------------------------------------


def viewsingleproductpage(req,dataid):
    data = productdb.objects.get(id=dataid)
    return render(req,"single_product.html",{'dat':data})


#-----------------------------------------------------------------CONTACT US----------------------------------------------------

def savecontactuspage(req):
    if req.method == "POST":
        na = req.POST.get('name')
        eml = req.POST.get('email')
        sub = req.POST.get('subject')
        msg = req.POST.get('message')
        obj=contactusdb(NAME=na, EMAIL=eml, SUBJECT=sub, MESSAGE=msg)
        obj.save()
        messages.success(req, " THANK YOU FOR CONTACTING US!  ")
        return redirect(viewcontactuspage)


#------------------------------------------------------------------CART OPERATION------------------------------------------------
def savecartpage(req):
    if req.method == "POST":
        na = req.POST.get('custname')
        pna = req.POST.get('productname')
        cat = req.POST.get('productcat')
        qty = req.POST.get('quantity')
        tprice = req.POST.get('totalprice')
        obj = cartdb(NAME=na, PDCTNAME=pna, CATEGORY=cat, QUANTITY=qty, PRIZE=tprice,)
        obj.save()
        messages.success(req, "ITEM ADDED TO THE CART ")
        return redirect(viewhomepage)
def viewcartpage(req):
    data = cartdb.objects.all()
    return render(req,"cartpage.html",{'data':data})

# ==============================finalcart================================

def viewfinalcartpage(req):
    data = cartdb.objects.all()
    return render(req,"cartfinalpage.html",{'data':data})



def displaycart(req):
    data = cartdb.objects.all()
    return render (req,"displaycartpage.html", {'data':data})





def deletecart(req,dataid):
    data = cartdb.objects.get(id=dataid)
    data.delete()
    return redirect(displaycart)
def deletecartfont(req,dataid):
    data = cartdb.objects.get(id=dataid)
    data.delete()
    messages.error(req, " YOUR ITEM HAS REMOVED  ")
    return redirect(viewfinalcartpage)

def viewcheckout(req):
    data = cartdb.objects.all()
    return render(req,"checkoutpage.html",  {'data':data})

#--------------------------------------------------------------LOGIN-AND-LOGOUT---------------------------------------------------


def webloginpage(req):
    return render(req,"weblogin.html")
def saveloginpage(req):
    if req.method == "POST":
        una = req.POST.get('username')
        eml = req.POST.get('email')
        passrd = req.POST.get('pass')
        cmfpass = req.POST.get('pass1')
        obj = weblogindb(UNAME=una, EMAIL=eml, PASSWRD=passrd,CMFPASSWRD=cmfpass)
        obj.save()
        return redirect(webloginpage)
def custumerlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username1')
        password_r = req.POST.get('password1')

        if weblogindb.objects.filter(UNAME=username_r, PASSWRD=password_r).exists():
            req.session['username1'] = username_r
            req.session['password1'] = password_r
            messages.success(req, "LOGIN SUCCESSFULLY ")
            return redirect(viewhomepage)
        else:
            messages.error(req, "INVALID USER ")
            return render(req,'weblogin.html')

def custumerlogout(req):
    del req.session['username1']
    del req.session['password1']
    messages.success(req, "LOGOUT SUCCESSFULLY ")
    return redirect(webloginpage)