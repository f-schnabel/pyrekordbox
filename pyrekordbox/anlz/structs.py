# Author: Dylan Jones
# Date:   2022-10-24

"""Binary structures of Rekordbox ANLZ-files.

References
----------
.. [1] Rekordbox Export Structure Analysis: Analysis Files,
   https://djl-analysis.deepsymmetry.org/rekordbox-export-analysis/anlz.html
"""

from dataclasses import dataclass
from typing import Any

from construct import (
    Array,
    Bytes,
    Const,
    Container,
    Default,
    Enum,
    Int8ub,
    Int16ub,
    Int32sb,
    Int32ub,
    PaddedString,
    Padding,
    Struct,
    Switch,
    this,
)
from construct_typed import DataclassMixin, DataclassStruct, csfield, csfield_const, csfield_noinit

# -- Beat Grid Tag (PQTZ) --------------------------------------------------------------

AnlzQuantizeTick = Struct(
    "beat" / Int16ub,
    "tempo" / Int16ub,
    "time" / Int32ub,  # in ms from start
)


@dataclass
class PQTZContent(DataclassMixin):
    _padding: None = csfield_noinit(Padding(4))
    u2: int = csfield_const(Int32ub, 0x80000)
    entry_count: int = csfield(Int32ub)
    entries: list[Container[Any]] = csfield(Array(this.entry_count, AnlzQuantizeTick))


# len_header: 24
PQTZ = DataclassStruct(PQTZContent)


# Extended Beat Grid Tag (PQT2)

AnlzQuantizeTick2 = Struct(
    "beat" / Int8ub,  # 1 byte
    "unkown" / Int8ub,  # 1 byte
)


@dataclass
class PQT2Content(DataclassMixin):
    _padding1: None = csfield_noinit(Padding(4))
    u1: int = csfield(Int32ub)
    _padding2: None = csfield_noinit(Padding(4))
    bpm: list[Container[Any]] = csfield(Array(2, AnlzQuantizeTick))
    entry_count: int = csfield(Int32ub)
    u3: int = csfield(Int32ub)
    u4: int = csfield(Int32ub)
    u5: int = csfield(Int32ub)
    entries: list[Container[Any]] = csfield(Array(this.entry_count, AnlzQuantizeTick2))


# len_header: 56
PQT2 = DataclassStruct(PQT2Content)


# -- Cue List Tag (PCOB) ---------------------------------------------------------------

AnlzCuePointType = Enum(Int8ub, single=1, loop=2)

AnlzCuePointStatus = Enum(Int32ub, disabled=0, enabled=4)

AnlzTagCueObjectType = Enum(Int32ub, memory=0, hotcue=1)

AnlzCuePoint = Struct(
    "type" / Const("PCPT", PaddedString(4, encoding="ascii")),
    "len_header" / Int32ub,
    "len_entry" / Int32ub,
    "hot_cue" / Int32ub,  # 0 for memory
    "status" / AnlzCuePointStatus,
    "u1" / Const(0x10000, Int32ub),
    "order_first" / Int16ub,  # 0xffff for first cue, 0,1,3 for next
    "order_last" / Int16ub,  # 1,2,3 for first, second, third cue, 0xffff for last
    "type" / AnlzCuePointType,
    Padding(1),
    "u2" / Const(1000, Int16ub),
    "time" / Int32ub,
    "loop_time" / Default(Int32ub, -1),
    Padding(16),
)


@dataclass
class PCOBContent(DataclassMixin):
    cue_type: int | str = csfield(AnlzTagCueObjectType)
    unk: int = csfield(Int16ub)
    count: int = csfield(Int16ub)
    memory_count: int = csfield(Int32sb)
    entries: list[Container[Any]] = csfield(Array(this.count, AnlzCuePoint))


# len_header: 24
PCOB = DataclassStruct(PCOBContent)


# Extended (nxs2) Cue List Tag (PCO2)

AnlzCuePoint2 = Struct(
    "type" / Const("PCP2", PaddedString(4, encoding="ascii")),
    "len_header" / Int32ub,
    "len_entry" / Int32ub,
    "hot_cue" / Int32ub,  # 0 for memory
    "type" / Int8ub,  # spotted: 0x010003e8 0x020003e8
    Padding(3),
    "time" / Int32ub,
    "loop_time" / Default(Int32ub, -1),
    "color_id" / Int8ub,
    Padding(7),
    "loop_enumerator" / Int16ub,
    "loop_denominator" / Int16ub,
    "len_comment" / Int32ub,
    "comment" / PaddedString(this.len_comment, encoding="utf-16-be"),
    "color_code" / Int8ub,
    "color_red" / Int8ub,
    "color_green" / Int8ub,
    "color_blue" / Int8ub,
    Padding(this.len_entry - 48 - this.len_comment),
)


