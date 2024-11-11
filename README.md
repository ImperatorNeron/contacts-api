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

1. Copy the `.env.template` file to `.env`. You can leave or change the `DJANGO_SECRET_KEY`. `GOOGLE_SCOPE` need to be the same.
   
2. Go to the [Google Cloud Console](https://cloud.google.com/), log in with your Google account, and click **Console**.

3. In the top navigation bar, click **Select/Create Project** and create a new project.

4. Give your project a name.

5. In the left sidebar, click **APIs & Services** -> **OAuth consent screen**.

6. Select **External** and click **Create**.

7. Provide the app name, support email, and add your email to the **Developer contact information** section.

8. Click **Add or Remove Scopes**, then select `userinfo.email` and `userinfo.profile`. Save and continue.

9.  Add a test user email and click **Save and Continue**. Review everything and click **Back to Dashboard**.

10. Go to **Credentials** -> **Create Credentials** -> **OAuth Client ID**.

11. Choose **Web application**, then add the following:
    - **Authorized JavaScript origins**: `http://localhost:8000`
    - **Authorized redirect URIs**: `http://localhost:8000/auth/google/callback/`

12. Copy the **Client ID** and paste it into the `GOOGLE_CLIENT_ID` field in your `.env` file. Similarly, copy the **Client Secret** and paste it into the `GOOGLE_CLIENT_SECRET` field in your `.env` file.

For a quick walkthrough, you can watch the first 2 minutes of this [video](https://www.youtube.com/watch?v=HtJKUQXmtok&ab_channel=CooperCodes). Remember to follow step 11 for the correct redirect URI configuration.



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

2. Start the Docker containers and check logs:

   ```bash
   scons up && scons logs
   ```

3. Run migrations with `scons`:

   ```bash
   scons migrate
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