# userprofile/models.py

from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser


class Condition(models.Model):
    name = models.CharField(max_length=255)

    # Choices for common dietary conditions
    FOOD_ALLERGIES = 'Food Allergies'
    CELIAC_DISEASE = 'Celiac Disease'
    DIABETES = 'Diabetes'
    DIABETES_HYPER = 'Diabetes (Hyperglycemia)'
    DIABETES_HYPO = 'Diabetes (Hypoglycemia)'
    HYPERTENSION = 'Hypertension'
    HYPERLIPIDEMIA = 'Hyperlipidemia'
    OBESITY = 'Obesity'
    GI_DISORDERS = 'Gastrointestinal Disorders'
    HEART_DISEASE = 'Heart Disease'
    KIDNEY_DISEASE = 'Kidney Disease'
    GOUT = 'Gout'
    FOOD_INTOLERANCES = 'Food Intolerances'
    EATING_DISORDERS = 'Eating Disorders'
    MALNUTRITION = 'Malnutrition'
    GESTATIONAL_CONDITIONS = 'Gestational Conditions'
    THYROID_DISORDERS = 'Thyroid Disorders'

CONDITION_CHOICES = [
    (Condition.FOOD_ALLERGIES, 'Food Allergies'),
    (Condition.CELIAC_DISEASE, 'Celiac Disease'),
    (Condition.DIABETES, 'Diabetes'),
    (Condition.DIABETES_HYPER, 'Diabetes (Hyperglycemia)'),
    (Condition.DIABETES_HYPO, 'Diabetes (Hypoglycemia)'),
    (Condition.HYPERTENSION, 'Hypertension'),
    (Condition.HYPERLIPIDEMIA, 'Hyperlipidemia'),
    (Condition.OBESITY, 'Obesity'),
    (Condition.GI_DISORDERS, 'Gastrointestinal Disorders'),
    (Condition.HEART_DISEASE, 'Heart Disease'),
    (Condition.KIDNEY_DISEASE, 'Kidney Disease'),
    (Condition.GOUT, 'Gout'),
    (Condition.FOOD_INTOLERANCES, 'Food Intolerances'),
    (Condition.EATING_DISORDERS, 'Eating Disorders'),
    (Condition.MALNUTRITION, 'Malnutrition'),
    (Condition.GESTATIONAL_CONDITIONS, 'Gestational Conditions'),
    (Condition.THYROID_DISORDERS, 'Thyroid Disorders'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE ,)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male')
    weight_kg = models.FloatField(default=0.0, help_text="Weight in kilograms")
    height_ft = models.FloatField(default=0.0, help_text="Height in feet")
    conditions = models.ManyToManyField(Condition, choices=CONDITION_CHOICES)
    food_recommendations = models.TextField(blank=True, null=True, default='')
    preferences = models.CharField(max_length=100,blank=False)





    def __str__(self):
        return self.user.username



class Meal(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name