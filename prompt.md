# **Prompt for Gemini: Full-Stack Japanese Class Website with Django Backend (Kyoto University)**

## **I. Project Overview**

You are tasked with generating a **full-stack web application** for a Japanese Class offered at Kyoto University. This application will include:
1.  A **frontend** (user interface) built with HTML, CSS, and JavaScript for informational purposes and user sign-up.
2.  A **backend** built with **Django** (Python) to serve the frontend, handle sign-up form submissions, validate data, and store it using Django's ORM.
3.  A comprehensive **`README.md`** file detailing the project structure, setup, and how to run the entire application.

The website's primary goals are:
* To inform prospective students about the Japanese class.
* To provide guidance on selecting the appropriate class level.
* To allow users to submit a request to attend a class via an online form, with data processed and stored by the Django backend.
* To reflect a professional, welcoming, and culturally aware image.
* To provide an admin interface (Django Admin) to view sign-up requests.

## **II. Technology Stack**

* **Frontend:**
    * HTML5
    * CSS3
    * Vanilla JavaScript (for client-side interactions and API calls)
* **Backend:**
    * Python 3.x
    * **Django** (as the web framework)
* **Database (for sign-ups):**
    * **SQLite** (default for Django, easy setup) using Django's Object-Relational Mapper (ORM).
* **Development Server:** The Django development server (`python manage.py runserver`).

## **III. Project File Structure (Standard Django)**

* Please generate the project with a standard Django structure. Assume the Django project is named `kyoto_class_project` and the primary app handling the Japanese class functionalities is named `japanese_class_app`.



The project is organized as follows:

```text
/kyoto_japanese_class_website_django
├── manage.py                          # Django's command-line utility
├── kyoto_class_project/               # Django project directory
│   ├── __init__.py
│   ├── settings.py                    # Project settings
│   ├── urls.py                        # Project-level URL routing
│   ├── wsgi.py
│   └── asgi.py
├── japanese_class_app/                # Django app directory
│   ├── __init__.py
│   ├── admin.py                       # Admin site configuration
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py                      # Database models (SignupRequest)
│   ├── forms.py                       # Django forms for validation (SignupForm)
│   ├── tests.py
│   ├── urls.py                        # App-level URL routing
│   ├── views.py                       # View functions/classes
│   └── templates/
│       └── japanese_class_app/        # App-specific templates directory
│           ├── index.html
│           ├── about.html
│           ├── levels.html
│           ├── level_assessment.html
│           ├── signup.html
│           ├── contact.html
│           └── layout.html            # Base template
│   └── static/
│       └── japanese_class_app/        # App-specific static files
│           ├── css/
│           │   └── style.css
│           ├── js/
│           │   └── main.js
│           └── images/                # Placeholder for images
├── requirements.txt                   # Python dependencies (Django, django-cors-headers)
└── README.md                          # Project documentation

```
## **IV. Frontend Development (Client-Side)**

**(A) HTML Pages (`japanese_class_app/templates/japanese_class_app/` directory):**
    * All HTML files should be placed in the app's templates directory.
    * **`layout.html` (Base Template):** Should contain the common HTML structure (doctype, head, navigation, footer) that other pages extend using Django's template language (e.g., `{% extends "japanese_class_app/layout.html" %}`, `{% block content %}{% endblock %}`). Include `{% load static %}`.
    * **Navigation Bar:** Consistent across all pages. Links: Home, About Us, Class Levels, Level Assessment, Sign Up, Contact. Use Django's `{% url %}` template tag for URLs.
    * **Footer:** Consistent across pages.
    * **CSRF Token:** In the `signup.html` form, ensure `{% csrf_token %}` is included.

    *(Content for `index.html`, `about.html`, `levels.html`, `level_assessment.html`, `signup.html`, `contact.html` remains largely the same as specified in the previous Flask-based prompt, adapting paths for Django templates and static files. Key changes for `signup.html` are noted below.)*

    **`signup.html` (Sign Up Page - specific adjustments):**
        * Form fields should align with the Django `SignupForm` (see Backend section).
        * Include `{% csrf_token %}` within the `<form>` tags.
        * Feedback Area: An empty `div` (e.g., `<div id="form-feedback"></div>`) to display messages.

