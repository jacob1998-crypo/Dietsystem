def get_recommendations(request):
    user_profile = UserProfile.objects.get(user=request.user)

    # Prepare request parameters
    query_params = {
        'query': 'healthy foods',
        'age': user_profile.age,
        'gender': user_profile.gender,
        'conditions': ','.join([condition.name for condition in user_profile.conditions.all()]),
        'api_key': settings.API_KEY,
    }

    try:
        # Send request to USDA FoodData Central API
        response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search', params=query_params)

        if response.status_code == 200:
            data = response.json()
            categorized_food = process_food_recommendations(data)

            # Render the template with categorized food recommendations
            context = {
                'user_profile': user_profile,
                'categorized_food': categorized_food,
            }
            messages.success(request, 'Food recommendations updated successfully!')
            return render(request, 'userprofile/recommendations.html', context)
        else:
            # Handle API error
            messages.error(request, 'Failed to fetch food recommendations. Please try again later.')
            return redirect('recommendations')
    except Exception as e:
        # Handle any other exceptions
        messages.error(request, f'An error occurred: {e}')
        return redirect('recommendations')

def process_food_recommendations(data):
    categorized_food = {'vegetables': [], 'vitamins': [], 'proteins': [], 'others': []}

    if 'foods' in data:
        for food in data['foods']:
            description = food.get('description', '').lower()

            if 'vegetable' in description:
                categorized_food['vegetables'].append(food)
            elif 'vitamin' in description:
                categorized_food['vitamins'].append(food)
            elif 'protein' in description:
                categorized_food['proteins'].append(food)
            else:
                categorized_food['others'].append(food)

    return categorized_food