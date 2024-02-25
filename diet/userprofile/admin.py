from django.contrib import admin
from .models import UserProfile,Meal

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','id', 'age', 'gender', 'weight_kg', 'height_ft', 'get_conditions', 'food_recommendations', 'preferences')

    def get_conditions(self, obj):
        return ", ".join([condition.name for condition in obj.conditions.all()])
    get_conditions.short_description = 'Conditions'

admin.site.register(UserProfile, UserProfileAdmin)

class MealAdmin(admin.ModelAdmin):
   
    list_display = ('name','category')

# Register the UserProfile model with the custom admin class
admin.site.register(Meal,MealAdmin)