# drf_auth_task1
A basic django rest framework authentication application, including register, login, update, logout and logout-all methods. Utilized knox for logout functions.


Tech Stack:

Backend: Django with Django REST Framework (DRF)
Database: SQLite, supported by Django
Authentication: Token-based authentication (using DRF's TokenAuthentication) 
Optional: Custom User Model for extended user authentication functionalities

Workflow Overview:

Project Setup: Initialize Django project, install DRF.
User Model: Define or customize user model.
Authentication Views: Implement login, logout, registration views.
Serializers: Develop serializers for data conversion and validation.
URL Configuration: Define URL patterns for views.
Testing: Write unit tests for authentication.
