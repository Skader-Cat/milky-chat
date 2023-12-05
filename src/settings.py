from sqlalchemy import Enum
from starlette.responses import HTMLResponse

import credits

class BaseSettingsClass:
    @classmethod
    def get_properties(cls):
        return {key.lower(): getattr(cls, key) for key in dir(cls)
                if not key.startswith('__') and hasattr(cls, key)}

class DatabaseSettings(BaseSettingsClass):
    DRIVER = 'postgresql+asyncpg'
    HOST = 'localhost'
    PORT = 5432
    USER = 'postgres'
    PASSWORD = credits.DB_PASSWORD
    DB_NAME = 'postgres'

    @property
    def GET_DB_URL(self):
        return f'{self.DRIVER}://{self.USER}:{self.PASSWORD}@{self.HOST}'

class DevelopmentSettings(BaseSettingsClass):
    DEBUG = True
    RELOAD = True

class AppSettings(BaseSettingsClass):
    TITLE = 'Milky Chat'
    DESCRIPTION = 'Backend чата на FastAPI с использованием WebSockets '
    VERSION = '0.0.1'
    DOCS_URL = '/docs'
    REDOC_URL = '/redoc'
    OPENAPI_URL = '/openapi.json'
    CONTACT = {
        'name': 'Лунь Архипов',
        'url': 'https://vk.com/johnnyfrom602',
        'team': 'MilkHunters'
    }
    LICENSE_INFO = {
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT'
    }
    SERVER_NAME = 'Milky'
    SERVER_HOST = 'localhost'
    SERVER_PORT = 8000

class ValidationError(BaseSettingsClass):
    class ErrorCode(Enum):
        NOT_FOUND = 404
        ALREADY_EXISTS = 409
        BAD_REQUEST = 400
        UNAUTHORIZED = 401
        FORBIDDEN = 403
        NOT_ALLOWED = 405
        NOT_ACCEPTABLE = 406

        INTERNAL_SERVER_ERROR = 500
        NOT_IMPLEMENTED = 501
        BAD_GATEWAY = 502
        SERVICE_UNAVAILABLE = 503
        GATEWAY_TIMEOUT = 504
        HTTP_VERSION_NOT_SUPPORTED = 505

    ERRORS = {
        ErrorCode.NOT_FOUND: 'не найден',
        ErrorCode.ALREADY_EXISTS: 'уже существует',
        ErrorCode.BAD_REQUEST: 'неверный запрос',
        ErrorCode.UNAUTHORIZED: 'не авторизован',
        ErrorCode.FORBIDDEN: 'запрещено',
        ErrorCode.NOT_ALLOWED: 'недопустимо',
        ErrorCode.NOT_ACCEPTABLE: 'неприемлемо',
        ErrorCode.INTERNAL_SERVER_ERROR: 'внутренняя ошибка сервера',
        ErrorCode.NOT_IMPLEMENTED: 'не реализовано',
        ErrorCode.BAD_GATEWAY: 'плохой шлюз',
        ErrorCode.SERVICE_UNAVAILABLE: 'сервис недоступен',
        ErrorCode.GATEWAY_TIMEOUT: 'время ожидания истекло',
        ErrorCode.HTTP_VERSION_NOT_SUPPORTED: 'версия HTTP не поддерживается'
    }

