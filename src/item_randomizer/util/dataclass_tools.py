from dataclasses import fields, is_dataclass
from enum import Enum

def as_tuple(
        dc,
        excludes: set[str],
):
    return tuple(
        getattr(dc, f.name) for f in fields(dc) if f.name not in excludes
    )


def assert_matches_plain(dc, plain_class, fld_name=None):
    if is_dataclass(dc):
        for f in fields(dc):
            dc_attrib = getattr(dc, f.name)
            plain_attrib = getattr(plain_class, f.name)
            assert_matches_plain(dc_attrib, plain_attrib, f.name)
    elif isinstance(dc, list):
        assert len(dc) == len(plain_class)
        for dc_item, plain_item in zip(dc, plain_class):
            assert_matches_plain(dc_item, plain_item, fld_name)
    elif isinstance(dc, Enum):
        assert dc.value == plain_class.value
    else:
        assert dc == plain_class, f"{fld_name} does not match, {isinstance(dc, Enum)}"
