from typing import List, Any

from aw_core.config import load_config_toml

default_config = """
[aw-qt]
autostart_modules = []
url = 'http://localhost'
port = 5600

[aw-qt-testing]
autostart_modules = []
url = 'http://localhost'
port = 5666
""".strip()


class AwQtSettings:
    def __init__(self, testing: bool):
        """
        An instance of loaded settings, containing a list of modules to autostart.
        Constructor takes a `testing` boolean as an argument
        """
        config = load_config_toml("aw-qt", default_config)
        config_section: Any = config["aw-qt" if not testing else "aw-qt-testing"]

        self.autostart_modules: List[str] = config_section["autostart_modules"]
        self.url: str = config_section["url"]
        self.port: str = config_section["port"]
