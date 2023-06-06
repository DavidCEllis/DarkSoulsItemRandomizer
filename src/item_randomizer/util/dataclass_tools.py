from dataclasses import fields, is_dataclass


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
    else:
        assert dc == plain_class, f"{fld_name} does not match"
