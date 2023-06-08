from item_randomizer.randomizer_options import (
    RandOptDifficulty,
    RandOptKeyDifficulty,
    RandOptStartItemsDifficulty,
    RandOptSoulItemsDifficulty,
    RandOptGameVersion,
)

from item_randomizer._old_version.randomizer_options import (
    RandOptDifficulty as OldOptDifficulty,
    RandOptKeyDifficulty as OldOptKeyDifficulty,
    RandOptStartItemsDifficulty as OldOptStartItemsDifficulty,
    RandOptSoulItemsDifficulty as OldOptSoulItemsDifficulty,
    RandOptGameVersion as OldOptGameVersion,
)



def test_descriptions():
    for diff in RandOptDifficulty:
        assert diff.description == OldOptDifficulty.as_string(diff)

    for diff in RandOptKeyDifficulty:
        assert diff.description == OldOptKeyDifficulty.as_string(diff)

    for diff in RandOptStartItemsDifficulty:
        assert diff.description == OldOptStartItemsDifficulty.as_string(diff)

    for diff in RandOptSoulItemsDifficulty:
        assert diff.description == OldOptSoulItemsDifficulty.as_string(diff)

    for diff in RandOptGameVersion:
        assert diff == OldOptGameVersion.as_string(diff)