**(B) CSS (`japanese_class_app/static/japanese_class_app/css/style.css`):**
    * Single stylesheet, linked via `{% static 'japanese_class_app/css/style.css' %}` in `layout.html`.
    * Design: Clean, modern, professional, welcoming, responsive.

**(C) JavaScript (`japanese_class_app/static/japanese_class_app/js/main.js`):**
    * Linked via `{% static 'japanese_class_app/js/main.js' %}`.
    * **Sign-Up Form Handling (`signup.html`):**
        * Event listener for the sign-up form submission.
        * On submit:
            * Prevent default form submission.
            * Gather data from all form fields.
            * **CSRF Token:** Retrieve the CSRF token value from the form (e.g., `document.querySelector('[name=csrfmiddlewaretoken]').value`).
            * **API Call:** Send the form data as a JSON payload using `fetch` to the backend API endpoint (e.g., `/api/signup/`) via a POST request. Include the CSRF token in the request headers (e.g., `'X-CSRFToken': csrftoken`).
            * **Handle Response:** Display success or error messages from the backend's JSON response in the `#form-feedback` div.

## **V. Backend Development (Server-Side - Django)**

**(A) Project Configuration (`kyoto_class_project/settings.py`):**
    * Add `'japanese_class_app'` to `INSTALLED_APPS`.
    * Add `'corsheaders'` to `INSTALLED_APPS` (for CORS).
    * Add `'corsheaders.middleware.CorsMiddleware'` to `MIDDLEWARE` (preferably high up).
    * Configure `STATIC_URL = '/static/'`. Optionally `STATICFILES_DIRS` if you have project-level static files (though app-specific is fine).
    * Set `CORS_ALLOWED_ORIGINS` or `CORS_ALLOW_ALL_ORIGINS = True` (for development; be more specific in production).

**(B) Project URLs (`kyoto_class_project/urls.py`):**
    * Include URLs from `japanese_class_app`: `path('', include('japanese_class_app.urls'))`.
    * Enable the Django admin: `path('admin/', admin.site.urls)`.

**(C) App Models (`japanese_class_app/models.py`):**
    * Define a `SignupRequest` model:
        ```python
        from django.db import models
        from django.utils import timezone

        class SignupRequest(models.Model):
            full_name = models.CharField(max_length=100)
            email = models.EmailField(unique=True) # Consider if email should be unique
            affiliation_choices = [
                ('student', 'Kyoto University Student'),
                ('staff_researcher', 'Kyoto University Staff/Researcher'),
                ('other', 'Other'),
            ]
            affiliation = models.CharField(max_length=20, choices=affiliation_choices)
            other_affiliation_details = models.CharField(max_length=100, blank=True, null=True)
            self_assessed_level = models.CharField(max_length=50) # Consider choices here too
            preferred_class_level = models.CharField(max_length=50) # Consider choices
            previous_experience = models.TextField(blank=True, null=True)
            learning_goals = models.TextField(blank=True, null=True)
            questions_comments = models.TextField(blank=True, null=True)
            timestamp = models.DateTimeField(default=timezone.now)

            def __str__(self):
                return f"{self.full_name} - {self.email}"
        ```

**(D) App Forms (`japanese_class_app/forms.py`):**
    * Create a `SignupForm` based on the `SignupRequest` model:
        ```python
        from django import forms
        from .models import SignupRequest

        class SignupForm(forms.ModelForm):
            class Meta:
                model = SignupRequest
                fields = [
                    'full_name', 'email', 'affiliation', 'other_affiliation_details',
                    'self_assessed_level', 'preferred_class_level',
                    'previous_experience', 'learning_goals', 'questions_comments'
                ]
            # Add custom validation here if needed beyond model validation
        ```

