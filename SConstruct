import os

DC = "docker compose"
DL = "docker logs"
EXEC = "docker exec -it"

APP_FILE = "docker_compose/app.yaml"
APP_CONTAINER = "drf-app"

ENV = "--env-file .env"

MAKEMIGRATIONS = "python manage.py makemigrations"
MIGRATE = "python manage.py migrate"


def app(target, source, env):
    command = f"{DC} -f {APP_FILE} {ENV} up --build -d"
    return os.system(command)


def app_logs(target, source, env):
    command = f"{DL} {APP_CONTAINER} -f"
    return os.system(command)


def app_down(target, source, env):
    command = f"{DC} -f {APP_FILE} {ENV} down"
    return os.system(command)


def makemigrations(target, source, env):
    command = f"{EXEC} {APP_CONTAINER} {MAKEMIGRATIONS}"
    return os.system(command)


def migrate(target, source, env):
    command = f"{EXEC} {APP_CONTAINER} {MIGRATE}"
    return os.system(command)


# app
Command("up", [], app)
Command("down", [], app_down)
Command("logs", [], app_logs)

# db
Command("makemigrations", [], makemigrations)
Command("migrate", [], migrate)
