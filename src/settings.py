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