**(E) App Views (`japanese_class_app/views.py`):**
    * **HTML Page Views:** Create view functions to render each HTML template (e.g., `index`, `about`, `signup_page_view`). For the `signup_page_view`, pass an instance of `SignupForm` to the template context.
    * **API View for Sign-Up (`api_signup_view`):**
        * Decorate with `@csrf_exempt` if not handling CSRF via AJAX headers correctly for simplicity of initial generation, OR ensure frontend JS sends CSRF token. For production, header method is better. For this prompt, assume frontend sends token.
        * Accept `POST` requests.
        * Load request JSON data.
        * Instantiate `SignupForm` with the received data.
        * If `form.is_valid()`:
            * `form.save()` the data.
            * Return `JsonResponse({'status': 'success', 'message': 'Sign-up request received!'}, status=201)`.
        * Else (form is invalid):
            * Return `JsonResponse({'status': 'error', 'errors': form.errors}, status=400)`.
        * Handle potential exceptions with a `500 Internal Server Error` `JsonResponse`.

**(F) App URLs (`japanese_class_app/urls.py`):**
    * Define URL patterns for all views:
        * Paths for each HTML page (e.g., `path('', views.index_view, name='index')`).
        * Path for the API endpoint: `path('api/signup/', views.api_signup_view, name='api_signup')`.

**(G) Admin Configuration (`japanese_class_app/admin.py`):**
    * Register the `SignupRequest` model with the admin site:
        ```python
        from django.contrib import admin
        from .models import SignupRequest

        @admin.register(SignupRequest)
        class SignupRequestAdmin(admin.ModelAdmin):
            list_display = ('full_name', 'e## **IV. Frontend Development (Client-Side)**

**(A) HTML Pages (`japanese_class_app/templates/japanese_class_app/` directory):**
    * All HTML files should be placed in the app's templates directory.
    * **`layout.html` (Base Template):** Should contain the common HTML structure (doctype, head, navigation, footer) that other pages extend using Django's template language (e.g., `{% extends "japanese_class_app/layout.html" %}`, `{% block content %}{% endblock %}`). Include `{% load static %}`.
    * **Navigation Bar:** Consistent across all pages. Links: Home, About Us, Class Levels, Level Assessment, Sign Up, Contact. Use Django's `{% url %}` template tag for URLs.
    * **Footer:** Consistent across pages.
    * **CSRF Token:** In the `signup.html` form, ensure `{% csrf_token %}` is included.

    *(Content for `index.html`, `about.html`, `levels.html`, `level_assessment.html`, `signup.html`, `contact.html` remains largely the same as specified in the previous Flask-based prompt, adapting paths for Django templates and static files. Key changes for `signup.html` are noted below.)*

    **`signup.html` (Sign Up Page - specific adjustments):**
        * Form fields should align with the Django `SignupForm` (see Backend section).
        * Include `{% csrf_token %}` within the `<form>` tags.
        * Feedback Area: An empty `div` (e.g., `<div id="form-feedback"></div>`) to display messages.

**(B) CSS (`japanese_class_app/static/japanese_class_app/css/style.css`):**
    * Single stylesheet, linked via `{% static 'japanese_class_app/css/style.css' %}` in `layout.html`.
    * Design: Clean, modern, professional, welcoming, responsive.

**(C) JavaScript (`japanese_class_app/static/japanese_class_app/js/main.js`):**
    * Linked via `{% static 'japanese_class_app/js/main.js' %}`.
    * **Sign-Up Form Handling (`signup.html`):**
        * Event listener for the sign-up form submission.
        * On submit:
            * Prevent default form submission.
            * Gather data from all form fields.
            * **CSRF Token:** Retrieve the CSRF token value from the form (e.g., `document.querySelector('[name=csrfmiddlewaretoken]').value`).
            * **API Call:** Send the form data as a JSON payload using `fetch` to the backend API endpoint (e.g., `/api/signup/`) via a POST request. Include the CSRF token in the request headers (e.g., `'X-CSRFToken': csrftoken`).
            * **Handle Response:** Display success or error messages from the backend's JSON response in the `#form-feedback` div.

## **V. Backend Development (Server-Side - Django)**

**(A) Project Configuration (`kyoto_class_project/settings.py`):**
    * Add `'japanese_class_app'` to `INSTALLED_APPS`.
    * Add `'corsheaders'` to `INSTALLED_APPS` (for CORS).
    * Add `'corsheaders.middleware.CorsMiddleware'` to `MIDDLEWARE` (preferably high up).
    * Configure `STATIC_URL = '/static/'`. Optionally `STATICFILES_DIRS` if you have project-level static files (though app-specific is fine).
    * Set `CORS_ALLOWED_ORIGINS` or `CORS_ALLOW_ALL_ORIGINS = True` (for development; be more specific in production).

