# django_auth_app

This documentation provides an overview and instructions for a Django-based authentication system. The application includes features like user registration, login with username or email, password reset, profile management, and authentication-restricted pages.

## Features:
### User registration
- Users can sign up with a username, email and password.
- Validations are implemented for secure password entry.

### Login with username or email
- Users can login with their username or email.
- Password is validated against the database.

### Password reset
- Users can reset their password by clicking on the password reset link in the login page.
- A password reset email is sent to the user's email address.
- The user can then reset their password by clicking on the password reset link in the email.

### Profile management
- Users can update their password.

## Local Setup:

### Installation
1. Clone the repository
    ```
        git clone https://github.com/saumitrapatil/django_auth_app.git
    ```
2. Install dependencies
    ```bash
        pip install -r requirements.txt
    ```
3. Setup the database
    ```bash
        python manage.py makemigrations
        python manage.py migrate
    ```
4. Run the development server
    ```bash
        python manage.py runserver
    ```
5. Access the application
    - Open your browser and navigate to [`http://localhost:8000`](http://localhost:8000)

## Project Structure
```
django_auth_app/
├── auth_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
``` 

## URL Patterns
URL Path | View | Description
--------- | ---- | -----------
`/` | home | Home page.
`/signup` | SignUp | User registration page.
`/login` | Login | Login page (username/email & password).
`/logout` | LogoutView | Logs out the user and redirects to login page.
`/dashboard` | dashboard | Dashboard page for authenticated users.
`/profile` | profile | Displays user profile information.
`/reset-password` | PasswordResetView | Sends password reset email.
`/change-password` | PasswordChangeView | Allows authenticated users to change passwords.
`/password-confirm/<uidb64>/<token>/` | PasswordResetConfirmView | Allows users to confirm password reset.

## Security Notes
- Protect sensitive data (like EMAIL_HOST_PASSWORD) by using environment variables.