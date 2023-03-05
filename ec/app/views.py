from django.db.models import Count
from django.shortcuts import redirect, render
from django.views import View 
from . models import Cart , Product , Customer
from . forms import CustomerProfileForm, CustomerRegistrationForm ,PasswordChangeForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")


class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(categoty=val)
        title =Product.objects.filter(categoty=val).values('title')
        return render(request,"app/category.html",locals())
    
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())
    
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"تم التسجيل بنجاح !")
        else:
            messages.warning(request,"خطا !في ادخال البيانات")    
        return render(request,'app/customerregistration.html',locals())
class profileView(View):
    def get(self,request):
        form= CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    def post(self,request):
        form= CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locaity = form.cleaned_data['locaity']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,locaity=locaity,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"تم حفظ البروفايل")
        else:
            messages.warning(request,"خطا في ادخال البيانات")
        return render(request,'app/profile.html',locals())  

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',locals())  

class updateAddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'app/updateAddress.html',locals())
    def post(self,request,pk):
        form= CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.moblie=form.cleaned_data['moblie']
            add.state=form.cleaned_data['state']
            add.zipcode=form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"تم تعديل البروفايل")
        else:
            messages.warning(request,"خطا في ادخال البيانات")
        return redirect("address")
class passwordChangeView():
    pass