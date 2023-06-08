from item_randomizer.shops_setup import DEFAULT_SHOP_DATA
from item_randomizer._old_version.shops_setup import DEFAULT_SHOP_DATA as OLD_SHOP_DATA

from item_randomizer.util.dataclass_tools import assert_matches_plain


def test_locations_match():
    for key in DEFAULT_SHOP_DATA:
        assert_matches_plain(DEFAULT_SHOP_DATA[key], OLD_SHOP_DATA[key])