**(B) Project URLs (`kyoto_class_project/urls.py`):**
    * Include URLs from `japanese_class_app`: `path('', include('japanese_class_app.urls'))`.
    * Enable the Django admin: `path('admin/', admin.site.urls)`.

**(C) App Models (`japanese_class_app/models.py`):**
    * Define a `SignupRequest` model:
        ```python
        from django.db import models
        from django.utils import timezone

        class SignupRequest(models.Model):
            full_name = models.CharField(max_length=100)
            email = models.EmailField(unique=True) # Consider if email should be unique
            affiliation_choices = [
                ('student', 'Kyoto University Student'),
                ('staff_researcher', 'Kyoto University Staff/Researcher'),
                ('other', 'Other'),
            ]
            affiliation = models.CharField(max_length=20, choices=affiliation_choices)
            other_affiliation_details = models.CharField(max_length=100, blank=True, null=True)
            self_assessed_level = models.CharField(max_length=50) # Consider choices here too
            preferred_class_level = models.CharField(max_length=50) # Consider choices
            previous_experience = models.TextField(blank=True, null=True)
            learning_goals = models.TextField(blank=True, null=True)
            questions_comments = models.TextField(blank=True, null=True)
            timestamp = models.DateTimeField(default=timezone.now)

            def __str__(self):
                return f"{self.full_name} - {self.email}"
        ```

**(D) App Forms (`japanese_class_app/forms.py`):**
    * Create a `SignupForm` based on the `SignupRequest` model:
        ```python
        from django import forms
        from .models import SignupRequest

        class SignupForm(forms.ModelForm):
            class Meta:
                model = SignupRequest
                fields = [
                    'full_name', 'email', 'affiliation', 'other_affiliation_details',
                    'self_assessed_level', 'preferred_class_level',
                    'previous_experience', 'learning_goals', 'questions_comments'
                ]
            # Add custom validation here if needed beyond model validation
        ```

**(E) App Views (`japanese_class_app/views.py`):**
    * **HTML Page Views:** Create view functions to render each HTML template (e.g., `index`, `about`, `signup_page_view`). For the `signup_page_view`, pass an instance of `SignupForm` to the template context.
    * **API View for Sign-Up (`api_signup_view`):**
        * Decorate with `@csrf_exempt` if not handling CSRF via AJAX headers correctly for simplicity of initial generation, OR ensure frontend JS sends CSRF token. For production, header method is better. For this prompt, assume frontend sends token.
        * Accept `POST` requests.
        * Load request JSON data.
        * Instantiate `SignupForm` with the received data.
        * If `form.is_valid()`:
            * `form.save()` the data.
            * Return `JsonResponse({'status': 'success', 'message': 'Sign-up request received!'}, status=201)`.
        * Else (form is invalid):
            * Return `JsonResponse({'status': 'error', 'errors': form.errors}, status=400)`.
        * Handle potential exceptions with a `500 Internal Server Error` `JsonResponse`.

**(F) App URLs (`japanese_class_app/urls.py`):**
    * Define URL patterns for all views:
        * Paths for each HTML page (e.g., `path('', views.index_view, name='index')`).
        * Path for the API endpoint: `path('api/signup/', views.api_signup_view, name='api_signup')`.

**(G) Admin Configuration (`japanese_class_app/admin.py`):**
    * Register the `SignupRequest` model with the admin site:
        ```python
        from django.contrib import admin
        from .models import SignupRequest

        @admin.register(SignupRequest)
        class SignupRequestAdmin(admin.ModelAdmin):
            list_display = ('full_name', 'email', 'affiliation', 'preferred_class_level', 'timestamp')
            list_filter = ('affiliation', 'preferred_class_level', 'timestamp')
            search_fields = ('full_name', 'email')
        ```

**(H) Dependencies (`requirements.txt`):**
    * List: `Django`, `django-cors-headers`.

## **VI. README.md File (Unified for Full-Stack Django Project)**