@dataclass
class PCO2Content(DataclassMixin):
    type: int | str = csfield(AnlzTagCueObjectType)
    count: int = csfield(Int16ub)
    unknown: int = csfield(Int16ub)
    entries: list[Container[Any]] = csfield(Array(this.count, AnlzCuePoint2))


# len_header: 20
PCO2 = DataclassStruct(PCO2Content)


# -- Path Tag (PPTH) -------------------------------------------------------------------


@dataclass
class PPTHContent(DataclassMixin):
    len_path: int = csfield(Int32ub)
    path: str = csfield(PaddedString(this.len_path - 2, encoding="utf-16-be"))
    _padding: None = csfield_noinit(Padding(2))


# len_header: 16
PPTH = DataclassStruct(PPTHContent)


# -- VBR Tag (PVBR) --------------------------------------------------------------------


@dataclass
class PVBRContent(DataclassMixin):
    u1: int = csfield(Int32ub)
    idx: list[int] = csfield(Array(400, Int32ub))
    u2: int = csfield(Int32ub)


# len_header: 16
PVBR = DataclassStruct(PVBRContent)


@dataclass
class PVDIContent(DataclassMixin):
    u1: int = csfield(Int32ub)
    u2: int = csfield(Int32ub)
    len_confidence: int = csfield(Int32ub)
    confidence: bytes = csfield(Bytes(this.len_confidence))


# len_header: 24
PVDI = DataclassStruct(PVDIContent)


@dataclass
class PVB2Content(DataclassMixin):
    u1: int = csfield(Int32ub)
    u2: int = csfield(Int32ub)
    u3: int = csfield(Int32ub)
    entry_count: int = csfield(Int32ub)
    entry_size: int = csfield(Int32ub)
    entries: list[bytes] = csfield(Array(this.entry_count, Bytes(this.entry_size)))


# len_header: 32
PVB2 = DataclassStruct(PVB2Content)


# -- (Tiny) Waveform Preview Tag (PWAV / PWV2) -----------------------------------------


@dataclass
class WaveformPreviewContent(DataclassMixin):
    len_preview: int = csfield(Int32ub)
    unknown: int = csfield_const(Int32ub, 0x10000)
    entries: list[int] = csfield(Array(this.len_preview, Int8ub))


# len_header: 20
PWAV = DataclassStruct(WaveformPreviewContent)

# len_header: 20
PWV2 = DataclassStruct(WaveformPreviewContent)


# -- Waveform Detail Tag (PWV3) --------------------------------------------------------


@dataclass
class PWV3Content(DataclassMixin):
    len_entry_bytes: int = csfield_const(Int32ub, 1)
    len_entries: int = csfield(Int32ub)
    u1: int = csfield_const(Int32ub, 0x00960000)
    entries: list[int] = csfield(Array(this.len_entries, Int8ub))


# len_header: 24
PWV3 = DataclassStruct(PWV3Content)


# -- Waveform Color Preview Tag (PWV4) -------------------------------------------------


@dataclass
class PWV4Content(DataclassMixin):
    len_entry_bytes: int = csfield_const(Int32ub, 6)
    len_entries: int = csfield(Int32ub)
    unknown: int = csfield(Int32ub)
    entries: bytes = csfield(Bytes(this.len_entry_bytes * this.len_entries))


# len_header: 24
PWV4 = DataclassStruct(PWV4Content)


# -- Waveform Color Detail Tag (PWV5) --------------------------------------------------


@dataclass
class PWV5Content(DataclassMixin):
    len_entry_bytes: int = csfield_const(Int32ub, 2)
    len_entries: int = csfield(Int32ub)
    unknown: int = csfield(Int32ub)
    entries: list[int] = csfield(Array(this.len_entries, Int16ub))


# len_header: 24
PWV5 = DataclassStruct(PWV5Content)

# -- Song Structure Tag (PSSI) ---------------------------------------------------------

