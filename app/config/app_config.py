from typing import NamedTuple

from .db_config import DbConfig


class AppConfig(NamedTuple):
    db_conf: DbConfig
