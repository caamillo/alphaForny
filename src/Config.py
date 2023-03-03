import toml

class Config:
    def __init__(self, configPath = './config.toml') -> None:
        with open(configPath) as f:
            config = toml.loads(f.read())
        self.__dict__.update(**config)