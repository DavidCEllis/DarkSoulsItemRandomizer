from dataclasses import fields

from item_randomizer.items_setup import ITEMS
from item_randomizer._old_version.items_setup import ITEMS as OLD_ITEMS
from item_randomizer.util.dataclass_tools import assert_matches_plain


def test_items_match():
    for key in ITEMS:
        new_item, old_item = ITEMS[key], OLD_ITEMS[key]

        for f in fields(new_item):
            # diff got changed to difficulty internally
            # Originally the argument name and the variable name did not match
            name = f.name if f.name != "difficulty" else "diff"
            assert_matches_plain(
                getattr(new_item, name),
                getattr(old_item, name),
                name
            )
