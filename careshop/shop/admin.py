from django.contrib import admin
from .models import  Shop , Category , Slider


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("kategorismi", "slug", "urun_sayisi")
    prepopulated_fields = {"slug": ("kategorismi",), }

    def urun_sayisi (self , obj):
        return obj.shop_set.count()


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("marka", "urunismi", "fiyat", "isActive","slug","category_list")
    prepopulated_fields = {"slug":("urunismi",),}
    search_fields = ("urunismi", "marka")
    list_filter = ( "marka","isActive")

    def category_list(self , obj):
        html=" "
        for category in obj.kategoriler.all():
            html+=category.kategorismi+ "/"
        return html

admin.site.register(Slider)

