from django.contrib import admin
from .models import Crop, CropProblem


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
	list_display = ('title', 'farmer', 'created_at')


@admin.register(CropProblem)
class CropProblemAdmin(admin.ModelAdmin):
	list_display = ('title', 'farmer', 'created_at')
    
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'created_at')
	readonly_fields = ('created_at',)
