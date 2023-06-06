from dataclasses import fields


def as_tuple(
        dc,
        excludes: set[str],
):
    return tuple(
        getattr(dc, f.name) for f in fields(dc) if f.name not in excludes
    )
