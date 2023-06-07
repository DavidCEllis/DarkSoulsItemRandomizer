from abc import ABC, abstractmethod

import struct

from .binary_tools import extract_shift_jisz


class BaseItem(ABC):
    @classmethod
    @abstractmethod
    def from_binary(cls, item_id, data, description):
        return NotImplemented

    @abstractmethod
    def to_binary(self):
        return NotImplemented


class BaseParam(ABC):
    RECORD_SIZE = 0xC
    DATA_RECORD_SIZE = 0x00  # MUST BE OVERRIDDEN

    BASE_OBJ = BaseItem

    @abstractmethod
    def __init__(self, inits=None):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_count(file_content, master_offset) -> int:
        return NotImplemented

    @classmethod
    def load_from_file_content(cls, file_content):
        master_offset = 0

        count = cls.get_count(file_content, master_offset)
        master_offset = 0x30  # Skip the rest of the header

        contents = []
        content_struct = struct.Struct("<III")

        for i in range(count):
            (item_id, item_data_offset, item_string_offset) = content_struct.unpack_from(
                file_content, offset=master_offset
            )

            master_offset += content_struct.size

            description = extract_shift_jisz(file_content, item_string_offset)
            item_data = file_content[
                item_data_offset: item_data_offset + cls.DATA_RECORD_SIZE
            ]

            contents.append(
                cls.BASE_OBJ.from_binary(item_id, item_data, description)
            )

        return cls(contents)


    @abstractmethod
    def export_as_binary(self):
        return NotImplemented
