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