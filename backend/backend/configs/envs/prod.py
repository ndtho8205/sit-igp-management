from backend.configs.envs.base import BaseAppConfig


class ProdAppConfig(BaseAppConfig):
    class Config(BaseAppConfig.Config):
        env_file = "prod.env"
