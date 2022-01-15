from backend.configs.envs.base import BaseAppConfig


class TestAppConfig(BaseAppConfig):
    class Config(BaseAppConfig.Config):
        env_file = "test.env"
