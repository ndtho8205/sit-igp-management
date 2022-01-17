from backend.configs.envs.dev import DevAppConfig
from backend.configs.envs.base import BaseConfig, AppEnvTypes, BaseAppConfig
from backend.configs.envs.prod import ProdAppConfig
from backend.configs.envs.test import TestAppConfig


def _get_app_config() -> BaseAppConfig:
    environments = {
        AppEnvTypes.PROD: ProdAppConfig,
        AppEnvTypes.DEV: DevAppConfig,
        AppEnvTypes.TEST: TestAppConfig,
    }

    app_env = BaseConfig().APP_ENV
    return environments[app_env]()


app_config = _get_app_config()
