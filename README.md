# E-commerce API

## Installation

To set up this image storage API, follow these steps:

1. Start the application using Docker Compose:

   ```shell
   docker-compose up
   ```

2. Apply database migrations inside the Docker container:

   ```shell
   docker-compose exec -it web bash
   python manage.py migrate
   ```

3. Create a superuser for the application:

   ```shell
   python manage.py createsuperuser
   ```

4. In order to use the API, assign a user tier to the admin user via the admin panel.

## Access URLs

You can access the following URLs for the API:


- Swagger: http://127.0.0.1:8000/
- Register: http://127.0.0.1:8000/auth/register
- Login: http://127.0.0.1:8000/auth/login
- List products: http://127.0.0.1:8000/products
- Create products: http://127.0.0.1:8000/products/create/
- Modify or delete product: http://127.0.0.1:8000/products/modify/{id}
- Detail of the product: http://127.0.0.1:8000/products{id}
- Place order: http://127.0.0.1:8000/orders/create/
- Get Statistics of the most often ordered products: http://127.0.0.1:8000/products/statistics/{start_date:yyyy-mm-dd}/{end_date:yyyy-mm-dd}/{count}
- Admin Panel: http://127.0.0.1:8000/admin








