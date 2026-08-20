# Author: Dylan Jones
# Date:   2022-05-07

from ..utils import warn_deprecated as _warn_deprecated
from .database import Rekordbox6Database
from .smartlist import SmartList
from .tables import (
    AgentRegistry,
    CloudAgentRegistry,
    ContentActiveCensor,
    ContentCue,
    ContentFile,
    DjmdActiveCensor,
    DjmdAlbum,
    DjmdArtist,
    DjmdCategory,
    DjmdColor,
    DjmdContent,
    DjmdCue,
    DjmdDevice,
    DjmdGenre,
    DjmdHistory,
    DjmdHotCueBanklist,
    DjmdKey,
    DjmdLabel,
    DjmdMenuItems,
    DjmdMixerParam,
    DjmdMyTag,
    DjmdPlaylist,
    DjmdProperty,
    DjmdRelatedTracks,
    DjmdSampler,
    DjmdSongHistory,
    DjmdSongHotCueBanklist,
    DjmdSongMyTag,
    DjmdSongPlaylist,
    DjmdSongRelatedTracks,
    DjmdSongSampler,
    DjmdSongTagList,
    DjmdSort,
    HotCueBanklistCue,
    ImageFile,
    SettingFile,
    UuidIDMap,
)

_warn_deprecated(
    "pyrekordbox.db6",
    "pyrekordbox.masterdb",
    hint="The db6 package was renamed to masterdb!",
    remove_in="0.6.0",
)
