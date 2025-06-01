from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# from django.views.decorators.csrf import csrf_exempt # Use if not handling CSRF via AJAX headers
import json

from .forms import SignupForm
from .models import SignupRequest

# HTML Page Views
def index_view(request):
    """Renders the home page."""
    return render(request, 'japanese_class_app/index.html')

def about_view(request):
    """Renders the about us page."""
    return render(request, 'japanese_class_app/about.html')

def levels_view(request):
    """Renders the class levels page."""
    return render(request, 'japanese_class_app/levels.html')

def level_assessment_view(request):
    """Renders the level assessment guidance page."""
    return render(request, 'japanese_class_app/level_assessment.html')

def signup_page_view(request):
    """Renders the sign-up page with the form."""
    form = SignupForm()
    return render(request, 'japanese_class_app/signup.html', {'form': form})

def contact_view(request):
    """Renders the contact page."""
    return render(request, 'japanese_class_app/contact.html')


# API View for Sign-Up
# @csrf_exempt # Only use csrf_exempt for APIs if you understand the security implications
               # and are using token-based authentication or other CSRF protection mechanisms.
               # For this project, the frontend JS is expected to send the CSRF token.
@require_POST # Ensures this view only accepts POST requests
def api_signup_view(request):
    """Handles the sign-up form submission via API."""
    try:
        # Ensure request content type is application/json
        if request.content_type != 'application/json':
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid content type. Expected application/json.'
            }, status=415)

        data = json.loads(request.body)
        form = SignupForm(data)

        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Sign-up request received! We will contact you shortly.'
            }, status=201)
        else:
            # Convert form.errors to a more easily parsable format if needed,
            # but Django's default is usually fine for JS.
            return JsonResponse({
                'status': 'error',
                'errors': form.errors
            }, status=400)
            
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid JSON data.'
        }, status=400)
    except Exception as e:
        # Log the exception e for debugging
        print(f"Error in api_signup_view: {e}") # Basic logging
        return JsonResponse({
            'status': 'error',
            'message': 'An unexpected error occurred. Please try again later.'
        }, status=500)
