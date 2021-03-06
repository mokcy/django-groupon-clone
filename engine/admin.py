# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Advertiser, ProductCategory, Profile, EmailSubscribe, City, Coupon, Deal

class AdvertiserAdmin(admin.ModelAdmin):
    """admin class"""
    list_display = ('name', 'city', 'phone')
    list_filter = ('city', )
    search_fields = ('name', 'address', 'contact', 'email')
    
class DealAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ( 'title', )
    }
    list_display = ('title', 'advertiser', 'city', 'retail_price', 'deal_price')
    list_filter = ('is_deal_on', 'advertiser', 'city')
    
    date_navigation = 'date_published'

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city')
    list_filter = ('city', 'is_email_sub')

class EmailSubAdmin(admin.ModelAdmin):
    list_display = ('email', 'city')
    list_links = list_display
    list_filter = ('city',)

class CouponAdmin(admin.ModelAdmin):
    list_display = ['user', 'deal', 'status']
    list_filter = ('user', 'deal')
    list_per_page = 100
    search_fields = ['user', 'deal']

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'is_active', 'order')
    list_filter = ('is_active',)
    list_per_page = 100
    search_fields = ('name',)
    prepopulated_fields = {
        'slug': ( 'name', )
    }
    ordering = ('order', 'name')


admin.site.register(ProductCategory)
admin.site.register(Deal, DealAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Advertiser, AdvertiserAdmin)
admin.site.register(EmailSubscribe, EmailSubAdmin)
