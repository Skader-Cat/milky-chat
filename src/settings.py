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




