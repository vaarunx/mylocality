from django import forms
from django.contrib import admin

from easy_maps.widgets import AddressWithMapWidget

from .models import Rental

class FirmAdmin(admin.ModelAdmin):
    class form(forms.ModelForm):
        class Meta:
            widgets = {
                'address': AddressWithMapWidget({'class': 'vTextField'})
            }

admin.site.register(Rental)