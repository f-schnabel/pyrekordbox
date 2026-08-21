# Author: Dylan Jones
# Date:   2022-04-10

# mypy: disable-error-code="attr-defined"
from .anlz import (
    AnlzFile as AnlzFile,
    get_anlz_paths as get_anlz_paths,
    read_anlz_files as read_anlz_files,
    walk_anlz_paths as walk_anlz_paths,
)
from .config import get_config as get_config, show_config as show_config, update_config as update_config
from .devicelib_plus import DeviceLibraryPlus as DeviceLibraryPlus
from .logger import logger as logger
from .masterdb import MasterDatabase as MasterDatabase
from .masterdb.database import Rekordbox6Database as Rekordbox6Database
from .mysettings import (
    DevSettingFile as DevSettingFile,
    DjmMySettingFile as DjmMySettingFile,
    MySetting2File as MySetting2File,
    MySettingFile as MySettingFile,
    get_mysetting_paths as get_mysetting_paths,
    read_mysetting_file as read_mysetting_file,
)
from .rbxml import (
    RekordboxXml as RekordboxXml,
    XmlAttributeKeyError as XmlAttributeKeyError,
    XmlDuplicateError as XmlDuplicateError,
)

try:
    from ._version import version as __version__
except ImportError:  # pragma: no cover
    __version__ = "unknown"
