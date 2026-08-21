# Author: Dylan Jones
# Date:   2023-02-01

import re
from pathlib import Path

from . import structs as structs
from .file import (
    FILES,
    DevSettingFile as DevSettingFile,
    DjmMySettingFile as DjmMySettingFile,
    MySetting2File as MySetting2File,
    MySettingFile as MySettingFile,
    SettingsFile,
)

RE_MYSETTING = re.compile(".*SETTING[0-9]?.DAT$")


def get_mysetting_paths(root: str | Path, deep: bool = False) -> list[Path]:
    files = list()
    root = Path(root)
    iteator = root.rglob("*") if deep else root.iterdir()
    for path in iteator:
        if path.is_file() and RE_MYSETTING.match(path.name):
            files.append(path)
    return files


def read_mysetting_file(path: str | Path) -> SettingsFile:
    obj = FILES[str(Path(path).name)]
    return obj.parse_file(path)
