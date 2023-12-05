import credits

class DatabaseSettings:
    DRIVER = 'postgresql+asyncpg'
    HOST = 'localhost'
    PORT = 5432
    USER = 'postgres'
    PASSWORD = credits.DB_PASSWORD
    DB_NAME = 'postgres'

    @property
    def GET_DB_URL(self):
        return f'{self.DRIVER}://{self.USER}:{self.PASSWORD}@{self.HOST}'


class DevelopmentSettings:
    DEBUG = True
    RELOAD = True
    HOST = 'localhost'
    PORT = 8000

class AppSettings:
    TITLE = 'Milky Chat'
    DESCRIPTION = 'Backend чата на FastAPI с использованием WebSockets '
    VERSION = '0.0.1'
    DOCS_URL = '/docs'
    REDOC_URL = '/redoc'
    OPENAPI_URL = '/openapi.json'
    DEFAULT_RESPONSES = {
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"},
    }
    DEFAULT_TAGS = [
        {
            "name": "users",
            "description": "Пользователи. Логика аутентификации и авторизации пользователей.",
        },
        {
            "name": "channels",
            "description": "Беседы (каналы), в которых происходит общение пользователей.",
        },
    ]
    PROJECT_NAME = 'Milky Chat'
    ALLOWED_HOSTS = ['*']
    BACKEND_CORS_ORIGINS = ['*']
    SECRET_KEY = credits.SECRET_KEY
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_SECRET_KEY = credits.ACCESS_TOKEN_SECRET_KEY
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 * 4
    REFRESH_TOKEN_SECRET_KEY = credits.REFRESH_TOKEN_SECRET_KEY
    PASSWORD_RESET_TOKEN_EXPIRE_HOURS = 1
    EMAIL_RESET_TOKEN_EXPIRE_HOURS = 1
    EMAILS_ENABLED = False
    EMAILS_FROM_EMAIL = ''
