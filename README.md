# Contacts API
## Overview
This is a Django-based API for managing contacts with region restrict and google oauth2. This project can be run either with Docker or without it. Follow the instructions below to get started.

### 1. Clone the Repository
Clone the repository from GitHub:

```bash
git clone https://github.com/ImperatorNeron/contacts-api.git
```

### 2. Navigate to the Project Directory
Change the working directory to the project folder:

```bash
cd contacts-api
```

## 3. Create a Virtual Environment

Create a virtual environment using `venv` and activate it:

```bash
python -m venv venv
```

For **Windows**:

```bash
venv\Scripts\activate
```

For **Mac/Linux**:

```bash
source venv/bin/activate
```

## 4. Configure Environment Variables

Create a `.env` file based on the provided `.env.template`:

1. Copy `.env.template` to `.env`. You can left DJANGO_SECRET_KEY and GOOGLE_SCOPE(highly recommend)
   
2. ...

## 5. Running the Application

### Without Docker

1. Install dependencies:

   ```bash
   pip install poetry
   poetry install
   ```

2. Apply migrations to the database:

   ```bash
   python app/manage.py migrate
   ```

3. Start the Django development server:

   ```bash
   python app/manage.py runserver localhost:8000
   ```

4. To run tests, navigate to the `app` directory and run `pytest`:

   ```bash
   cd app
   pytest
   ```

### With Docker

If you prefer to run the project with Docker, follow these steps:

1. Install dependencies (as shown in step 5 above):

   ```bash
   pip install poetry
   poetry install
   ```

2. Run migrations with `scons`:

   ```bash
   scons migrate
   ```

3. Start the Docker containers and check logs:

   ```bash
   scons up && scons logs
   ```

4. Run tests using `scons` if you need:

   ```bash
   scons tests
   ```

## 6. Conclusion

You can now start working with the **contacts-api** project. If you have any questions, feel free to open an issue or contact me.

### Implemented Commands
#### Application

- ```scons up``` - up application
- ```scons logs``` - follow the logs in app container
- ```scons down``` - down application

#### Migrations
- ```scons makemigrations``` - do migrations
- ```scons migrate``` - migrate to db

#### Tests
- ```scons tests``` - run tests

## License
This project is licensed under the MIT License - see the LICENSE file for details.