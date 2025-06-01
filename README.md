# Kyoto University Japanese Class - Full-Stack Django Website

## I. Overview

This project is a full-stack web application for a Japanese Language Class offered at Kyoto University (fictional). It allows prospective students to learn about the classes, assess their level, and sign up for a class. The backend is built with Django and uses SQLite for data storage.

The primary goals are:
* To inform prospective students about the Japanese class.
* To provide guidance on selecting the appropriate class level.
* To allow users to submit a request to attend a class via an online form.
* To reflect a professional, welcoming, and culturally aware image.
* To provide a Django admin interface to view sign-up requests.

## II. Technology Stack

*   **Frontend:**
    *   HTML5
    *   CSS3
    *   Vanilla JavaScript (for client-side interactions and API calls)
*   **Backend:**
    *   Python 3.x
    *   Django Web Framework
*   **Database:**
    *   SQLite (via Django ORM)
*   **Others:**
    *   `django-cors-headers` for Cross-Origin Resource Sharing.

## III. Project File Structure

```text
/kyoto_japanese_class_website_django  <- Project Root (where you run the script from, if PROJECT_ROOT=".")
├── manage.py                          
├── kyoto_class_project/               
│   ├── __init__.py
│   ├── settings.py                    
│   ├── urls.py                        
│   ├── wsgi.py
│   └── asgi.py
├── japanese_class_app/                
│   ├── __init__.py
│   ├── admin.py                       
│   ├── apps.py
│   ├── migrations/                    
│   │   └── __init__.py
│   ├── models.py                      
│   ├── forms.py                       
│   ├── tests.py                       
│   ├── urls.py                        
│   ├── views.py                       
│   └── templates/
│       └── japanese_class_app/        
│           ├── index.html
│           ├── about.html
│           ├── levels.html
│           ├── level_assessment.html
│           ├── signup.html
│           ├── contact.html
│           └── layout.html            
│   └── static/
│       └── japanese_class_app/        
│           ├── css/
│           │   └── style.css
│           ├── js/
│           │   └── main.js
│           └── images/                
├── requirements.txt                   
└── README.md                          
```

## IV. Prerequisites

*   Python 3.8 or newer
*   `pip` (Python package installer)
*   A virtual environment tool (e.g., `venv`, `virtualenv`) is highly recommended.

## V. Setup Instructions

1.  **Create Project Directory Structure:**
    Use the `mkdir -p ...` command provided earlier, or let a script (like the Python one discussed) create directories if it's designed to do so.
    ```bash
    # Example mkdir command from previous response:
    # mkdir -p kyoto_class_project japanese_class_app/migrations japanese_class_app/templates/japanese_class_app japanese_class_app/static/japanese_class_app/css japanese_class_app/static/japanese_class_app/js japanese_class_app/static/japanese_class_app/images
    # (Ensure you are in the `kyoto_japanese_class_website_django` root when running this specific mkdir)
    ```

2.  **Populate Files:**
    Save the entire content of this AI response (the one you are reading now with all the code blocks) into a single file named `all_project_code.txt` *inside* your `kyoto_japanese_class_website_django` directory.
    Use the Python script (`populate_files.py`, also provided in a previous response) to parse `all_project_code.txt` and create all the individual source files.
    *   Ensure `populate_files.py` is also in the `kyoto_japanese_class_website_django` directory.
    *   Ensure `PROJECT_ROOT = "."` is set in `populate_files.py`.
    *   Run `python populate_files.py` from within the `kyoto_japanese_class_website_django` directory.

3.  **Create and Activate a Virtual Environment:**
    (From within `kyoto_japanese_class_website_django` directory)
    *   On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Apply Database Migrations:**
    The `SignupRequest` model needs its table created in the database.
    ```bash
    python manage.py makemigrations japanese_class_app
    python manage.py migrate
    ```

6.  **Create a Superuser (for Admin Access):**
    This allows you to log into the Django admin panel.
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create a username, email (optional), and password.

## VI. Running the Application

1.  **Start the Django Development Server:**
    ```bash
    python manage.py runserver
    ```

2.  **Access the Application:**
    Open your web browser and go to:
    *   **Main Website:** `http://127.0.0.1:8000/`
    *   **Django Admin Panel:** `http://127.0.0.1:8000/admin/`
        *   Log in with the superuser credentials you created.

## VII. Frontend Overview

*   **HTML Pages:** Located in `japanese_class_app/templates/japanese_class_app/`.
    *   `layout.html`: Base template providing common structure, navigation, and footer.
    *   Other HTML files (`index.html`, `about.html`, etc.) extend `layout.html`.
*   **Static Files:** Located in `japanese_class_app/static/japanese_class_app/`.
    *   `css/style.css`: Main stylesheet for the website.
    *   `js/main.js`: JavaScript for frontend interactions, primarily for handling the sign-up form submission via AJAX.
    *   `images/`: Placeholder for any images used on the site.

## VIII. Backend API Endpoint

*   **Sign-up API:** `POST /api/signup/`
    *   **Request Body (JSON):** Expects a JSON object with fields corresponding to the `SignupForm` (e.g., `full_name`, `email`, `affiliation`, etc.).
    *   **CSRF Token:** The frontend JavaScript must include the `X-CSRFToken` header with the value from the `csrftoken` cookie or form field.
    *   **Responses:**
        *   `201 Created`: On successful sign-up. Returns `{'status': 'success', 'message': '...'}`.
        *   `400 Bad Request`: On validation errors or malformed JSON. Returns `{'status': 'error', 'errors': {...}}` or `{'status': 'error', 'message': '...'}`.
        *   `500 Internal Server Error`: On unexpected server errors.

## IX. Database

*   The application uses **SQLite** as its database, configured by default in `kyoto_class_project/settings.py`.
*   The primary model for storing sign-up information is `SignupRequest`, defined in `japanese_class_app/models.py`. Its fields include user details, affiliation, assessed level, and preferences.

## X. Customization & Next Steps

*   **Content:** Update the placeholder text in HTML templates (`index.html`, `about.html`, etc.) with actual information about the Kyoto University Japanese classes.
*   **Styling:** Modify `japanese_class_app/static/japanese_class_app/css/style.css` to enhance the visual design.
*   **Images:** Add relevant images to `japanese_class_app/static/japanese_class_app/images/` and reference them in templates.
*   **Admin Panel:** Explore the Django admin panel at `/admin/` to view and manage `SignupRequest` entries. You can customize the admin display further in `japanese_class_app/admin.py`.
*   **Error Handling:** Enhance error handling and user feedback in `japanese_class_app/static/japanese_class_app/js/main.js`.
*   **Production Deployment:** For production, configure `DEBUG = False` in `settings.py`, set `ALLOWED_HOSTS`, use a robust database (like PostgreSQL), and deploy using a WSGI server (e.g., Gunicorn) behind a web server (e.g., Nginx).
*   **Further Enhancements:**
    *   Email notifications upon sign-up.
    *   More sophisticated level assessment tools.
    *   User accounts for students.
    *   Class scheduling and management features.
    *   Internationalization (i18n) and Localization (l10n) for multiple languages.