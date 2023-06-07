from dataclasses import fields, is_dataclass
from enum import Enum

def as_tuple(
        dc,
        excludes: set[str],
):
    """
    Tuple creation for dataclasses with easy exclusion of unwanted fields.
    :param dc: dataclass object
    :param excludes: set of string field names to exclude from the tuple

    """
    return tuple(
        getattr(dc, f.name) for f in fields(dc) if f.name not in excludes
    )


def assert_matches_plain(dc, plain_class, fld_name=None):
    """
    Tool for testing things haven't been broken when converting the original plain
    python classes to dataclasses.

    In use dc should be the new dataclass and plain_class the original class
    recursion will lead to dc being the new data and plain_class the old data.

    :param dc: new object
    :param plain_class: old object
    :param fld_name: name of the field being compared if given (for assert debugging)
    """
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
        assert dc.value == plain_class.value, f"{fld_name} does not match"
    else:
        assert dc == plain_class, f"{fld_name} does not match"