SongStructureEntry = Struct(
    "index" / Int16ub,
    "beat" / Int16ub,
    "kind" / Int16ub,
    "u1" / Int8ub,
    "k1" / Int8ub,
    "u2" / Int8ub,
    "k2" / Int8ub,
    "u3" / Int8ub,
    "b" / Int8ub,
    "beat_2" / Int16ub,
    "beat_3" / Int16ub,
    "beat_4" / Int16ub,
    "u4" / Int8ub,
    "k3" / Int8ub,
    "u5" / Int8ub,
    "fill" / Int8ub,
    "beat_fill" / Int16ub,
)


@dataclass
class PSSIContent(DataclassMixin):
    len_entry_bytes: int = csfield_const(Int32ub, 24)
    len_entries: int = csfield(Int16ub)
    mood: int = csfield(Int16ub)
    u1: bytes = csfield(Bytes(6))
    end_beat: int = csfield(Int16ub)
    u2: bytes = csfield(Bytes(2))
    bank: int = csfield(Int8ub)
    u3: bytes = csfield(Bytes(1))
    entries: list[Container[Any]] = csfield(Array(this.len_entries, SongStructureEntry))


# len_header: 32
PSSI = DataclassStruct(PSSIContent)

# -- PWV6 ------------------------------------------------------------------------------


@dataclass
class PWV6Content(DataclassMixin):
    len_entry_bytes: int = csfield_const(Int32ub, 3)
    len_entries: int = csfield(Int32ub)
    entries: bytes = csfield(Bytes(this.len_entry_bytes * this.len_entries))


# len_header: 20
PWV6 = DataclassStruct(PWV6Content)

# -- PWV7 ------------------------------------------------------------------------------


@dataclass
class PWV7Content(DataclassMixin):
    len_entry_bytes: int = csfield_const(Int32ub, 3)
    len_entries: int = csfield(Int32ub)
    unknown: int = csfield_const(Int32ub, 0x00960000)
    entries: bytes = csfield(Bytes(this.len_entry_bytes * this.len_entries))


# len_header: 24
PWV7 = DataclassStruct(PWV7Content)

# -- PWVC ------------------------------------------------------------------------------


@dataclass
class PWVCContent(DataclassMixin):
    unknown: int = csfield(Int16ub)
    data: list[int] = csfield(Array(3, Int16ub))


# len_header: 14
PWVC = DataclassStruct(PWVCContent)


# -- Main Items ------------------------------------------------------------------------


@dataclass
class AnlzFileHeaderData(DataclassMixin):
    type: str = csfield(PaddedString(4, encoding="ascii"))
    len_header: int = csfield(Int32ub)
    len_file: int = csfield(Int32ub)
    u1: int = csfield(Int32ub)
    u2: int = csfield(Int32ub)
    u3: int = csfield(Int32ub)
    u4: int = csfield(Int32ub)


AnlzFileHeader = DataclassStruct(AnlzFileHeaderData)

type AnlzTagContent = (
    PQTZContent
    | PQT2Content
    | PCOBContent
    | PCO2Content
    | PPTHContent
    | PVBRContent
    | PVDIContent
    | PVB2Content
    | PSSIContent
    | WaveformPreviewContent
    | PWV3Content
    | PWV4Content
    | PWV5Content
    | PWV6Content
    | PWV7Content
    | PWVCContent
    | bytes
)


@dataclass
class AnlzTagData(DataclassMixin):
    type: str = csfield(PaddedString(4, encoding="ascii"))
    len_header: int = csfield(Int32ub)
    len_tag: int = csfield(Int32ub)
    content: AnlzTagContent = csfield(
        Switch(
            this.type,
            {
                "PQTZ": PQTZ,
                "PQT2": PQT2,
                "PCOB": PCOB,  # seen in both DAT and EXT files
                "PCO2": PCO2,  # seen in EXT files
                "PPTH": PPTH,
                "PVBR": PVBR,
                "PVDI": PVDI,
                "PVB2": PVB2,
                "PSSI": PSSI,  # seen in EXT files
                "PWAV": PWAV,
                "PWV2": PWV2,
                "PWV3": PWV3,  # seen in EXT files
                "PWV4": PWV4,  # seen in EXT files
                "PWV5": PWV5,  # seen in EXT files
                "PWV6": PWV6,  # seen in 2EX files
                "PWV7": PWV7,  # seen in 2EX files
                "PWVC": PWVC,  # seen in 2EX files
            },
            default=Bytes(this.len_tag - 12),
        )
    )


AnlzTag = DataclassStruct(AnlzTagData)
