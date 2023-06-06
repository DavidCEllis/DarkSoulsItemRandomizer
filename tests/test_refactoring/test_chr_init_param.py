from dataclasses import fields

from item_randomizer.chr_init_param import ChrInit
# noinspection PyProtectedMember
from item_randomizer._old_version.chr_init_param import ChrInit as OldChrInit


class TestChrInit:
    def test_init_matches(self):
        init_id = 1
        description = "ChrDescription"
        float_data = [float(i)/2 for i in range(1, 4)]
        int_data = [i for i in range(4, 91)]

        chr_init = ChrInit(init_id, *float_data, *int_data, description)
        old_chr_init = OldChrInit(init_id, *float_data, *int_data, description)

        for f in fields(chr_init):
            assert getattr(chr_init, f.name) == getattr(old_chr_init, f.name)

        # Old version has a trailing space which has been removed
        assert chr_init.to_string() == old_chr_init.to_string().strip()

        # New version uses a namedtuple but should still match the old plain tuple
        assert chr_init.to_binary() == old_chr_init.to_binary()

    def test_cycle_matches(self):
        init_id = 1
        description = "ChrDescription"
        float_data = [float(i) / 2 for i in range(1, 4)]
        int_data = [i for i in range(4, 91)]

        chr_init = ChrInit(init_id, *float_data, *int_data, description)

        cycled_chr_init = ChrInit.from_binary(*chr_init.to_binary())

        assert chr_init == cycled_chr_init