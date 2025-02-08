from django.contrib import admin
from .models import ZodiacSign, Horoscope

class HoroscopeAdmin(admin.ModelAdmin):
    list_display = ('zodiac_sign', 'period', 'date', 'updated_at', 'author', 'lucky_number', 'lucky_color')

admin.site.register(ZodiacSign)
admin.site.register(Horoscope, HoroscopeAdmin)
