from item_randomizer.util.dataclass_tools import assert_matches_plain
from item_randomizer.chr_setup import (
    VANILLA_CHRS,
    CHR_ARMOR_LINKS,
    ARMOR_SETS,
    STARTING_WEAPONS_AND_SHIELDS,
    EXTRA_DATA,
)
from item_randomizer._old_version.chr_setup import (
    VANILLA_CHRS as OLD_VANILLA_CHRS,
    CHR_ARMOR_LINKS as OLD_CHR_ARMOR_LINKS,
    ARMOR_SETS as OLD_ARMOR_SETS,
    STARTING_WEAPONS_AND_SHIELDS as OLD_STARTING_WEAPONS_AND_SHIELDS,
    EXTRA_DATA as OLD_EXTRA_DATA,
)


# These all have a check at the start to make sure they are the old/new versions
# Then compare each entry to make sure they match

def test_vanilla_chrs():
    assert VANILLA_CHRS != OLD_VANILLA_CHRS

    for key in VANILLA_CHRS:
        assert_matches_plain(VANILLA_CHRS[key], OLD_VANILLA_CHRS[key])


def test_chr_armor_links():
    assert CHR_ARMOR_LINKS != OLD_CHR_ARMOR_LINKS

    for new_link, old_link in zip(CHR_ARMOR_LINKS, OLD_CHR_ARMOR_LINKS):
        assert_matches_plain(new_link, old_link)


def test_armor_sets():
    assert ARMOR_SETS != OLD_ARMOR_SETS

    for new_set, old_set in zip(ARMOR_SETS, OLD_ARMOR_SETS):
        assert_matches_plain(new_set, old_set)


def test_starting_weapons_and_shields():
    assert STARTING_WEAPONS_AND_SHIELDS != OLD_STARTING_WEAPONS_AND_SHIELDS

    for key in STARTING_WEAPONS_AND_SHIELDS:
        assert_matches_plain(
            STARTING_WEAPONS_AND_SHIELDS[key],
            OLD_STARTING_WEAPONS_AND_SHIELDS[key]
        )

def test_extra_data():
    assert EXTRA_DATA != OLD_EXTRA_DATA

    for new_data, old_data in zip(EXTRA_DATA, OLD_EXTRA_DATA):
        assert_matches_plain(new_data, old_data)
