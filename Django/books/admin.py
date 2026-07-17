from django.contrib import admin
from .models import Book,Review
# Register your models here.

class ReviewLine(admin,TabularLine):
    model = Review
    extra =1 
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =['title','author','added_by','created_art']
    search_fields=['title','author']
    inlines =[ReviewLine]

    @admin.register(Review)
    class ReviewAdmin(admin.ModelAdmin):
        list_display=['user','book','rating']
        list_filter= ['rating']

        