from django.contrib import admin
from . import models
# Register your models here.



@admin.register(models.CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'category', 'image', 'description', 'created_on')



@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("creditcard", 'user', 'content', 'created_on', )


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_name", 'name', 'email',)

admin.site.register(models.Category)
