# Author: Dylan Jones
# Date:   2023-08-13

from pathlib import Path

from ..masterdb.database import MasterDatabase
from ..utils import warn_deprecated

type PathLike = str | Path


class Rekordbox6Database(MasterDatabase):
    def __init__(self, path: PathLike | None = None, db_dir: PathLike = "", key: str = "", unlock: bool = True):
        warn_deprecated(
            "pyrekordbox.db6.Rekordbox6Database",
            "pyrekordbox.masterdb.MasterDatabase",
            hint="The Rekordbox6Database class was renamed to MasterDatabase!",
            remove_in="0.6.0",
        )
        super().__init__(path, db_dir, key, unlock)
