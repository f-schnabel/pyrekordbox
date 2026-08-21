# Author: Dylan Jones
# Date:   2022-05-07

from ..utils import warn_deprecated as _warn_deprecated
from .database import Rekordbox6Database as Rekordbox6Database
from .smartlist import SmartList as SmartList
from .tables import (
    AgentRegistry as AgentRegistry,
    CloudAgentRegistry as CloudAgentRegistry,
    ContentActiveCensor as ContentActiveCensor,
    ContentCue as ContentCue,
    ContentFile as ContentFile,
    DjmdActiveCensor as DjmdActiveCensor,
    DjmdAlbum as DjmdAlbum,
    DjmdArtist as DjmdArtist,
    DjmdCategory as DjmdCategory,
    DjmdColor as DjmdColor,
    DjmdContent as DjmdContent,
    DjmdCue as DjmdCue,
    DjmdDevice as DjmdDevice,
    DjmdGenre as DjmdGenre,
    DjmdHistory as DjmdHistory,
    DjmdHotCueBanklist as DjmdHotCueBanklist,
    DjmdKey as DjmdKey,
    DjmdLabel as DjmdLabel,
    DjmdMenuItems as DjmdMenuItems,
    DjmdMixerParam as DjmdMixerParam,
    DjmdMyTag as DjmdMyTag,
    DjmdPlaylist as DjmdPlaylist,
    DjmdProperty as DjmdProperty,
    DjmdRelatedTracks as DjmdRelatedTracks,
    DjmdSampler as DjmdSampler,
    DjmdSongHistory as DjmdSongHistory,
    DjmdSongHotCueBanklist as DjmdSongHotCueBanklist,
    DjmdSongMyTag as DjmdSongMyTag,
    DjmdSongPlaylist as DjmdSongPlaylist,
    DjmdSongRelatedTracks as DjmdSongRelatedTracks,
    DjmdSongSampler as DjmdSongSampler,
    DjmdSongTagList as DjmdSongTagList,
    DjmdSort as DjmdSort,
    HotCueBanklistCue as HotCueBanklistCue,
    ImageFile as ImageFile,
    SettingFile as SettingFile,
    UuidIDMap as UuidIDMap,
)

_warn_deprecated(
    "pyrekordbox.db6",
    "pyrekordbox.masterdb",
    hint="The db6 package was renamed to masterdb!",
    remove_in="0.6.0",
)
