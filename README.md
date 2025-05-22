# Brewery Django API Gateway

A Django REST API gateway for the [Open Brewery DB](https://www.openbrewerydb.org/) API, featuring OpenAPI/Swagger documentation via drf-spectacular.

## Features

- Proxy and validate requests to the Open Brewery DB API
- Query breweries and metadata with flexible filters
- OpenAPI schema and interactive docs (Swagger UI & Redoc)
- CORS support for frontend integration

## Requirements

- Python 3.12+
- Django 5.2.1
- See [`requirements.txt`](requirements.txt) for all dependencies

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/brunellamarzolini/brewery_django.git
   cd brewery_django
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server**

   ```bash
   python manage.py runserver
   ```

## Using with the Frontend

You can use this API gateway together with the [brewery-explorer frontend project](https://github.com/brunellamarzolini/brewery-explorer.git):

1. Clone the frontend repository:
   ```bash
   git clone https://github.com/brunellamarzolini/brewery-explorer.git
   cd brewery-explorer
   ```

2. Install dependencies and start the frontend development server:
   ```bash
   npm install
   npm run dev
   ```

By default, CORS is configured to allow requests from the frontend at `http://localhost:5173`

## API Endpoints

- `/api/breweries/` — List breweries (supports filters)
- `/api/breweries/meta` — Get metadata
- `/api/schema/` — OpenAPI schema (JSON)
- `/api/schema/swagger-ui/` — Swagger UI docs
- `/api/schema/redoc/` — Redoc docs

## Example Query

```http
GET /api/breweries/?by_name=dog&per_page=5&page=1
```

## CORS

CORS is enabled for `http://localhost:5173` by default. Adjust `CORS_ALLOWED_ORIGINS` in [`settings.py`](brewery_django/settings.py) as needed.


**Developed with Django REST Framework and drf-spectacular.**