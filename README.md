# News Site API

This is a Django-based web application for a news site that allows users to read, 
create, edit, and delete news articles. The project includes a backend built using 
Django REST framework and provides various functionalities such as user 
authentication, news creation, categorization, and filtering.

## Features

- User authentication (registration and login) using JWT (JSON Web Tokens).
- List and detail views for news articles with pagination and category filtering.
- User-specific permissions to create, edit, and delete news articles.
- Categorization of news articles into different categories.
- RESTful API endpoints for news articles and categories.

## Technologies Used

- Django
- Django REST framework
- SQLite (or your preferred database)
- JSON Web Tokens (JWT) for authentication

## Setup Instructions

   ```bash
    git clone https://github.com/ochernyi/news-site.git
    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    pip install -r requirements.txt
   ```

1. Configure your database settings in `settings.py`.
2. Apply database migrations: `python manage.py migrate`
3. Create a superuser for admin access: `python manage.py createsuperuser`
4. Run the development server: `python manage.py runserver`

## API Endpoints

- `/user/token/`: Obtain a JWT token by providing valid credentials.
- `/user/token/refresh/`: Refresh a JWT token to extend the expiration time.
- `/user/register/`: Register new user 
- `/user/me/`: User account
- `/news/news/`: List and create news articles.
- `/news/news/<pk>/`: Retrieve, update, and delete a specific news article.
- `/news/categories/`: List and create news categories.
- `/news/categories/<pk>/`: Retrieve, update, and delete a specific category.

## Documentation Endpoints
- `api/schema/`: The API schema of project.
- `api/doc/swagger/`: Swagger documentation.
- `api/doc/redoc/`: ReDoc documentation.

## Usage

- Access the Django admin panel at `/admin/` to manage users, news articles, and categories.
- Register and log in to access user-specific functionalities.
- Use API endpoints to interact with news articles and categories programmatically.


## Running Tests

To ensure the functionality of the project, you can run the provided test suite. The tests cover various aspects of the application, including user authentication, news articles, categories, and more.

### Prerequisites

Before running the tests, make sure you have the project dependencies installed. You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
