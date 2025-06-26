from django.contrib import admin
from .models import Product, Review, Seller, ProductCertificate

class ProductReviewInline(admin.TabularInline):
    model = Review
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ProductReviewInline]

class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('product',)

class ProductCertificateAdmin(admin.ModelAdmin):
    list_display = ('product', 'certificate_number')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(ProductCertificate, ProductCertificateAdmin)