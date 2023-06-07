import struct
import sys

from collections import namedtuple
from dataclasses import dataclass
import typing

from .base_param import BaseItem, BaseParam

class ShopLineItemType:
    WEAPON = 0
    ARMOR = 1
    RING = 2
    ITEM = 3
    SHOP_SPELL = 4
    NONE = -1

ShopLineupTuple = namedtuple("ShopLineupTuple", "lineup_id data description")

@dataclass
class ShopLineup(BaseItem):
    lineup_id: int
    item_type: typing.Any
    item_id: int
    cost: int
    sell_quantity: int
    event_flag: typing.Any
    mtrl_id: typing.Any
    qwc_id: typing.Any
    shop_type: typing.Any
    description: str

    @classmethod
    def from_binary(cls, lineup_id, data, description):
        (
            item_id,
            cost,
            mtrl_id,
            event_flag,
            qwc_id,
            sell_quantity,
            shop_type,
            item_type,
            _,
            _,
        ) = struct.unpack("@iiiiihBb II", data)
        return cls(
            lineup_id,
            item_type,
            item_id,
            cost,
            sell_quantity,
            event_flag,
            mtrl_id,
            qwc_id,
            shop_type,
            description,
        )

    def to_binary(self):
        arg_list = [
            self.item_id,
            self.cost,
            self.mtrl_id,
            self.event_flag,
            self.qwc_id,
            self.sell_quantity,
            self.shop_type,
            self.item_type,
        ]
        data = struct.pack("@iiiiihBb", *arg_list) + b"\x00" * 8
        return ShopLineupTuple(self.lineup_id, data, self.description)

    def as_string(self):
        return "Id: %d (%d %d %d %d %d %d %d %d): %s" % (
            self.lineup_id,
            self.item_id,
            self.cost,
            self.mtrl_id,
            self.event_flag,
            self.qwc_id,
            self.sell_quantity,
            self.shop_type,
            self.item_type,
            self.description,
        )


class ShopLineupParam(BaseParam):
    RECORD_SIZE = 0xC
    DATA_RECORD_SIZE = 0x20

    BASE_OBJ = ShopLineup

    def __init__(self, shop_lineups=None):
        if shop_lineups is None:
            shop_lineups = []
        self.shop_lineups = shop_lineups

    @staticmethod
    def get_count(file_content, master_offset):
        (
            strings_offset,
            data_offset,
            unk1,
            unk2,
            shop_lineup_count,
        ) = struct.unpack_from("<IHHHH", file_content, offset=master_offset)

        return shop_lineup_count

    def export_as_binary(self):
        num_of_records = len(self.shop_lineups)
        records_offset = 0x30
        data_offset = records_offset + num_of_records * self.RECORD_SIZE
        strings_offset = data_offset + num_of_records * self.DATA_RECORD_SIZE
        header = (
            struct.pack("@IHHHH", strings_offset, data_offset, 1, 1, num_of_records)
            + b"SHOP_LINEUP_PARAM"
            + b"\x00"
            + b"\x20" * 14
            + b"\x00\x02\x00\x00"
        )
        packed_record = b""
        packed_data = b""
        packed_strings = b""
        current_data_offset = data_offset
        current_strings_offset = strings_offset
        for lineup in sorted(self.shop_lineups, key=lambda lineup: lineup.lineup_id):
            (lineup_id, data, description) = lineup.to_binary()
            encoded_description = description.encode("shift-jis") + b"\x00"
            packed_record += struct.pack(
                "@III", lineup_id, current_data_offset, current_strings_offset
            )
            packed_data += data
            packed_strings += encoded_description
            current_data_offset += len(data)
            current_strings_offset += len(encoded_description)
        return header + packed_record + packed_data + packed_strings

    def as_string(self):
        return "\n".join(
            [
                lineup.as_string()
                for lineup in sorted(
                    self.shop_lineups, key=lambda lineup: lineup.lineup_id
                )
            ]
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No filename specified.")
        sys.exit(0)

    with open(sys.argv[1], "rb") as f:
        file_content = f.read()

        data = ShopLineupParam.load_from_file_content(file_content)
        print(data.as_string())
