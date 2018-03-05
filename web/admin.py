from django.contrib import admin
from web.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(recipe)
admin.site.register(user_recipe)
admin.site.register(tag)
admin.site.register(recipe_tag)
admin.site.register(peymane)
admin.site.register(ingredient)
admin.site.register(recipe_ingredient)