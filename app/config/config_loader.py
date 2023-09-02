from typing import Optional
from pathlib import Path

from environs import Env

from .db_config import DbConfig
from .app_config import AppConfig


BASE_DIR = Path(__file__).resolve().parent.parent.parent


def load_config(path_to_env_file: Optional[str] = None) -> AppConfig:
    DEFAULT_PATH_TO_ENV_FILE = str(BASE_DIR / ".env")
    path = path_to_env_file if path_to_env_file is not None else DEFAULT_PATH_TO_ENV_FILE

    env = Env()
    env.read_env(path=path)

    SCHEME = env.str("SCHEME")
    POSTGRES_USER = env.str("POSTGRES_USER")
    POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")
    POSTGRES_DB = env.str("POSTGRES_DB")
    POSTGRES_HOST = env.str("POSTGRES_HOST")
    POSTGRES_PORT = env.str("POSTGRES_PORT")

    db_conf = DbConfig(
        POSTGRES_USER=POSTGRES_USER, POSTGRES_PASSWORD=POSTGRES_PASSWORD,
        POSTGRES_HOST=POSTGRES_HOST, POSTGRES_PORT=POSTGRES_PORT,
        POSTGRES_DB=POSTGRES_DB,
        SCHEME=SCHEME
    )

    return AppConfig(
        db_conf=db_conf
    )