Generate a `README.md` file in the project root. It should cover:
1.  **Project Title:** e.g., "Kyoto University Japanese Class - Full-Stack Django Website"
2.  **Overview:** Brief project description.
3.  **Technology Stack:** List frontend and backend technologies.
4.  **File Structure:** (As detailed in Section III, formatted in Markdown).
5.  **Prerequisites:** Python 3.x, pip.
6.  **Setup Instructions:**
    * Cloning/downloading.
    * Creating a virtual environment.
    * Installing dependencies (`pip install -r requirements.txt`).
    * Running database migrations: `python manage.py makemigrations japanese_class_app`, then `python manage.py migrate`.
    * Creating a superuser for admin access: `python manage.py createsuperuser`.
7.  **Running the Application:**
    * Command to start the Django development server (`python manage.py runserver`).
    * URL for the application (e.g., `http://127.0.0.1:8000/`).
    * URL for Django admin (e.g., `http://127.0.0.1:8000/admin/`).
8.  **Frontend Overview:** Brief description of HTML pages, static files location.
9.  **Backend API Endpoint:** Details for `/api/signup/`.
10. **Database:** Mention SQLite and the `SignupRequest` model.
11. **Customization & Next Steps:** Placeholder content, Django admin usage, potential enhancements.

## **VII. Output Format**

* Provide the complete code for all specified files within the Django project structure.
* Provide the content for `README.md`.
* Ensure code is well-formatted and commented.

## **VIII. Final Check**

Before completing, ensure:
* The Django app serves all HTML pages correctly.
* Frontend JavaScript sends sign-up data (including CSRF token) to the backend API.
* Backend validates data using Django Forms, saves it via the ORM, and returns appropriate JSON responses.
* The `SignupRequest` model is registered and accessible in the Django admin panel.
* CORS is configured.
* The `README.md` is comprehensive for the full-stack Django application.

Please generate the full-stack Django application as described.mail', 'affiliation', 'preferred_class_level', 'timestamp')
            list_filter = ('affiliation', 'preferred_class_level', 'timestamp')
            search_fields = ('full_name', 'email')
        ```

**(H) Dependencies (`requirements.txt`):**
    * List: `Django`, `django-cors-headers`.

## **VI. README.md File (Unified for Full-Stack Django Project)**

Generate a `README.md` file in the project root. It should cover:
1.  **Project Title:** e.g., "Kyoto University Japanese Class - Full-Stack Django Website"
2.  **Overview:** Brief project description.
3.  **Technology Stack:** List frontend and backend technologies.
4.  **File Structure:** (As detailed in Section III, formatted in Markdown).
5.  **Prerequisites:** Python 3.x, pip.
6.  **Setup Instructions:**
    * Cloning/downloading.
    * Creating a virtual environment.
    * Installing dependencies (`pip install -r requirements.txt`).
    * Running database migrations: `python manage.py makemigrations japanese_class_app`, then `python manage.py migrate`.
    * Creating a superuser for admin access: `python manage.py createsuperuser`.
7.  **Running the Application:**
    * Command to start the Django development server (`python manage.py runserver`).
    * URL for the application (e.g., `http://127.0.0.1:8000/`).
    * URL for Django admin (e.g., `http://127.0.0.1:8000/admin/`).
8.  **Frontend Overview:** Brief description of HTML pages, static files location.
9.  **Backend API Endpoint:** Details for `/api/signup/`.
10. **Database:** Mention SQLite and the `SignupRequest` model.
11. **Customization & Next Steps:** Placeholder content, Django admin usage, potential enhancements.

## **VII. Output Format**

* Provide the complete code for all specified files within the Django project structure.
* Provide the content for `README.md`.
* Ensure code is well-formatted and commented.

## **VIII. Final Check**

Before completing, ensure:
* The Django app serves all HTML pages correctly.
* Frontend JavaScript sends sign-up data (including CSRF token) to the backend API.
* Backend validates data using Django Forms, saves it via the ORM, and returns appropriate JSON responses.
* The `SignupRequest` model is registered and accessible in the Django admin panel.
* CORS is configured.
* The `README.md` is comprehensive for the full-stack Django application.

Please generate the full-stack Django application as described.Good luck.