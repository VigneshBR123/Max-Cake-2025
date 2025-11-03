from django.shortcuts import render, redirect

from django.views import View

from .models import Cakes, WishList, Cart

from .forms import AddCakeForm

from django.db.models import Q

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permission import permission_role

# Create your views here.

# Home Page

# @method_decorator(login_required(login_url='login'), name='dispatch')
class HomeView(View):

    def get(self,request,*args,**kwargs):

        query = request.GET.get('query')

        # cakes = Cakes.objects.all()

        # cakes = Cakes.objects.filter()  #loads all records

        cakes = Cakes.objects.filter(active_status = True)

        wedding_cakes = cakes.filter(categorey__name = 'Wedding Cakes')

        birthday_cakes = cakes.filter(categorey__name = 'Birthday Cakes')

        plum_cakes = cakes.filter(categorey__name = 'Plum Cakes')

        cup_cakes = cakes.filter(categorey__name = 'Cup Cakes')

        data = {
            'page':'home',
            'wedding_cakes': wedding_cakes,
            'birthday_cakes': birthday_cakes,
            'plum_cakes': plum_cakes,
            'cup_cakes': cup_cakes,
        }

        # Fuzzy Search

        if query:

            search_result = cakes.filter(Q(name__icontains = query)|
                                         Q(desciption__icontains = query)|
                                         Q(categorey__name__icontains = query)|
                                         Q(flavour__name__icontains = query)|
                                         Q(shape__name__icontains = query)|
                                         Q(toppings__name__icontains = query)|
                                         Q(weight__value__icontains = query)|
                                         Q(egg_sts__icontains = query))

            data = {
            'page':'home',
            'wedding_cakes': wedding_cakes,
            'birthday_cakes': birthday_cakes,
            'plum_cakes': plum_cakes,
            'cup_cakes': cup_cakes,
            'search_result': search_result,
            'query': query
        }

        return render(request, 'cakes/home.html', context=data)
    
class VisitorsView(View):

    def get(self,request,*args,**kwargs):

        data = {
            'page':'visit_us'
        }

        return render(request, 'cakes/visit_us.html', context=data)
    
class AboutUsView(View):

    def get(self,request,*args,**kwargs):

        data = {
            'page':'about_us'
        }

        return render(request, 'cakes/about_us.html', context=data)
    
@method_decorator(permission_role(roles=['Admin', 'User']), name='dispatch')
class AddCakeView(View):

    form_class = AddCakeForm

    def get(self,request,*args,**kwargs):

        form = self.form_class()

        data = {
            'page':'add_cake',
            'form':form,
        }

        return render(request, 'cakes/add_cake.html', context=data)
    
    def post(self,request,*args,**kwargs):

        ' data from add_cake template '

        # cake_name = request.POST.get('name')
        # cake_desc = request.POST.get('description')
        # cake_photo = request.FILES.get('photo')
        # cake_cate = request.POST.get('category')
        # cake_flavour = request.POST.get('flavour')
        # cake_shape = request.POST.get('shape')
        # cake_weight = request.POST.get('weight')
        # cake_egg_sts = request.POST.get('egg_sts')
        # cake_toppings = request.POST.get('toppings')
        # cake_is_avail = request.POST.get('is_available')
        # cake_price = request.POST.get('price')

        # Cakes.objects.create(
        #     name = cake_name,
        #     desciption = cake_desc,
        #     photo = cake_photo,
        #     categorey = cake_cate,
        #     flavour = cake_flavour,
        #     shape = cake_shape,
        #     weight = cake_weight,
        #     egg_sts = cake_egg_sts,
        #     toppings = cake_toppings,
        #     is_available = cake_is_avail,
        #     price = cake_price
        # )


        ' data from add_cake template using form '

        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect('home')
        
        data = {
            'page':'add_cake',
            'form':form,
        }

        return render(request,'cakes/add_cake.html', context=data)
    
class CakeDetailsView(View):

    def get(self,request,*args,**kwargs):

        # id comes in dictionary from url

        uuid = kwargs.get('uuid')

        cake = Cakes.objects.get(uuid = uuid)

        data = {
            'cake': cake
        }

        return render(request, 'cakes/cake_details.html', context=data)
    
class CakeUpdateView(View):

    form_class = AddCakeForm
    
    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        cake = Cakes.objects.get(uuid=uuid)

        form = self.form_class(instance=cake)

        data = {
            'form':form
        }

        return render(request, 'cakes/update_cake.html', context=data)
    
    def post(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        cake = Cakes.objects.get(uuid=uuid)

        form = self.form_class(request.POST, request.FILES, instance=cake)

        if form.is_valid():

            form.save()

            return redirect('cake_details',uuid=uuid)
        
        data = {
            'form':form
        }
        
        return render(request, 'cakes/update_cake.html', context=data)
    
class CakeDeleteView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        cake = Cakes.objects.get(uuid=uuid)

        cake.active_status = False

        cake.save()

        return redirect('home') 
    

# @method_decorator(permission_role(roles=['User']), name='dispatch')
class WishListView(View):

    def get(self,request,*args,**kwargs):

        wishlist = WishList.objects.filter(user = request.user)

        # wishlist = request.user.wishlist

        print(wishlist)

        data = {
            "wishlist": wishlist
        }

        return render(request, 'cakes/wishlist.html', context=data)


# @method_decorator(permission_role(roles=['User']), name='dispatch')
class AddToWishListView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get("uuid")

        cake = Cakes.objects.get(uuid=uuid)

        wishlist = WishList.objects.get(user = request.user)

        wishlist.cakes.add(cake)

        return redirect('home')


# @method_decorator(permission_role(roles=['User']), name='dispatch')
class RemoveFromWishListView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get("uuid")

        cake = Cakes.objects.get(uuid=uuid)

        wishlist = WishList.objects.get(user = request.user)

        wishlist.cakes.remove(cake)

        if request.GET.get("req") == "wishlist":

            return redirect('cake_wishlist')

        else:

            return redirect('home')