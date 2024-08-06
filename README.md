# Back-End Developer Test (Python) - CRUD API

This project is a RESTful API for performing CRUD operations on items using Django and Django REST framework.

## Prerequisites

- Python 3.6+
- PostgreSQL (or any other preferred database)
- pip (Python package installer)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/SaputraAfryan/Pari-TechTest.git
   cd Pari-TechTest
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:

   - Ensure PostgreSQL is installed and running.
   - Create a new database:

   ```sql
   CREATE DATABASE mydatabase;
   CREATE USER mydatabaseuser WITH PASSWORD 'mypassword';
   ALTER ROLE mydatabaseuser SET client_encoding TO 'utf8';
   ALTER ROLE mydatabaseuser SET default_transaction_isolation TO 'read committed';
   ALTER ROLE mydatabaseuser SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE mydatabase TO mydatabaseuser;
   ```

   - Update `TechTestProject/settings.py` with your database configuration:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'mydatabase',
           'USER': 'mydatabaseuser',
           'PASSWORD': 'mypassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Run database migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **GET /api/items/**: Retrieve a list of all items.
- **GET /api/items/{id}/**: Retrieve a single item by ID.
- **POST /api/items/**: Create a new item. The request body should contain the item details.
- **PUT /api/items/{id}/**: Update an existing item by ID. The request body should contain the updated item details.
- **DELETE /api/items/{id}/**: Delete an item by ID.

## Documentation

- **Swagger UI**: Navigate to `http://localhost:8000/swagger/` to view the API documentation.

## Error Handling

- Proper error handling is implemented in the views to ensure meaningful error messages are returned.

## Running Tests

- To run tests, use the following command:

  ```bash
  python manage.py test
  ```

## Contributing

- Contributions are welcome. Please fork the repository and submit a pull request.

## License

- This project is licensed under the Apache 2.0 License.
