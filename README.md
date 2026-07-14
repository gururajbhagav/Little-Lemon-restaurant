# Little Lemon Backend Capstone Project

A Django REST Framework backend for the Little Lemon restaurant: menu management,
table booking, token-based authentication, and user registration via Djoser.

## Project structure

```
littlelemon/          # Django project (settings, root urls)
restaurant/           # Django app (models, views, serializers, tests)
templates/index.html  # Static HTML home page
```

## Setup instructions

1. Create and activate a virtual environment.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a MySQL database named `littlelemon`, then update the `DATABASES`
   credentials in `littlelemon/settings.py` (USER / PASSWORD) to match your
   local MySQL setup.
4. Run migrations:
   ```
   python manage.py makemigrations restaurant
   python manage.py migrate
   ```
5. Create a superuser (for /admin access):
   ```
   python manage.py createsuperuser
   ```
6. Start the server:
   ```
   python manage.py runserver
   ```

## Readme.txt — API paths for peer testing

```
/
/admin/
/api/menu-items/
/api/menu-items/<id>/
/api/bookings/
/api/bookings/<id>/
/api/api-token-auth/
/auth/users/
/auth/token/login/
/auth/token/logout/
```

## Testing with Insomnia

1. `POST /auth/users/` with `username`, `email`, `password` to register a user.
2. `POST /auth/token/login/` with `username`/`password` to obtain an auth token.
3. On subsequent requests to `/api/menu-items/` or `/api/bookings/`, add header:
   `Authorization: Token <your_token>`
4. GET/POST/PUT/DELETE against `/api/menu-items/` and `/api/bookings/` to
   exercise the full CRUD API.

## Running unit tests

```
python manage.py test restaurant
```
