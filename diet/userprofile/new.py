
# userprofile/views.py

# ... (other imports)

def generate_meal_plan(request):
    user_profile = UserProfile.objects.get(user=request.user)

    # Implement logic to generate a weekly meal plan based on user profile
    meal_plan = generate_weekly_meal_plan(user_profile)

    # Save the meals in the database
    save_meals_in_database(user_profile, meal_plan)

    context = {
        'user_profile': user_profile,
        'meal_plan': meal_plan,
    }
    return render(request, 'userprofile/weekly_meal_plan.html', context)

def generate_weekly_meal_plan(user_profile):
    # Implement your logic to generate a weekly meal plan
    # This is a sample meal plan; replace it with your actual logic
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meals_per_day = ['Breakfast', 'Lunch', 'Dinner']

    meal_plan = {day: [f'{meal} {day}' for meal in meals_per_day] for day in days_of_week}

    return meal_plan

def save_meals_in_database(user_profile, meal_plan):
    # Save the generated meals in the database
    for day, meals in meal_plan.items():
        for meal_name in meals:
            meal, created = Meal.objects.get_or_create(name=meal_name, category='Custom')
            user_profile.meals.add(meal)

# ... (other views remain the same)



<!-- userprofile/templates/userprofile/weekly_meal_plan.html -->
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <h2>Weekly Meal Plan</h2>
    <p>Here is your personalized weekly meal plan:</p>

    {% if meal_plan %}
        <ul>
            {% for day, meals in meal_plan.items %}
                <li><strong>{{ day }}</strong>:
                    <ul>
                        {% for meal_name in meals %}
                            {% with meal=user_profile.meals.get(name=meal_name) %}
                                <li>{{ meal.name }} - {{ meal.category }}</li>
                            {% endwith %}
                        {% endfor %}
                    </ul>
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No meal plan available.</p>
    {% endif %}
</div>
{% endblock %}





# userprofile/models.py
from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

class Condition(models.Model):
    name = models.CharField(max_length=255)

class Meal(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male')
    weight = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    conditions = models.CharField(max_length=100, null=True, default='')
    food_recommendations = models.TextField(blank=True, null=True, default='')
    bio = models.TextField(blank=True, null=True, default='')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return self.user.username






{% extends 'base.html' %}

{% block content %}
<!-- templates/recommendations.html -->

<!-- templates/recommendations.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Food Recommendations</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Food Recommendations</h1>

    {% if categorized_food %}
        {% for category, foods in categorized_food.items %}
            <h2>{{ category|title }}</h2>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Nutrients</th>
                    </tr>
                </thead>
                <tbody>
                    {% for food in foods %}
                        <tr>
                            <td>{{ food.description }}</td>
                            <td>{{ food.description }}</td>
                            <td>
                                <ul>
                                    {% for nutrient in food.nutrients %}
                                        <li>{{ nutrient.name }}: {{ nutrient.value }} {{ nutrient.unit }}</li>
                                    {% endfor %}
                                </ul>
                            </td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% endfor %}
    {% else %}
        <p>No food recommendations available.</p>
    {% endif %}
</body>
</html>



{% endblock %}