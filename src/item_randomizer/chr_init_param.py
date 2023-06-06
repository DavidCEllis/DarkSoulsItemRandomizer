import struct
import sys

from collections import namedtuple
from dataclasses import dataclass
from .util.dataclass_tools import as_tuple

from .binary_handlers.binary_tools import extract_shift_jisz


ChrInitStruct = struct.Struct(
    "< 3f i 4i 4i 4i 5i 3i 7i 10i 2i 3h 4h 3h h 10b 10b 5b 7b 4b 10x"
)

ChrInitTuple = namedtuple("ChrInitTuple", "chr_init_id data description")


@dataclass
class ChrInit:
    chr_init_id: int
    base_rec_mp: float
    base_rec_sp: float
    red_falldam: float
    soul: int
    wep_r1: int
    wep_r2: int
    wep_l1: int
    wep_l2: int
    armor_head: int
    armor_chest: int
    armor_hand: int
    armor_leg: int
    arrow_1: int
    bolt_1: int
    arrow_2: int
    bolt_2: int
    ring_1: int
    ring_2: int
    ring_3: int
    ring_4: int
    ring_5: int
    skill_1: int
    skill_2: int
    skill_3: int
    spell_1: int
    spell_2: int
    spell_3: int
    spell_4: int
    spell_5: int
    spell_6: int
    spell_7: int
    item_1: int
    item_2: int
    item_3: int
    item_4: int
    item_5: int
    item_6: int
    item_7: int
    item_8: int
    item_9: int
    item_10: int
    facegen_id: int
    think_id: int
    base_hp: int  # Shorts from here
    base_mp: int
    base_sp: int
    arrow_1_num: int
    bolt_1_num: int
    arrow_2_num: int
    bolt_2_num: int
    qwc_sb: int
    qwc_mw: int
    qwc_cd: int
    soul_level: int
    base_vit: int  # Chrs from here
    base_att: int
    base_end: int
    base_str: int
    base_dex: int
    base_int: int
    base_fth: int
    base_luc: int
    base_hum: int
    base_res: int
    item_1_num: int
    item_2_num: int
    item_3_num: int
    item_4_num: int
    item_5_num: int
    item_6_num: int
    item_7_num: int
    item_8_num: int
    item_9_num: int
    item_10_num: int
    body_scale_head: int
    body_scale_chest: int
    body_scale_ab: int
    body_scale_arm: int
    body_scale_leg: int
    gest_0: int
    gest_1: int
    gest_2: int
    gest_3: int
    gest_4: int
    gest_5: int
    gest_6: int
    npc_type: int
    draw_type: int
    sex: int
    covenant: int
    description: str

    @classmethod
    def from_binary(cls, chr_init_id, data, description):
        return cls(
            chr_init_id,
            *ChrInitStruct.unpack_from(data, offset=0),
            description,
        )

    def to_binary(self):
        excluded_fields = {"chr_init_id", "description"}
        arg_tuple = as_tuple(self, excluded_fields)
        data = ChrInitStruct.pack(*arg_tuple)
        return ChrInitTuple(self.chr_init_id, data, self.description)

    def to_string(self):
        # Keep the same format as the old version
        excluded_fields = {"chr_init_id", "description"}
        values = as_tuple(self, excluded_fields)
        header = f"{self.chr_init_id} {self.description}"
        body = " ".join(f"{int(value)}" for value in values)
        return " ".join([header, body])


class ChrInitParam:
    RECORD_SIZE = 0xC
    DATA_RECORD_SIZE = 0xF0

    def __init__(self, chr_inits=None):
        if chr_inits is None:
            chr_inits = []
        self.chr_inits = chr_inits

    @classmethod
    def load_from_file_content(cls, file_content):
        master_offset = 0

        (strings_offset, data_offset, unk, chr_init_count) = struct.unpack_from(
            "<IIHH", file_content, offset=master_offset
        )
        master_offset = 0x30  # Skip the rest of the header.

        chr_inits = []
        for i in range(chr_init_count):
            (
                chr_init_id,
                chr_init_data_offset,
                chr_init_string_offset,
            ) = struct.unpack_from("<III", file_content, offset=master_offset)
            master_offset += struct.calcsize("<III")

            description = extract_shift_jisz(file_content, chr_init_string_offset)
            chr_init_data = file_content[
                chr_init_data_offset : chr_init_data_offset + cls.DATA_RECORD_SIZE
            ]
            chr_inits.append(
                ChrInit.from_binary(chr_init_id, chr_init_data, description)
            )
        return ChrInitParam(chr_inits)

    def find_chr_by_id(self, chr_id):
        for chr_init in self.chr_inits:
            if chr_init.chr_init_id == chr_id:
                return chr_init
        return None

    def export_as_binary(self):
        num_of_records = len(self.chr_inits)
        records_offset = 0x30
        data_offset = records_offset + num_of_records * self.RECORD_SIZE
        strings_offset = data_offset + num_of_records * self.DATA_RECORD_SIZE
        header = struct.pack("@IIHH", strings_offset, data_offset, 1, num_of_records)
        header += b"CHARACTER_INIT_PARAM" + b"\x00" + b"\x20" * 11 + b"\x00\x02\x00\x00"
        packed_record = b""
        packed_data = b""
        packed_strings = b""
        current_data_offset = data_offset
        current_strings_offset = strings_offset
        for chr_init in sorted(self.chr_inits, key=lambda c: c.chr_init_id):
            (chr_init_id, data, description) = chr_init.to_binary()
            encoded_description = description.encode("shift-jis") + b"\x00"
            packed_record += struct.pack(
                "@III", chr_init_id, current_data_offset, current_strings_offset
            )
            packed_data += data
            packed_strings += encoded_description
            current_data_offset += len(data)
            current_strings_offset += len(encoded_description)
        return header + packed_record + packed_data + packed_strings


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No filename specified.")
        sys.exit(0)

    with open(sys.argv[1], "rb") as f:
        content = f.read()

    chr_data = ChrInitParam.load_from_file_content(content)
    for chr_init in chr_data.chr_inits:
        print(chr_init.to_string())
