from .config_loader import load_config


app_conf = load_config()

__all__ = ("app_config",)
