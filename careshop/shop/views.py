


from django.shortcuts import get_object_or_404, render, redirect
from .models import  Shop , Category , sepet
from django.core.paginator import Paginator

# Create your views here.



def index(request):
   #list comphension alt satırda yapılan şeyin adı
    urunler = Shop.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

    return render(request, 'shop/index.html' , {
        'categories': kategoriler,
        'urunler' :  urunler
    })
def search(request):
    if "q" in request.GET and request.GET["q"] !="":
        q= request.GET["q"]
        urunler = Shop.objects.filter( isActive=True,urunismi__contains=q).order_by("marka")
        kategoriler = Category.objects.all()
    else:
        return redirect("")
    paginator = Paginator(urunler, 12)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'shop/list.html', {
        'categories': kategoriler,
        'page_obj': page_obj,


    })

def favori(request):
   #list comphension alt satırda yapılan şeyin adı
    urunler = Shop.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

    return render(request, 'shop/index.html' , {
        'categories': kategoriler,
        'urunler' :  urunler
    })
def sepet(request):
  if request.method=="POST":
     sepet.marka=Shop.marka
     print(sepet.marka)
  return render(request, "shop/sepet.html")
def detaylar(request , slug):
    shop = get_object_or_404(Shop , slug=slug)
    context = {
        'urun': shop
    }
    return render(request, 'shop/detaylar.html', context)

def getShopByCategory(request , slug):
    urunler = Shop.objects.filter(kategoriler__slug = slug, isActive=True).order_by("marka")
    kategoriler= Category.objects.all()

    paginator = Paginator(urunler , 12)
    page= request.GET.get('page',1)
    page_obj = paginator.page(page)




    return render(request,'shop/index.html',{
        'categories': kategoriler,
        'page_obj': page_obj,
        'seciliKategori': slug

    })
