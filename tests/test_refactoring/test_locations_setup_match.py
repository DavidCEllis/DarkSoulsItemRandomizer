from item_randomizer.locations_setup import LOCATIONS
from item_randomizer._old_version.locations_setup import LOCATIONS as OLD_LOCATIONS

from item_randomizer.util.dataclass_tools import assert_matches_plain


def test_locations_match():
    for key in LOCATIONS:
        assert_matches_plain(LOCATIONS[key], OLD_LOCATIONS[key])
