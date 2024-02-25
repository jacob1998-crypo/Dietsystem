from django.contrib import messages
from .models import UserProfile, Condition 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
import requests
from django.conf import settings
import google.generativeai as genai
import json

def dashboard(request):
    return render(request, 'userprofile/dashboard.html')

def update_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            try:
                user_profile.id = int(request.POST.get('id', user_profile.id))
            except (ValueError, TypeError):
                pass
            user_profile.save()
            return redirect('recommendations')
    else:
        form = UserProfileForm(instance=user_profile)
    
    form.fields['conditions'].queryset = Condition.objects.all()
    return render(request, 'userprofile/update_profile.html', {'form': form})

def get_recommendations(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        # Configure the GenAI library with your API key
        genai.configure(api_key=settings.API_KEY)
        generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048
        }
        model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)
        age = user_profile.age
        gender = user_profile.gender
        conditions = user_profile.conditions.all()
        
        # Prepare the prompt with user parameters
        prompt = f"Generate a healthy diet using these parameters: Age {age}, Gender {gender}, Conditions {[condition.name for condition in conditions]}"
        
        # Generate content based on the prompt and user parameters
       

        response = model.generate_content(prompt)
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4))  # Pretty-print JSON data
        else:
            print("Failed to fetch food recommendations. Status code:", response.status_code)


        
        # Extract food recommendations from the response (assuming it's in JSON format)
        food_recommendations = response.json().get('food_recommendations', [])
            
        context = {
            'user_profile': user_profile,
            'food_recommendations': food_recommendations,
        }
        return render(request, 'userprofile/recommendations.html', context)
    except Exception as e:
        messages.error(request, f'An error occurred: {e}')
        return render(request, 'userprofile/recommendations.html', {'error_message': 'Failed to fetch food recommendations. Please try again later.'})
