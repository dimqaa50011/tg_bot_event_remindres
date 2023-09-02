from typing import NamedTuple


class DbConfig(NamedTuple):
    SCHEME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @property
    def db_uri(self):
        return "{}://{}:{}@{}:{}/{}".format(
            self.SCHEME,
            self.POSTGRES_USER, self.POSTGRES_PASSWORD,
            self.POSTGRES_HOST, self.POSTGRES_PORT,
            self.POSTGRES_DB
        )
