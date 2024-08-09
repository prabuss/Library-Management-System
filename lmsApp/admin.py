from django.contrib import admin
from .models import Category, SubCategory, Books, Students, Borrow

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('name', 'description')

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'description','date_added')
    list_filter = ('category', 'date_added')
    search_fields = ('name', 'description')

class BooksAdmin(admin.ModelAdmin):
    list_display = ('sub_category', 'isbn', 'title', 'author', 'publisher', 'date_published', 'date_added')
    list_filter = ('sub_category', 'date_added')
    search_fields = ('isbn', 'title', 'author', 'publisher')

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('code', 'first_name', 'middle_name', 'last_name', 'gender', 'contact', 'email', 'address', 'department', 'course', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('code', 'first_name', 'middle_name', 'last_name', 'contact', 'email', 'address')

class BorrowAdmin(admin.ModelAdmin):
    list_display = ('student', 'book', 'borrowing_date', 'return_date', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('student__code', 'book__title')

admin.site.register(Category, CategoryAdmin)

admin.site.register(Books, BooksAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Borrow, BorrowAdmin)