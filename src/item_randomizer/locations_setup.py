# Set up location information.


class LOC_DIF:
    IGNORE = -1  # Not used by the game.
    EASY = 0
    MEDIUM = 1
    HARD = 2
    NPC_EASY = 3
    NPC_MEDIUM = 4
    NPC_HARD = 5
    SHOP_EASY = 6
    SHOP_MEDIUM = 7
    SHOP_HARD = 8
    UPGRADE = 9
    RANDOM_UPGRADE = 10
    STARTING_ITEM = 11
    EMPTY = 12  # Empty, but could be used.
    LEAVE_ALONE = 13  # Important items that aren't appropriate to shuffle.


class AREA:
    NONE = -1
    MOVING_NPC = 0
    DEPTHS = 1
    LOWER_UNDEAD_BURG = 2
    LOWER_UNDEAD_BURG_RESIDENCE = 3
    UNDEAD_BURG = 4
    UNDEAD_BURG_RESIDENCE = 5
    WATCHTOWER_BASEMENT = 6
    UNDEAD_PARISH = 7
    FIRELINK = 8
    PAINTED_WORLD = 9
    PAINTED_WORLD_ANNEX = 10
    DARKROOT_GARDEN = 11
    DARKROOT_FOREST = 12
    DARKROOT_BASIN = 13
    OOLACILE_SANCTUARY = 14
    ROYAL_WOOD = 15
    OOLACILE_TOWNSHIP = 16
    OOLACILE_HIDDEN = 17
    KALAMEET_FIGHT = 18
    CHASM_OF_THE_ABYSS = 19
    CATACOMBS = 20
    TOMB_OF_THE_GIANTS_PRE_LV = 21
    TOMB_OF_THE_GIANTS_POST_LV = 22
    GREAT_HOLLOW = 23
    ASH_LAKE = 24
    BLIGHTTOWN = 25
    QUELAAGS_DOMAIN = 26
    DEMON_RUINS_NO_LAVA_PRE_LV = 27
    DEMON_RUINS_NO_LAVA_POST_LV = 28
    DEMON_RUINS_LAVA = 29
    LOST_IZALITH = 30
    SENS_FORTRESS = 31
    SENS_CAGE = 32
    ANOR_LONDO = 33
    DARKMOON_TOMB = 34
    NEW_LONDO_PRE_SEAL = 35
    NEW_LONDO_POST_LV = 36
    NEW_LONDO_POST_SEAL = 37
    NEW_LONDO_POST_SEAL_SKIP = 38
    VALLEY_OF_DRAKES = 39
    POST_4K = 40
    DUKES_PRISON = 41
    DUKES_PRISON_EXTRA = 42
    DUKES_PRISON_GIANT_CELL = 43
    DUKES_ARCHIVES = 44
    CRYSTAL_CAVE = 45
    KILN = 46
    UNDEAD_ASYLUM = 47
    UNDEAD_ASYLUM_F2_WEST = 48
    NPC_RNG_DROP = 49


# has_cumul_flag: (flag, count, chance_numerator, chance_denominator, cumulative_point)
#  * The first two are to build the drop table itself.
#  * The last three are to build the items in the drop table.
class CumulFlag:
    def __init__(self, flag, count, chance_numer, chance_denom, cumulative_point):
        self.flag = flag
        self.count = count
        self.chance_numer = chance_numer
        self.chance_denom = chance_denom
        self.cumulative_point = cumulative_point


class Location:
    def __repr__(self):
        return str("Location (id: " + str(self.location_id) + ")")

    def __init__(
        self,
        diff,
        area,
        max_size,
        is_transient=False,
        is_race_key_loc=False,
        linked_locations=[],
        has_flag=-1,
        has_cumul_flag=None,
        default_key=None,
        location_id=-1,
    ):
        if diff == LOC_DIF.IGNORE and area != AREA.NONE:
            print("Warning: Difficulty = IGNORE and area != NONE")
        if (
            diff != LOC_DIF.NPC_EASY
            and diff != LOC_DIF.NPC_MEDIUM
            and diff != LOC_DIF.NPC_HARD
            and diff != LOC_DIF.EMPTY
            and diff != LOC_DIF.UPGRADE
            and diff != LOC_DIF.RANDOM_UPGRADE
        ) and area == AREA.NPC_RNG_DROP:
            print(
                "Warning: Difficulty != NPC_(EASY|MEDIUM|HARD) but area = NPC_RNG_DROP"
            )
        if (
            diff == LOC_DIF.NPC_EASY
            or diff == LOC_DIF.NPC_MEDIUM
            or diff == LOC_DIF.NPC_HARD
        ) and area != AREA.NPC_RNG_DROP:
            print(
                "Warning: Difficulty = NPC_(EASY|MEDIUM|HARD) and area != NPC_RNG_DROP"
            )

        self.diff = diff
        self.area = area
        self.max_size = max_size
        self.is_transient = is_transient
        self.is_race_key_loc = is_race_key_loc
        self.linked_locations = linked_locations
        self.has_flag = has_flag
        self.has_cumul_flag = has_cumul_flag
        self.default_key = default_key


LOCATIONS = {
    0: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    2: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1000: Location(
        LOC_DIF.LEAVE_ALONE,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        linked_locations=[6000],
    ),
    1010: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 9, is_transient=True),
    1020: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1030: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1040: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9, is_transient=True),
    1050: Location(
        LOC_DIF.EASY,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        linked_locations=[1070, 6280],
    ),
    1060: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 9, is_transient=True),
    1080: Location(LOC_DIF.LEAVE_ALONE, AREA.UNDEAD_ASYLUM, 1, is_transient=True),
    1081: Location(
        LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True, has_flag=50000081
    ),
    1082: Location(
        LOC_DIF.LEAVE_ALONE,
        AREA.NONE,
        1,
        is_transient=True,
        has_flag=50000082,
        linked_locations=[6022],
    ),
    1090: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 9, default_key="lordvessel"),
    1100: Location(
        LOC_DIF.HARD,
        AREA.NEW_LONDO_POST_LV,
        9,
        is_race_key_loc=True,
        default_key="key_to_the_seal",
    ),
    1110: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 9, is_transient=True),
    1120: Location(LOC_DIF.HARD, AREA.UNDEAD_PARISH, 9, is_transient=True),
    1130: Location(LOC_DIF.LEAVE_ALONE, AREA.UNDEAD_PARISH, 9),
    1140: Location(LOC_DIF.EASY, AREA.FIRELINK, 9, is_transient=True),
    1150: Location(LOC_DIF.HARD, AREA.UNDEAD_PARISH, 9, is_transient=True),
    1160: Location(LOC_DIF.MEDIUM, AREA.DARKROOT_GARDEN, 9, is_transient=True),
    1170: Location(LOC_DIF.LEAVE_ALONE, AREA.DARKROOT_GARDEN, 9, is_transient=True),
    1180: Location(LOC_DIF.LEAVE_ALONE, AREA.DARKROOT_GARDEN, 9, is_transient=True),
    1190: Location(LOC_DIF.EASY, AREA.CATACOMBS, 9, is_transient=True),
    1200: Location(LOC_DIF.MEDIUM, AREA.CATACOMBS, 9, is_transient=True),
    1210: Location(LOC_DIF.HARD, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9, is_transient=True),
    1220: Location(LOC_DIF.HARD, AREA.CATACOMBS, 9, is_transient=True),
    1230: Location(LOC_DIF.LEAVE_ALONE, AREA.CATACOMBS, 9, is_transient=True),
    1240: Location(
        LOC_DIF.MEDIUM, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9, is_transient=True
    ),
    1250: Location(LOC_DIF.HARD, AREA.ASH_LAKE, 9, is_transient=True),
    1260: Location(LOC_DIF.HARD, AREA.ASH_LAKE, 9, is_transient=True),
    1270: Location(LOC_DIF.LEAVE_ALONE, AREA.ASH_LAKE, 9, is_transient=True),
    1280: Location(LOC_DIF.HARD, AREA.QUELAAGS_DOMAIN, 9, is_transient=True),
    1290: Location(LOC_DIF.HARD, AREA.QUELAAGS_DOMAIN, 9, is_transient=True),
    1300: Location(
        LOC_DIF.HARD, AREA.BLIGHTTOWN, 9, is_transient=True, linked_locations=[6170]
    ),
    1310: Location(LOC_DIF.HARD, AREA.QUELAAGS_DOMAIN, 9, is_transient=True),
    1320: Location(LOC_DIF.LEAVE_ALONE, AREA.QUELAAGS_DOMAIN, 9, is_transient=True),
    1330: Location(LOC_DIF.LEAVE_ALONE, AREA.QUELAAGS_DOMAIN, 9, is_transient=True),
    1340: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1350: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 9, is_transient=True),
    1360: Location(LOC_DIF.HARD, AREA.DARKMOON_TOMB, 9, is_transient=True),
    1370: Location(LOC_DIF.LEAVE_ALONE, AREA.DARKMOON_TOMB, 1, is_transient=True),
    1371: Location(LOC_DIF.LEAVE_ALONE, AREA.DARKMOON_TOMB, 1, is_transient=True),
    1380: Location(LOC_DIF.HARD, AREA.POST_4K, 9, is_transient=True),
    1390: Location(LOC_DIF.LEAVE_ALONE, AREA.POST_4K, 9, is_transient=True),
    1400: Location(LOC_DIF.LEAVE_ALONE, AREA.POST_4K, 1, is_transient=True),
    1401: Location(LOC_DIF.LEAVE_ALONE, AREA.POST_4K, 1, is_transient=True),
    1402: Location(LOC_DIF.LEAVE_ALONE, AREA.POST_4K, 1, is_transient=True),
    1403: Location(LOC_DIF.LEAVE_ALONE, AREA.POST_4K, 1, is_transient=True),
    1404: Location(LOC_DIF.LEAVE_ALONE, AREA.POST_4K, 1, is_transient=True),
    1410: Location(LOC_DIF.LEAVE_ALONE, AREA.UNDEAD_PARISH, 9, is_transient=True),
    1420: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1500: Location(
        LOC_DIF.HARD,
        AREA.OOLACILE_TOWNSHIP,
        1,
        is_transient=True,
        linked_locations=[6740],
    ),
    1510: Location(
        LOC_DIF.HARD,
        AREA.KALAMEET_FIGHT,
        1,
        is_transient=True,
        linked_locations=[41100000],
    ),
    1520: Location(
        LOC_DIF.HARD,
        AREA.OOLACILE_SANCTUARY,
        9,
        is_transient=True,
        linked_locations=[41400000],
    ),
    2020: Location(LOC_DIF.LEAVE_ALONE, AREA.DUKES_PRISON, 9, is_transient=True),
    2030: Location(
        LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True, has_flag=50001031
    ),
    2031: Location(LOC_DIF.HARD, AREA.FIRELINK, 8, is_transient=True),
    2060: Location(LOC_DIF.LEAVE_ALONE, AREA.ANOR_LONDO, 9, is_transient=True),
    2070: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 9, has_flag=50001070),
    2200: Location(LOC_DIF.HARD, AREA.OOLACILE_TOWNSHIP, 9, is_transient=True),
    2500: Location(
        LOC_DIF.HARD, AREA.DEPTHS, 9, is_race_key_loc=True, default_key="blighttown_key"
    ),
    2510: Location(
        LOC_DIF.HARD,
        AREA.LOWER_UNDEAD_BURG,
        9,
        is_race_key_loc=True,
        default_key="key_to_depths",
    ),
    2520: Location(LOC_DIF.HARD, AREA.PAINTED_WORLD, 9, is_race_key_loc=True),
    2530: Location(LOC_DIF.HARD, AREA.DARKROOT_FOREST, 9, is_race_key_loc=True),
    2540: Location(
        LOC_DIF.HARD,
        AREA.DARKROOT_GARDEN,
        9,
        is_race_key_loc=True,
        default_key="covenant_of_artorias",
    ),
    2550: Location(
        LOC_DIF.HARD,
        AREA.TOMB_OF_THE_GIANTS_PRE_LV,
        9,
        is_race_key_loc=True,
        default_key="rite_of_kindling",
    ),
    2560: Location(
        LOC_DIF.HARD,
        AREA.TOMB_OF_THE_GIANTS_POST_LV,
        9,
        is_race_key_loc=True,
        default_key="lord_soul_nito",
    ),
    2570: Location(LOC_DIF.HARD, AREA.BLIGHTTOWN, 9, is_race_key_loc=True),
    2580: Location(
        LOC_DIF.HARD,
        AREA.LOST_IZALITH,
        9,
        is_race_key_loc=True,
        default_key="lord_soul_bed_of_chaos",
    ),
    2590: Location(LOC_DIF.HARD, AREA.SENS_FORTRESS, 9, is_race_key_loc=True),
    2600: Location(LOC_DIF.HARD, AREA.DARKMOON_TOMB, 9, is_race_key_loc=True),
    2610: Location(
        LOC_DIF.HARD, AREA.ANOR_LONDO, 1, is_race_key_loc=True, linked_locations=[2620]
    ),
    2611: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 8, is_transient=True),
    2621: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 8, is_transient=True),
    2630: Location(
        LOC_DIF.HARD,
        AREA.POST_4K,
        9,
        is_race_key_loc=True,
        default_key="lord_soul_shard_four_kings",
    ),
    2640: Location(
        LOC_DIF.HARD,
        AREA.CRYSTAL_CAVE,
        9,
        is_race_key_loc=True,
        default_key="lord_soul_shard_seath",
    ),
    2650: Location(LOC_DIF.HARD, AREA.KILN, 9, is_race_key_loc=True),
    2660: Location(LOC_DIF.LEAVE_ALONE, AREA.UNDEAD_ASYLUM, 1, has_flag=50001660),
    2661: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=50001661
    ),
    2670: Location(
        LOC_DIF.HARD,
        AREA.DEMON_RUINS_NO_LAVA_POST_LV,
        9,
        is_race_key_loc=True,
        default_key="orange_charred_ring",
    ),
    2680: Location(LOC_DIF.HARD, AREA.OOLACILE_SANCTUARY, 9, is_race_key_loc=True),
    2690: Location(LOC_DIF.HARD, AREA.ROYAL_WOOD, 9, is_race_key_loc=True),
    2700: Location(LOC_DIF.HARD, AREA.CHASM_OF_THE_ABYSS, 9, is_race_key_loc=True),
    2710: Location(LOC_DIF.HARD, AREA.KALAMEET_FIGHT, 9, is_race_key_loc=True),
    2800: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    2810: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    2820: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    3000: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810800
    ),
    3010: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810810
    ),
    3020: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810820
    ),
    3030: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810830
    ),
    3040: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810840
    ),
    3050: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810850
    ),
    3060: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810860
    ),
    3070: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810870
    ),
    3080: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810880
    ),
    3090: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810890
    ),
    3100: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810900
    ),
    3110: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    3120: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810920
    ),
    3130: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810930
    ),
    3140: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810940
    ),
    3150: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810950
    ),
    3160: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810960
    ),
    3170: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810970
    ),
    3180: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810980
    ),
    3190: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51810990
    ),
    3200: Location(
        LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_transient=True, has_flag=51811000
    ),
    4000: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4001: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4002: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4003: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4004: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4005: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4006: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4007: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4008: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4010: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4011: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4012: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4013: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4014: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4015: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4016: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4017: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4018: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4020: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4021: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4022: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4023: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4024: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4025: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4026: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4027: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4028: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4030: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4031: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4032: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4033: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4034: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4035: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4036: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4037: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4038: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4040: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4041: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4042: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4043: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4044: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4045: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4046: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4047: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4048: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4050: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4051: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4052: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4053: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4054: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4055: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4056: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4057: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4058: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4060: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4061: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4062: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4063: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4064: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4065: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4066: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4067: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4068: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4070: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4071: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4072: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4073: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4074: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4075: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4076: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    4077: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 1, is_transient=True),
    5000: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    5010: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    5020: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    5030: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    5040: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    5200: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    5210: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    5220: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    5230: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    5240: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    5250: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    5260: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    5270: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    5280: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    6001: Location(LOC_DIF.MEDIUM, AREA.MOVING_NPC, 9, is_transient=True),
    6010: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 9, is_transient=True),
    6020: Location(LOC_DIF.LEAVE_ALONE, AREA.UNDEAD_ASYLUM, 1, is_transient=True),
    6021: Location(LOC_DIF.LEAVE_ALONE, AREA.UNDEAD_ASYLUM, 1, is_transient=True),
    6040: Location(LOC_DIF.MEDIUM, AREA.MOVING_NPC, 9, is_transient=True),
    6070: Location(
        LOC_DIF.HARD, AREA.MOVING_NPC, 1, is_transient=True, has_flag=50006070
    ),
    6071: Location(
        LOC_DIF.HARD, AREA.UNDEAD_PARISH, 1, is_transient=True, has_flag=50006071
    ),
    6072: Location(
        LOC_DIF.EASY, AREA.MOVING_NPC, 1, is_transient=True, has_flag=50006072
    ),
    6080: Location(
        LOC_DIF.HARD, AREA.FIRELINK, 1, is_transient=True, has_flag=50006080
    ),
    6081: Location(
        LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True, has_flag=50006081
    ),
    6160: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    6180: Location(LOC_DIF.IGNORE, AREA.NONE, 1, is_transient=True, has_flag=50000100),
    6181: Location(LOC_DIF.IGNORE, AREA.NONE, 1, is_transient=True, has_flag=50006180),
    6190: Location(
        LOC_DIF.HARD,
        AREA.UNDEAD_PARISH,
        1,
        is_race_key_loc=True,
        linked_locations=[60001401],
        default_key="crest_of_artorias",
    ),
    6191: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 8, is_transient=True),
    6230: Location(
        LOC_DIF.EASY,
        AREA.UNDEAD_BURG,
        1,
        is_transient=True,
        linked_locations=[60001100],
    ),
    6231: Location(
        LOC_DIF.HARD,
        AREA.UNDEAD_BURG,
        1,
        is_race_key_loc=True,
        linked_locations=[60001105],
        default_key="residence_key",
    ),
    6232: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    6233: Location(
        LOC_DIF.EASY,
        AREA.UNDEAD_BURG,
        1,
        is_transient=True,
        linked_locations=[60001134],
    ),
    6281: Location(LOC_DIF.EASY, AREA.MOVING_NPC, 8, is_transient=True),
    6300: Location(LOC_DIF.MEDIUM, AREA.MOVING_NPC, 9, is_transient=True),
    6310: Location(LOC_DIF.MEDIUM, AREA.MOVING_NPC, 9, is_transient=True),
    6320: Location(LOC_DIF.MEDIUM, AREA.MOVING_NPC, 9, is_transient=True),
    6370: Location(LOC_DIF.LEAVE_ALONE, AREA.UNDEAD_PARISH, 1, is_transient=True),
    6371: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 9, is_transient=True),
    6420: Location(LOC_DIF.MEDIUM, AREA.MOVING_NPC, 9, is_transient=True),
    6500: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    6530: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9, is_transient=True),
    6550: Location(LOC_DIF.HARD, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9, is_transient=True),
    6560: Location(
        LOC_DIF.HARD,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        has_cumul_flag=CumulFlag(9100, 2, 33, 100, 100),
    ),
    6561: Location(
        LOC_DIF.HARD,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        has_cumul_flag=CumulFlag(9108, 2, 33, 100, 100),
    ),
    6570: Location(LOC_DIF.HARD, AREA.PAINTED_WORLD, 9, is_transient=True),
    6580: Location(LOC_DIF.HARD, AREA.WATCHTOWER_BASEMENT, 9, is_transient=True),
    6600: Location(LOC_DIF.HARD, AREA.SENS_FORTRESS, 9, is_transient=True),
    6620: Location(LOC_DIF.HARD, AREA.LOST_IZALITH, 9, is_transient=True),
    6640: Location(LOC_DIF.EMPTY, AREA.ANOR_LONDO, 9, is_transient=True),
    6650: Location(LOC_DIF.EMPTY, AREA.ANOR_LONDO, 9, is_transient=True),
    6741: Location(LOC_DIF.HARD, AREA.OOLACILE_TOWNSHIP, 8, is_transient=True),
    7020: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_ASYLUM, 9, is_transient=True),
    7030: Location(LOC_DIF.HARD, AREA.DUKES_ARCHIVES, 9, is_transient=True),
    8000: Location(LOC_DIF.MEDIUM, AREA.DARKROOT_GARDEN, 9, is_transient=True),
    9000: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9),
    9010: Location(LOC_DIF.HARD, AREA.POST_4K, 1, is_transient=True),
    9020: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9),
    9030: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9),
    9040: Location(LOC_DIF.HARD, AREA.CHASM_OF_THE_ABYSS, 1, is_transient=True),
    # Snipped several rows of un-used testing data that does not fit the
    #  standards of any other row. Rather than supporting this, it will
    #  not be included in the file, unless it is later deemed necessary.
    100000: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100010: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100020: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100100: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100110: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100120: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100200: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100210: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100220: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100300: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100310: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100320: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100400: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100410: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100420: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100500: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100510: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100520: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100600: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100610: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100620: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100700: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100710: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100720: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100800: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100810: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100820: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100900: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100910: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    100920: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101000: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101010: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101020: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101100: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101110: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101120: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101200: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101210: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101220: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101300: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101310: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101320: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101400: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101410: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    101420: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    1000000: Location(LOC_DIF.HARD, AREA.DEPTHS, 9),
    1000010: Location(LOC_DIF.EASY, AREA.DEPTHS, 9),
    1000020: Location(LOC_DIF.EASY, AREA.DEPTHS, 9),
    1000030: Location(LOC_DIF.EASY, AREA.DEPTHS, 9),
    1000040: Location(LOC_DIF.MEDIUM, AREA.DEPTHS, 9),
    1000050: Location(LOC_DIF.EASY, AREA.DEPTHS, 9),
    1000090: Location(LOC_DIF.MEDIUM, AREA.DEPTHS, 9),
    1000100: Location(LOC_DIF.MEDIUM, AREA.DEPTHS, 9),
    1000120: Location(LOC_DIF.EASY, AREA.DEPTHS, 9),
    1000140: Location(LOC_DIF.EASY, AREA.DEPTHS, 9),
    1000170: Location(LOC_DIF.MEDIUM, AREA.DEPTHS, 9),
    1000180: Location(LOC_DIF.EASY, AREA.DEPTHS, 9),
    1000190: Location(LOC_DIF.MEDIUM, AREA.DEPTHS, 9),
    1000210: Location(LOC_DIF.EASY, AREA.DEPTHS, 9),
    1000240: Location(
        LOC_DIF.EASY,
        AREA.DEPTHS,
        9,
        is_race_key_loc=True,
        default_key="sewer_chamber_key",
    ),
    1000500: Location(
        LOC_DIF.HARD, AREA.DEPTHS, 9, is_race_key_loc=True, default_key="large_ember"
    ),
    1010000: Location(
        LOC_DIF.MEDIUM,
        AREA.UNDEAD_PARISH,
        9,
        is_race_key_loc=True,
        default_key="mystery_key",
    ),
    1010020: Location(LOC_DIF.MEDIUM, AREA.LOWER_UNDEAD_BURG, 9),
    1010040: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 9),
    1010050: Location(LOC_DIF.HARD, AREA.UNDEAD_PARISH, 9, has_flag=51010050),
    1010070: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 9),
    1010080: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 9),
    1010090: Location(LOC_DIF.HARD, AREA.UNDEAD_BURG, 9),
    1010100: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_BURG, 9),
    1010120: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_BURG, 9),
    1010130: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 9),
    1010140: Location(
        LOC_DIF.EASY,
        AREA.UNDEAD_PARISH,
        9,
        is_race_key_loc=True,
        default_key="basement_key",
    ),
    1010160: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_BURG, 9),
    1010210: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 9),
    1010220: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 9),
    1010260: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 9),
    1010280: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 9),
    1010300: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 9),
    1010370: Location(LOC_DIF.EASY, AREA.LOWER_UNDEAD_BURG, 9),
    1010380: Location(LOC_DIF.MEDIUM, AREA.LOWER_UNDEAD_BURG, 9),
    1010390: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1010400: Location(LOC_DIF.HARD, AREA.UNDEAD_BURG, 9),
    1010410: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1010420: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1010430: Location(LOC_DIF.EASY, AREA.LOWER_UNDEAD_BURG, 9),
    1010440: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 9),
    1010450: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 9, is_race_key_loc=True),
    1010460: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_BURG_RESIDENCE, 9, is_race_key_loc=True
    ),
    1010470: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 9),
    1010480: Location(LOC_DIF.HARD, AREA.UNDEAD_BURG, 9),
    1010490: Location(LOC_DIF.MEDIUM, AREA.LOWER_UNDEAD_BURG, 9),
    1010500: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 9),
    1010510: Location(LOC_DIF.MEDIUM, AREA.LOWER_UNDEAD_BURG_RESIDENCE, 9),
    1010520: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 9),
    1020000: Location(LOC_DIF.EASY, AREA.FIRELINK, 9),
    1020010: Location(LOC_DIF.EASY, AREA.FIRELINK, 9),
    1020020: Location(LOC_DIF.EASY, AREA.FIRELINK, 9),
    1020030: Location(LOC_DIF.EASY, AREA.FIRELINK, 9),
    1020040: Location(LOC_DIF.EASY, AREA.FIRELINK, 9),
    1020050: Location(LOC_DIF.EASY, AREA.FIRELINK, 9),
    1020060: Location(LOC_DIF.EASY, AREA.FIRELINK, 9),
    1020070: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 9, is_race_key_loc=True),
    1020090: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 9),
    1020110: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 9),
    1020120: Location(LOC_DIF.EASY, AREA.FIRELINK, 9),
    1020130: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 9),
    1020140: Location(LOC_DIF.EASY, AREA.FIRELINK, 9),
    1020150: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 9),
    1020160: Location(LOC_DIF.EASY, AREA.FIRELINK, 9),
    1020170: Location(LOC_DIF.HARD, AREA.FIRELINK, 9),
    1020180: Location(LOC_DIF.EASY, AREA.FIRELINK, 9, is_race_key_loc=True),
    1020190: Location(LOC_DIF.EASY, AREA.FIRELINK, 9, is_race_key_loc=True),
    1020200: Location(LOC_DIF.EASY, AREA.FIRELINK, 9, is_race_key_loc=True),
    1020210: Location(
        LOC_DIF.HARD,
        AREA.FIRELINK,
        9,
        is_race_key_loc=True,
        default_key="undead_asylum_f2_west_key",
    ),
    1100010: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD, 9),
    # Link the PTDE Dried Finger location to its DS1R analogue, since only one is used in each game.
    1100020: Location(LOC_DIF.HARD, AREA.PAINTED_WORLD, 9, linked_locations=[1100050]),
    1100030: Location(LOC_DIF.MEDIUM, AREA.PAINTED_WORLD, 9),
    1100040: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD, 9),
    1100060: Location(LOC_DIF.MEDIUM, AREA.PAINTED_WORLD_ANNEX, 9),
    1100070: Location(LOC_DIF.MEDIUM, AREA.PAINTED_WORLD, 9),
    1100090: Location(LOC_DIF.HARD, AREA.PAINTED_WORLD_ANNEX, 9),
    1100100: Location(LOC_DIF.MEDIUM, AREA.PAINTED_WORLD_ANNEX, 9),
    1100120: Location(LOC_DIF.HARD, AREA.PAINTED_WORLD, 9),
    1100130: Location(LOC_DIF.MEDIUM, AREA.PAINTED_WORLD, 9),
    1100140: Location(
        LOC_DIF.HARD,
        AREA.PAINTED_WORLD,
        9,
        is_race_key_loc=True,
        default_key="annex_key",
    ),
    1100150: Location(LOC_DIF.HARD, AREA.PAINTED_WORLD, 9, is_transient=True),
    1100160: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD, 9),
    1100170: Location(LOC_DIF.HARD, AREA.PAINTED_WORLD, 9),
    1100190: Location(LOC_DIF.MEDIUM, AREA.PAINTED_WORLD, 9),
    1100200: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD, 9),
    1100210: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD, 9),
    1100230: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD, 9),
    1100240: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD, 9),
    1100250: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD, 9),
    1100260: Location(LOC_DIF.MEDIUM, AREA.PAINTED_WORLD, 9, has_flag=51100260),
    1100280: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD, 9),
    1100290: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD, 9),
    1100300: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD, 9),
    1100310: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD, 9),
    1100320: Location(LOC_DIF.HARD, AREA.PAINTED_WORLD_ANNEX, 9),
    1100330: Location(LOC_DIF.MEDIUM, AREA.PAINTED_WORLD, 9),
    1100340: Location(LOC_DIF.EASY, AREA.PAINTED_WORLD_ANNEX, 9),
    1100350: Location(LOC_DIF.MEDIUM, AREA.PAINTED_WORLD, 9),
    1100370: Location(
        LOC_DIF.HARD,
        AREA.PAINTED_WORLD_ANNEX,
        9,
        is_race_key_loc=True,
        default_key="dark_ember",
    ),
    1100500: Location(LOC_DIF.MEDIUM, AREA.PAINTED_WORLD, 9, is_race_key_loc=True),
    1200010: Location(LOC_DIF.EASY, AREA.DARKROOT_FOREST, 9),
    1200020: Location(LOC_DIF.MEDIUM, AREA.DARKROOT_BASIN, 9),
    1200030: Location(LOC_DIF.EASY, AREA.DARKROOT_FOREST, 9),
    1200040: Location(LOC_DIF.EASY, AREA.DARKROOT_BASIN, 9),
    1200060: Location(LOC_DIF.MEDIUM, AREA.DARKROOT_FOREST, 9),
    1200070: Location(LOC_DIF.MEDIUM, AREA.DARKROOT_FOREST, 9),
    1200080: Location(LOC_DIF.EASY, AREA.DARKROOT_GARDEN, 9),
    1200120: Location(LOC_DIF.MEDIUM, AREA.DARKROOT_GARDEN, 9),
    1200140: Location(
        LOC_DIF.MEDIUM,
        AREA.DARKROOT_FOREST,
        1,
        is_race_key_loc=True,
        default_key="watchtower_basement_key",
    ),
    1200141: Location(
        LOC_DIF.MEDIUM,
        AREA.DARKROOT_FOREST,
        1,
        is_race_key_loc=True,
        default_key="divine_ember",
    ),
    1200142: Location(LOC_DIF.MEDIUM, AREA.DARKROOT_FOREST, 7),
    1200150: Location(LOC_DIF.HARD, AREA.DARKROOT_BASIN, 9, is_transient=True),
    1200160: Location(LOC_DIF.HARD, AREA.DARKROOT_GARDEN, 9),
    1200170: Location(LOC_DIF.EASY, AREA.DARKROOT_FOREST, 9, has_flag=51200170),
    1200500: Location(
        LOC_DIF.MEDIUM,
        AREA.DARKROOT_GARDEN,
        9,
        is_race_key_loc=True,
        default_key="enchanted_ember",
    ),
    1200510: Location(LOC_DIF.MEDIUM, AREA.DARKROOT_GARDEN, 9, is_race_key_loc=True),
    1200180: Location(LOC_DIF.MEDIUM, AREA.DARKROOT_FOREST, 9),
    1200190: Location(LOC_DIF.HARD, AREA.DARKROOT_BASIN, 9),
    1200200: Location(LOC_DIF.MEDIUM, AREA.DARKROOT_BASIN, 9),
    1200210: Location(LOC_DIF.EASY, AREA.DARKROOT_BASIN, 9),
    1210000: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210010: Location(LOC_DIF.EASY, AREA.OOLACILE_SANCTUARY, 9),
    1210020: Location(LOC_DIF.MEDIUM, AREA.ROYAL_WOOD, 9),
    1210030: Location(LOC_DIF.EASY, AREA.ROYAL_WOOD, 9, has_flag=51210030),
    1210040: Location(LOC_DIF.EASY, AREA.ROYAL_WOOD, 9),
    1210050: Location(LOC_DIF.EASY, AREA.ROYAL_WOOD, 9),
    1210060: Location(LOC_DIF.MEDIUM, AREA.ROYAL_WOOD, 9),
    1210070: Location(LOC_DIF.HARD, AREA.ROYAL_WOOD, 9),
    1210080: Location(LOC_DIF.EASY, AREA.ROYAL_WOOD, 9),
    1210090: Location(LOC_DIF.EASY, AREA.ROYAL_WOOD, 9),
    1210100: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210110: Location(LOC_DIF.EASY, AREA.OOLACILE_TOWNSHIP, 9),
    1210120: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210130: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210140: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210150: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210160: Location(LOC_DIF.EASY, AREA.OOLACILE_TOWNSHIP, 9),
    1210170: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210180: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210190: Location(LOC_DIF.EASY, AREA.OOLACILE_TOWNSHIP, 9),
    1210200: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210210: Location(LOC_DIF.EASY, AREA.OOLACILE_TOWNSHIP, 9),
    1210220: Location(LOC_DIF.MEDIUM, AREA.ROYAL_WOOD, 9),
    1210230: Location(LOC_DIF.MEDIUM, AREA.ROYAL_WOOD, 9),
    1210240: Location(LOC_DIF.MEDIUM, AREA.ROYAL_WOOD, 9),
    1210250: Location(LOC_DIF.HARD, AREA.KALAMEET_FIGHT, 9),
    1210260: Location(LOC_DIF.MEDIUM, AREA.OOLACILE_TOWNSHIP, 9),
    1210270: Location(LOC_DIF.MEDIUM, AREA.CHASM_OF_THE_ABYSS, 9),
    1210280: Location(LOC_DIF.MEDIUM, AREA.CHASM_OF_THE_ABYSS, 9),
    1210290: Location(LOC_DIF.HARD, AREA.CHASM_OF_THE_ABYSS, 9),
    1210300: Location(LOC_DIF.MEDIUM, AREA.CHASM_OF_THE_ABYSS, 9),
    1210310: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210320: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210330: Location(LOC_DIF.HARD, AREA.CHASM_OF_THE_ABYSS, 9),
    1210340: Location(LOC_DIF.MEDIUM, AREA.CHASM_OF_THE_ABYSS, 9),
    1210350: Location(LOC_DIF.EASY, AREA.ROYAL_WOOD, 9),
    1210360: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210370: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210380: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210390: Location(LOC_DIF.EASY, AREA.ROYAL_WOOD, 9),
    1210400: Location(LOC_DIF.EASY, AREA.ROYAL_WOOD, 9),
    1210410: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210420: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210430: Location(LOC_DIF.HARD, AREA.OOLACILE_TOWNSHIP, 9),
    1210440: Location(LOC_DIF.MEDIUM, AREA.CHASM_OF_THE_ABYSS, 9),
    1210450: Location(LOC_DIF.MEDIUM, AREA.ROYAL_WOOD, 9),
    1210460: Location(LOC_DIF.MEDIUM, AREA.OOLACILE_TOWNSHIP, 9),
    1210470: Location(LOC_DIF.MEDIUM, AREA.ROYAL_WOOD, 9),
    1210500: Location(LOC_DIF.MEDIUM, AREA.ROYAL_WOOD, 9, is_race_key_loc=True),
    1210510: Location(LOC_DIF.HARD, AREA.OOLACILE_TOWNSHIP, 9, is_race_key_loc=True),
    1210520: Location(LOC_DIF.HARD, AREA.OOLACILE_HIDDEN, 9, is_race_key_loc=True),
    1210530: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1210540: Location(LOC_DIF.HARD, AREA.OOLACILE_TOWNSHIP, 9, is_race_key_loc=True),
    1210550: Location(LOC_DIF.HARD, AREA.ROYAL_WOOD, 9, is_race_key_loc=True),
    1210560: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1211000: Location(LOC_DIF.MEDIUM, AREA.OOLACILE_TOWNSHIP, 9),
    1300000: Location(LOC_DIF.EASY, AREA.CATACOMBS, 9),
    1300010: Location(LOC_DIF.MEDIUM, AREA.CATACOMBS, 9),
    1300020: Location(
        LOC_DIF.MEDIUM,
        AREA.CATACOMBS,
        9,
        is_race_key_loc=True,
        default_key="darkmoon_seance_ring",
    ),
    1300030: Location(LOC_DIF.MEDIUM, AREA.CATACOMBS, 9),
    1300070: Location(LOC_DIF.EASY, AREA.CATACOMBS, 9),
    1300100: Location(LOC_DIF.HARD, AREA.CATACOMBS, 9),
    1300110: Location(LOC_DIF.HARD, AREA.CATACOMBS, 9),
    1300140: Location(LOC_DIF.EASY, AREA.CATACOMBS, 9),
    1300150: Location(LOC_DIF.MEDIUM, AREA.CATACOMBS, 9),
    1300190: Location(LOC_DIF.EASY, AREA.CATACOMBS, 9),
    1300210: Location(LOC_DIF.MEDIUM, AREA.CATACOMBS, 9),
    1300220: Location(LOC_DIF.EASY, AREA.CATACOMBS, 9),
    1300230: Location(LOC_DIF.HARD, AREA.CATACOMBS, 9),
    1300240: Location(LOC_DIF.MEDIUM, AREA.CATACOMBS, 9),
    1300250: Location(LOC_DIF.EASY, AREA.CATACOMBS, 9),
    1310000: Location(LOC_DIF.EASY, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310010: Location(LOC_DIF.MEDIUM, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310020: Location(LOC_DIF.MEDIUM, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310030: Location(LOC_DIF.EASY, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310040: Location(LOC_DIF.HARD, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310050: Location(LOC_DIF.EASY, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310070: Location(LOC_DIF.EASY, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310080: Location(LOC_DIF.EASY, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310090: Location(LOC_DIF.EASY, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310100: Location(
        LOC_DIF.MEDIUM, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9, has_flag=51310100
    ),
    1310110: Location(LOC_DIF.MEDIUM, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310120: Location(LOC_DIF.HARD, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310140: Location(LOC_DIF.MEDIUM, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310160: Location(LOC_DIF.EASY, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310180: Location(LOC_DIF.EASY, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310200: Location(LOC_DIF.MEDIUM, AREA.TOMB_OF_THE_GIANTS_POST_LV, 9),
    1310220: Location(LOC_DIF.HARD, AREA.TOMB_OF_THE_GIANTS_POST_LV, 9),
    1310230: Location(LOC_DIF.MEDIUM, AREA.TOMB_OF_THE_GIANTS_POST_LV, 9),
    1310240: Location(
        LOC_DIF.HARD, AREA.TOMB_OF_THE_GIANTS_POST_LV, 9, is_transient=True
    ),
    1310290: Location(LOC_DIF.MEDIUM, AREA.TOMB_OF_THE_GIANTS_POST_LV, 9),
    1310300: Location(LOC_DIF.EASY, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9),
    1310500: Location(
        LOC_DIF.HARD,
        AREA.TOMB_OF_THE_GIANTS_PRE_LV,
        9,
        is_race_key_loc=True,
        default_key="large_divine_ember",
    ),
    1320000: Location(LOC_DIF.EASY, AREA.GREAT_HOLLOW, 9),
    1320020: Location(LOC_DIF.MEDIUM, AREA.GREAT_HOLLOW, 9),
    1320040: Location(LOC_DIF.EASY, AREA.GREAT_HOLLOW, 9),
    1320050: Location(LOC_DIF.EASY, AREA.GREAT_HOLLOW, 9),
    1320060: Location(LOC_DIF.MEDIUM, AREA.GREAT_HOLLOW, 9),
    1320070: Location(LOC_DIF.MEDIUM, AREA.GREAT_HOLLOW, 9),
    1320080: Location(LOC_DIF.HARD, AREA.GREAT_HOLLOW, 9),
    1320090: Location(LOC_DIF.EASY, AREA.GREAT_HOLLOW, 9),
    1320100: Location(LOC_DIF.HARD, AREA.GREAT_HOLLOW, 9),
    1320110: Location(LOC_DIF.EASY, AREA.GREAT_HOLLOW, 9),
    1320120: Location(LOC_DIF.EASY, AREA.GREAT_HOLLOW, 9),
    1320140: Location(LOC_DIF.MEDIUM, AREA.ASH_LAKE, 9),
    1320150: Location(LOC_DIF.EASY, AREA.ASH_LAKE, 9),
    1320160: Location(LOC_DIF.EASY, AREA.ASH_LAKE, 9),
    1320170: Location(LOC_DIF.HARD, AREA.ASH_LAKE, 9),
    1320180: Location(LOC_DIF.EASY, AREA.GREAT_HOLLOW, 9, is_race_key_loc=True),
    1320190: Location(LOC_DIF.MEDIUM, AREA.GREAT_HOLLOW, 9),
    1400020: Location(LOC_DIF.HARD, AREA.BLIGHTTOWN, 9),
    1400040: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9),
    1400050: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9),
    1400060: Location(LOC_DIF.HARD, AREA.BLIGHTTOWN, 9),
    1400080: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9),
    1400090: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9),
    1400100: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9),
    1400130: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9),
    1400140: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9),
    1400150: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9),
    1400160: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9),
    1400180: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9),
    1400190: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9),
    1400210: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9),
    1400230: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9),
    1400250: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9),
    1400260: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9),
    1400270: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9),
    1400280: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9),
    1400290: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9),
    1400300: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9),
    1400310: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9),
    1400320: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9),
    1400340: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9),
    1400350: Location(LOC_DIF.HARD, AREA.BLIGHTTOWN, 9, has_flag=51400350),
    1400360: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 9),
    1400370: Location(LOC_DIF.HARD, AREA.QUELAAGS_DOMAIN, 9, is_transient=True),
    1400500: Location(
        LOC_DIF.EASY,
        AREA.BLIGHTTOWN,
        9,
        is_race_key_loc=True,
        default_key="key_to_new_londo_ruins",
    ),
    1400510: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 9, is_race_key_loc=True),
    1400520: Location(LOC_DIF.HARD, AREA.BLIGHTTOWN, 9, is_race_key_loc=True),
    1410000: Location(LOC_DIF.MEDIUM, AREA.LOST_IZALITH, 9),
    1410010: Location(LOC_DIF.MEDIUM, AREA.LOST_IZALITH, 9),
    1410020: Location(LOC_DIF.MEDIUM, AREA.LOST_IZALITH, 9),
    1410030: Location(LOC_DIF.MEDIUM, AREA.LOST_IZALITH, 9),
    1410050: Location(LOC_DIF.EASY, AREA.DEMON_RUINS_NO_LAVA_PRE_LV, 9),
    1410060: Location(LOC_DIF.MEDIUM, AREA.DEMON_RUINS_LAVA, 9),
    1410080: Location(LOC_DIF.EASY, AREA.DEMON_RUINS_NO_LAVA_PRE_LV, 9),
    1410090: Location(LOC_DIF.MEDIUM, AREA.DEMON_RUINS_NO_LAVA_PRE_LV, 9),
    1410100: Location(
        LOC_DIF.MEDIUM,
        AREA.DEMON_RUINS_NO_LAVA_PRE_LV,
        9,
        is_race_key_loc=True,
        default_key="large_flame_ember",
    ),
    1410140: Location(LOC_DIF.MEDIUM, AREA.DEMON_RUINS_NO_LAVA_PRE_LV, 9),
    1410160: Location(LOC_DIF.EASY, AREA.DEMON_RUINS_NO_LAVA_POST_LV, 9),
    1410180: Location(
        LOC_DIF.MEDIUM, AREA.DEMON_RUINS_NO_LAVA_PRE_LV, 9, has_flag=51410180
    ),
    1410190: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1410200: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1410210: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1410220: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1410230: Location(LOC_DIF.EASY, AREA.DEMON_RUINS_NO_LAVA_POST_LV, 9),
    1410240: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1410250: Location(LOC_DIF.EASY, AREA.DEMON_RUINS_NO_LAVA_POST_LV, 9),
    1410260: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1410270: Location(LOC_DIF.EASY, AREA.DEMON_RUINS_NO_LAVA_POST_LV, 9),
    1410280: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1410290: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1410300: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1410310: Location(LOC_DIF.EASY, AREA.LOST_IZALITH, 9),
    1410320: Location(LOC_DIF.EASY, AREA.LOST_IZALITH, 9),
    1410330: Location(LOC_DIF.HARD, AREA.LOST_IZALITH, 9),
    1410340: Location(LOC_DIF.HARD, AREA.LOST_IZALITH, 9),
    1410350: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1410360: Location(LOC_DIF.MEDIUM, AREA.LOST_IZALITH, 9),
    1410370: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1410380: Location(LOC_DIF.HARD, AREA.LOST_IZALITH, 9),
    1410390: Location(LOC_DIF.MEDIUM, AREA.LOST_IZALITH, 9),
    1410400: Location(LOC_DIF.MEDIUM, AREA.LOST_IZALITH, 9),
    1410410: Location(LOC_DIF.HARD, AREA.LOST_IZALITH, 9, is_race_key_loc=True),
    1410500: Location(LOC_DIF.MEDIUM, AREA.LOST_IZALITH, 9, is_race_key_loc=True),
    1410510: Location(LOC_DIF.EASY, AREA.DEMON_RUINS_NO_LAVA_PRE_LV, 9),
    1410520: Location(LOC_DIF.MEDIUM, AREA.LOST_IZALITH, 9, is_race_key_loc=True),
    1410530: Location(
        LOC_DIF.HARD,
        AREA.DEMON_RUINS_LAVA,
        9,
        is_race_key_loc=True,
        default_key="chaos_flame_ember",
    ),
    1500000: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 9, is_race_key_loc=True),
    1500010: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 9),
    1500020: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 9, is_race_key_loc=True),
    1500030: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1500040: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 9, is_race_key_loc=True),
    1500050: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1500060: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 9),
    1500070: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 9),
    1500080: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 9),
    1500090: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 9, is_race_key_loc=True),
    1500100: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 9, is_race_key_loc=True),
    1500150: Location(
        LOC_DIF.MEDIUM,
        AREA.SENS_FORTRESS,
        9,
        is_race_key_loc=True,
        default_key="cage_key",
    ),
    1500300: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 9),
    1500310: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 9),
    1500320: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 9),
    1500330: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 9),
    1500350: Location(LOC_DIF.HARD, AREA.SENS_FORTRESS, 9),
    1500360: Location(LOC_DIF.HARD, AREA.SENS_FORTRESS, 9),
    1500400: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 9),
    1500410: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 9),
    1500420: Location(LOC_DIF.HARD, AREA.SENS_CAGE, 9),
    1500430: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    1500440: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 9),
    1510000: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 9),
    1510030: Location(LOC_DIF.EASY, AREA.ANOR_LONDO, 9),
    1510040: Location(LOC_DIF.EASY, AREA.ANOR_LONDO, 9),
    1510050: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 9),
    1510060: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 9),
    1510070: Location(LOC_DIF.EASY, AREA.ANOR_LONDO, 9),
    1510080: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 9, is_transient=True),
    1510510: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510520: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510530: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510540: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510560: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510570: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510580: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510590: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510600: Location(LOC_DIF.EASY, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510610: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510620: Location(LOC_DIF.HARD, AREA.DARKMOON_TOMB, 9, is_race_key_loc=True),
    1510650: Location(LOC_DIF.HARD, AREA.DARKMOON_TOMB, 9, is_race_key_loc=True),
    1510660: Location(LOC_DIF.HARD, AREA.DARKMOON_TOMB, 9, is_race_key_loc=True),
    1510670: Location(LOC_DIF.EASY, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510680: Location(LOC_DIF.EASY, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510690: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 9, is_race_key_loc=True),
    1510700: Location(LOC_DIF.EASY, AREA.ANOR_LONDO, 9),
    1600000: Location(LOC_DIF.EASY, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600020: Location(LOC_DIF.EASY, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600030: Location(LOC_DIF.MEDIUM, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600040: Location(LOC_DIF.MEDIUM, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600060: Location(LOC_DIF.EASY, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600070: Location(LOC_DIF.EASY, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600090: Location(LOC_DIF.EASY, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600100: Location(LOC_DIF.EASY, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600110: Location(LOC_DIF.MEDIUM, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600120: Location(LOC_DIF.EASY, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600130: Location(LOC_DIF.MEDIUM, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600140: Location(LOC_DIF.MEDIUM, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600150: Location(LOC_DIF.EASY, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600160: Location(LOC_DIF.MEDIUM, AREA.NEW_LONDO_PRE_SEAL, 9),
    1600170: Location(LOC_DIF.EASY, AREA.VALLEY_OF_DRAKES, 9),
    1600180: Location(LOC_DIF.MEDIUM, AREA.VALLEY_OF_DRAKES, 9),
    1600190: Location(LOC_DIF.EASY, AREA.VALLEY_OF_DRAKES, 9),
    1600200: Location(LOC_DIF.EASY, AREA.VALLEY_OF_DRAKES, 9),
    1600210: Location(LOC_DIF.MEDIUM, AREA.VALLEY_OF_DRAKES, 9),
    1600220: Location(LOC_DIF.MEDIUM, AREA.VALLEY_OF_DRAKES, 9),
    1600250: Location(LOC_DIF.MEDIUM, AREA.NEW_LONDO_POST_SEAL, 9),
    1600260: Location(LOC_DIF.MEDIUM, AREA.NEW_LONDO_POST_SEAL, 9),
    1600270: Location(LOC_DIF.EASY, AREA.NEW_LONDO_POST_SEAL, 9),
    1600280: Location(LOC_DIF.EASY, AREA.NEW_LONDO_POST_SEAL, 9),
    1600290: Location(
        LOC_DIF.HARD, AREA.NEW_LONDO_POST_SEAL_SKIP, 9, is_race_key_loc=True
    ),
    1600310: Location(LOC_DIF.EASY, AREA.NEW_LONDO_POST_SEAL, 9),
    1600330: Location(LOC_DIF.HARD, AREA.NEW_LONDO_POST_SEAL, 9),
    1600360: Location(LOC_DIF.HARD, AREA.POST_4K, 9),
    1600370: Location(LOC_DIF.EASY, AREA.NEW_LONDO_POST_SEAL, 9),
    1600380: Location(LOC_DIF.HARD, AREA.VALLEY_OF_DRAKES, 9),
    1600500: Location(
        LOC_DIF.HARD,
        AREA.NEW_LONDO_POST_SEAL,
        9,
        is_race_key_loc=True,
        default_key="very_large_ember",
    ),
    1600510: Location(
        LOC_DIF.MEDIUM, AREA.NEW_LONDO_POST_SEAL, 9, is_race_key_loc=True
    ),
    1600520: Location(LOC_DIF.MEDIUM, AREA.NEW_LONDO_PRE_SEAL, 9),
    1700000: Location(LOC_DIF.MEDIUM, AREA.DUKES_ARCHIVES, 9),
    1700010: Location(LOC_DIF.EASY, AREA.DUKES_ARCHIVES, 9),
    1700020: Location(LOC_DIF.HARD, AREA.DUKES_ARCHIVES, 9, is_race_key_loc=True),
    1700040: Location(LOC_DIF.HARD, AREA.DUKES_ARCHIVES, 9),
    1700050: Location(LOC_DIF.MEDIUM, AREA.DUKES_ARCHIVES, 9, is_race_key_loc=True),
    1700060: Location(LOC_DIF.HARD, AREA.DUKES_PRISON_EXTRA, 9),
    1700070: Location(LOC_DIF.MEDIUM, AREA.DUKES_PRISON, 9),
    1700080: Location(LOC_DIF.MEDIUM, AREA.DUKES_PRISON_EXTRA, 9),
    1700120: Location(LOC_DIF.MEDIUM, AREA.DUKES_ARCHIVES, 9),
    1700150: Location(LOC_DIF.MEDIUM, AREA.CRYSTAL_CAVE, 9),
    1700160: Location(LOC_DIF.HARD, AREA.CRYSTAL_CAVE, 9),
    1700170: Location(LOC_DIF.MEDIUM, AREA.CRYSTAL_CAVE, 9),
    1700180: Location(LOC_DIF.EASY, AREA.CRYSTAL_CAVE, 9),
    1700200: Location(LOC_DIF.HARD, AREA.DUKES_PRISON_GIANT_CELL, 9),
    1700210: Location(
        LOC_DIF.HARD,
        AREA.DUKES_PRISON,
        9,
        is_race_key_loc=True,
        default_key="archive_prison_extra_key",
    ),
    1700510: Location(LOC_DIF.EASY, AREA.DUKES_ARCHIVES, 9, is_race_key_loc=True),
    1700520: Location(LOC_DIF.MEDIUM, AREA.DUKES_ARCHIVES, 9, is_race_key_loc=True),
    1700530: Location(
        LOC_DIF.HARD,
        AREA.DUKES_ARCHIVES,
        9,
        is_race_key_loc=True,
        default_key="large_magic_ember",
    ),
    1700540: Location(LOC_DIF.MEDIUM, AREA.DUKES_ARCHIVES, 9, is_race_key_loc=True),
    1700560: Location(LOC_DIF.MEDIUM, AREA.DUKES_ARCHIVES, 9, is_race_key_loc=True),
    1700580: Location(LOC_DIF.MEDIUM, AREA.DUKES_ARCHIVES, 9, is_race_key_loc=True),
    1700590: Location(
        LOC_DIF.MEDIUM,
        AREA.DUKES_ARCHIVES,
        9,
        is_race_key_loc=True,
        default_key="archive_tower_giant_cell_key",
    ),
    1700600: Location(
        LOC_DIF.MEDIUM,
        AREA.DUKES_ARCHIVES,
        9,
        is_race_key_loc=True,
        default_key="crystal_ember",
    ),
    1700630: Location(
        LOC_DIF.HARD,
        AREA.DUKES_PRISON,
        9,
        is_race_key_loc=True,
        default_key="archive_tower_giant_door_key",
    ),
    1700640: Location(LOC_DIF.HARD, AREA.DUKES_ARCHIVES, 9, is_transient=True),
    1700650: Location(LOC_DIF.HARD, AREA.DUKES_ARCHIVES, 9),
    1800050: Location(LOC_DIF.HARD, AREA.KILN, 9),
    1810000: Location(LOC_DIF.LEAVE_ALONE, AREA.UNDEAD_ASYLUM, 9),
    1810060: Location(LOC_DIF.HARD, AREA.UNDEAD_ASYLUM_F2_WEST, 9),
    1810070: Location(LOC_DIF.EASY, AREA.UNDEAD_ASYLUM, 9),
    1810080: Location(
        LOC_DIF.MEDIUM,
        AREA.UNDEAD_ASYLUM,
        9,
        is_race_key_loc=True,
        default_key="peculiar_doll",
    ),
    1810100: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810100),
    1810110: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810110),
    1810120: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810120),
    1810130: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810130),
    1810140: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810140),
    1810150: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810150),
    1810160: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810160),
    1810170: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810170),
    1810180: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810180),
    1810190: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810190),
    1810200: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810200),
    1810210: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810210),
    1810220: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810220),
    1810230: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810230),
    1810240: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810240),
    1810250: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810250),
    1810260: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810260),
    1810270: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810270),
    1810280: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810280),
    1810290: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810290),
    1810300: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810300),
    1810310: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810310),
    1810320: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810320),
    1810330: Location(LOC_DIF.STARTING_ITEM, AREA.UNDEAD_ASYLUM, 9, has_flag=51810330),
    9990000: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990010: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990011: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990020: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990021: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990022: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990030: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990031: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990032: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990033: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990034: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990100: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990110: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990500: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990510: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990520: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990530: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990540: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990550: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990560: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990570: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990580: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990590: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990600: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990610: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990620: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990630: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990640: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990650: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990660: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990670: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990680: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990690: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990700: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990710: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990720: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990730: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990740: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990750: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990760: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990770: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990780: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990790: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990800: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990810: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990820: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990830: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990840: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990850: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990860: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990870: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990880: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990890: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    9990900: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    12000000: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[12010000, 12010100, 12030000],
    ),
    12010200: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[12010300],
    ),
    12020000: Location(LOC_DIF.MEDIUM, AREA.DEPTHS, 9, is_transient=True),
    20600000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    20600100: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    20600200: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    22300000: Location(LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 9, is_transient=True),
    22300010: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    22310000: Location(
        LOC_DIF.HARD, AREA.DEMON_RUINS_NO_LAVA_POST_LV, 9, is_transient=True
    ),
    22400000: Location(
        LOC_DIF.NPC_MEDIUM,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[22400100],
    ),
    22500000: Location(
        LOC_DIF.NPC_HARD,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[22500200],
    ),
    22600000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    22600100: Location(LOC_DIF.IGNORE, AREA.NONE, 9),
    22700000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    22700100: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    22800000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    22800100: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    23000000: Location(
        LOC_DIF.HARD,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        linked_locations=[23000100, 23000200, 23000300, 23000400, 23000500],
        has_cumul_flag=CumulFlag(9164, 7, 2, 100, 10),
    ),
    23000001: Location(LOC_DIF.HARD, AREA.CATACOMBS, 8, is_transient=True),
    23000101: Location(LOC_DIF.UPGRADE, AREA.UNDEAD_PARISH, 8, is_transient=True),
    23000201: Location(LOC_DIF.UPGRADE, AREA.SENS_FORTRESS, 8, is_transient=True),
    23000301: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    23000401: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 8, is_transient=True),
    23000501: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 1, is_transient=True),
    23100000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    23300000: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[23300100],
    ),
    23700000: Location(
        LOC_DIF.NPC_HARD,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[23700100, 23700200],
    ),
    23800000: Location(
        LOC_DIF.NPC_MEDIUM,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[23800100],
    ),
    23900000: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    23900220: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    24000000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    24100000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    24100300: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    24100400: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    24300000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    25000000: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25000300, 25001000, 25002200, 25002500, 25003000, 25003200],
    ),
    25000100: Location(
        LOC_DIF.EMPTY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25001100, 25002300, 25003100],
    ),
    25000200: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25001200, 25002100, 25002400],
    ),
    25002000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    25004000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    25100000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    25100100: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_BURG, 9, is_transient=True),
    25200000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    25300200: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    25400000: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25401000, 25402000],
    ),
    25400100: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25401100, 25402100],
    ),
    25400200: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25401200, 25402200],
    ),
    25500000: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25502000],
    ),
    25500100: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25501000, 25502100, 25503100, 25503200],
    ),
    25500200: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25502200],
    ),
    25503000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    25600000: Location(
        LOC_DIF.NPC_MEDIUM,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25600300],
    ),
    25600100: Location(LOC_DIF.IGNORE, AREA.NONE, 9, is_transient=True),
    25600200: Location(
        LOC_DIF.NPC_MEDIUM,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25600400],
    ),
    25601000: Location(
        LOC_DIF.NPC_MEDIUM,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25601300],
    ),
    25601100: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    25601200: Location(
        LOC_DIF.NPC_MEDIUM,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[25601400],
    ),
    25700000: Location(LOC_DIF.IGNORE, AREA.NONE, 9),
    25700100: Location(LOC_DIF.HARD, AREA.UNDEAD_PARISH, 1, is_transient=True),
    25700101: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 8, is_transient=True),
    25700200: Location(LOC_DIF.IGNORE, AREA.NONE, 9),
    25701000: Location(LOC_DIF.IGNORE, AREA.NONE, 9, linked_locations=[25701200]),
    25701100: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    25702000: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    25702100: Location(LOC_DIF.IGNORE, AREA.NONE, 9, linked_locations=[25702200]),
    26400000: Location(LOC_DIF.HARD, AREA.UNDEAD_PARISH, 9, is_transient=True),
    26500000: Location(
        LOC_DIF.HARD,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        has_cumul_flag=CumulFlag(9172, 5, 2, 100, 10),
    ),
    26600000: Location(
        LOC_DIF.MEDIUM,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        has_cumul_flag=CumulFlag(9116, 1, 10, 100, 100),
    ),
    26700000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    26800000: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    26900000: Location(
        LOC_DIF.NPC_MEDIUM,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[26900200, 26900300],
    ),
    26900100: Location(
        LOC_DIF.LEAVE_ALONE, AREA.DUKES_PRISON, 9, is_transient=True, has_flag=51700990
    ),
    27000000: Location(
        LOC_DIF.NPC_HARD,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[27000100],
    ),
    27100000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    27100100: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    27100200: Location(
        LOC_DIF.HARD,
        AREA.DUKES_ARCHIVES,
        9,
        is_race_key_loc=True,
        default_key="broken_pendant",
    ),
    27110000: Location(LOC_DIF.EMPTY, AREA.DARKROOT_BASIN, 9),
    27110100: Location(LOC_DIF.EMPTY, AREA.DUKES_ARCHIVES, 9, is_transient=True),
    27300000: Location(LOC_DIF.EMPTY, AREA.PAINTED_WORLD, 9),
    27310000: Location(LOC_DIF.HARD, AREA.PAINTED_WORLD, 9, is_transient=True),
    27800000: Location(
        LOC_DIF.HARD,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        linked_locations=[
            27801000,
            27801010,
            27801020,
            27801030,
            27802000,
            27802010,
            27803000,
            27803100,
        ],
        has_cumul_flag=CumulFlag(9124, 6, 1, 1000, 10),
    ),
    27800001: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 8, is_transient=True),
    27801001: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 8, is_transient=True),
    27801011: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 8, is_transient=True),
    27801021: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 8, is_transient=True),
    27801031: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 8, is_transient=True),
    27802001: Location(LOC_DIF.HARD, AREA.DUKES_ARCHIVES, 8, is_transient=True),
    27802011: Location(LOC_DIF.HARD, AREA.DUKES_ARCHIVES, 8, is_transient=True),
    27803001: Location(
        LOC_DIF.HARD,
        AREA.OOLACILE_TOWNSHIP,
        8,
        is_race_key_loc=True,
        default_key="crest_key",
    ),
    27803101: Location(LOC_DIF.HARD, AREA.OOLACILE_TOWNSHIP, 1),
    27900000: Location(LOC_DIF.HARD, AREA.UNDEAD_BURG, 1, is_race_key_loc=True),
    27900001: Location(
        LOC_DIF.NPC_HARD,
        AREA.NPC_RNG_DROP,
        8,
        is_transient=True,
        linked_locations=[27905000, 27907002],
    ),
    27900100: Location(LOC_DIF.HARD, AREA.UNDEAD_PARISH, 1, is_race_key_loc=True),
    27900101: Location(
        LOC_DIF.NPC_HARD,
        AREA.NPC_RNG_DROP,
        8,
        is_transient=True,
        linked_locations=[27905100],
    ),
    27901000: Location(LOC_DIF.HARD, AREA.DARKROOT_BASIN, 1, is_race_key_loc=True),
    27901001: Location(
        LOC_DIF.NPC_HARD,
        AREA.NPC_RNG_DROP,
        8,
        is_transient=True,
        linked_locations=[27903001, 27905300],
    ),
    27902000: Location(LOC_DIF.HARD, AREA.CATACOMBS, 1, is_race_key_loc=True),
    27902001: Location(
        LOC_DIF.NPC_HARD,
        AREA.NPC_RNG_DROP,
        8,
        is_transient=True,
        linked_locations=[27905200],
    ),
    27903000: Location(
        LOC_DIF.HARD, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 1, is_race_key_loc=True
    ),
    27907000: Location(LOC_DIF.HARD, AREA.UNDEAD_ASYLUM, 1, is_race_key_loc=True),
    27907001: Location(LOC_DIF.UPGRADE, AREA.UNDEAD_ASYLUM, 1, is_transient=True),
    27910000: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    28000000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    28000100: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    28100000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    28110000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    28200000: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    28301000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    28400000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    28400100: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    28400200: Location(LOC_DIF.HARD, AREA.PAINTED_WORLD, 9, is_transient=True),
    28600000: Location(LOC_DIF.UPGRADE, AREA.SENS_FORTRESS, 9, is_transient=True),
    28600100: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 9, is_transient=True),
    28600200: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    28700000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    28701000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    29000000: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[29001000, 29002000, 29003000],
    ),
    29000100: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[29001100, 29002100, 29003100],
    ),
    29000200: Location(
        LOC_DIF.NPC_EASY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[29001200, 29002200, 29003200],
    ),
    29100000: Location(
        LOC_DIF.NPC_MEDIUM,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[29100200, 29101100],
    ),
    29100100: Location(
        LOC_DIF.NPC_MEDIUM,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[29101000, 29101300],
    ),
    29101200: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    29101400: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    29200000: Location(LOC_DIF.HARD, AREA.CATACOMBS, 9, is_transient=True),
    29200200: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    29300000: Location(
        LOC_DIF.NPC_HARD,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[29300100],
    ),
    29400000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    29500000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    29600000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    30900000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    32000000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    32100000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    32100100: Location(LOC_DIF.MEDIUM, AREA.QUELAAGS_DOMAIN, 9, is_transient=True),
    32200000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    32300000: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1),
    32300100: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    32400000: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    32500000: Location(
        LOC_DIF.NPC_MEDIUM,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[32500100],
    ),
    32700000: Location(
        LOC_DIF.NPC_MEDIUM,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[32700100],
    ),
    33000000: Location(
        LOC_DIF.UPGRADE,
        AREA.NPC_RNG_DROP,
        1,
        is_transient=True,
        linked_locations=[
            33001000,
            33002000,
            33003000,
            33004000,
            33005000,
            33006000,
            33007000,
            33007100,
            33007200,
            33007300,
        ],
    ),
    33000001: Location(LOC_DIF.RANDOM_UPGRADE, AREA.NPC_RNG_DROP, 8, is_transient=True),
    33001001: Location(LOC_DIF.RANDOM_UPGRADE, AREA.NPC_RNG_DROP, 8, is_transient=True),
    33002001: Location(LOC_DIF.RANDOM_UPGRADE, AREA.NPC_RNG_DROP, 8, is_transient=True),
    33003001: Location(LOC_DIF.RANDOM_UPGRADE, AREA.NPC_RNG_DROP, 8, is_transient=True),
    33004001: Location(LOC_DIF.RANDOM_UPGRADE, AREA.NPC_RNG_DROP, 8, is_transient=True),
    33005001: Location(LOC_DIF.RANDOM_UPGRADE, AREA.NPC_RNG_DROP, 8, is_transient=True),
    33006001: Location(LOC_DIF.RANDOM_UPGRADE, AREA.NPC_RNG_DROP, 8, is_transient=True),
    33007001: Location(LOC_DIF.RANDOM_UPGRADE, AREA.NPC_RNG_DROP, 8, is_transient=True),
    33007101: Location(LOC_DIF.RANDOM_UPGRADE, AREA.NPC_RNG_DROP, 8, is_transient=True),
    33007201: Location(LOC_DIF.RANDOM_UPGRADE, AREA.NPC_RNG_DROP, 8, is_transient=True),
    33007301: Location(LOC_DIF.RANDOM_UPGRADE, AREA.NPC_RNG_DROP, 8, is_transient=True),
    33200000: Location(
        LOC_DIF.MEDIUM, AREA.TOMB_OF_THE_GIANTS_PRE_LV, 9, is_transient=True
    ),
    33200100: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    33200200: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    33300000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    33300100: Location(LOC_DIF.MEDIUM, AREA.DUKES_PRISON, 9, is_transient=True),
    33300200: Location(LOC_DIF.MEDIUM, AREA.DUKES_PRISON, 9, is_transient=True),
    33400000: Location(
        LOC_DIF.EMPTY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[33400100, 33400200],
    ),
    33410000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    33500000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    33700000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    33800000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    33900000: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    34000000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    34100000: Location(
        LOC_DIF.NPC_MEDIUM,
        AREA.NPC_RNG_DROP,
        1,
        is_transient=True,
        linked_locations=[34100100],
    ),
    34200000: Location(LOC_DIF.HARD, AREA.PAINTED_WORLD, 9, is_transient=True),
    34200200: Location(LOC_DIF.HARD, AREA.VALLEY_OF_DRAKES, 9),
    34210100: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    34220000: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1),
    34300000: Location(LOC_DIF.EMPTY, AREA.UNDEAD_BURG, 9, is_transient=True),
    34310000: Location(LOC_DIF.HARD, AREA.UNDEAD_BURG, 9, is_transient=True),
    34500000: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    34510000: Location(LOC_DIF.HARD, AREA.ASH_LAKE, 9),
    34600000: Location(
        LOC_DIF.HARD,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        linked_locations=[34610000],
        has_cumul_flag=CumulFlag(9156, 2, 20, 100, 20),
    ),
    34710000: Location(LOC_DIF.LEAVE_ALONE, AREA.OOLACILE_SANCTUARY, 9),
    34720000: Location(LOC_DIF.HARD, AREA.OOLACILE_SANCTUARY, 9, is_transient=True),
    34720010: Location(LOC_DIF.HARD, AREA.OOLACILE_SANCTUARY, 9, is_transient=True),
    34720020: Location(LOC_DIF.HARD, AREA.OOLACILE_SANCTUARY, 9, is_transient=True),
    34800000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    34800100: Location(LOC_DIF.HARD, AREA.LOST_IZALITH, 9, is_transient=True),
    34900000: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34900100: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34900200: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34900300: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34900400: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34900500: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34900600: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34900700: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34900800: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34900900: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34901000: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34901100: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34901200: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34901300: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34901400: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34910000: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34910100: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34910200: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34910300: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34910400: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34910500: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34910600: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34910700: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34910800: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34910900: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34911000: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34911100: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34911200: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34911300: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34911400: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34920000: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34920100: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34920200: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34920300: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34920400: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34920500: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34920600: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34920700: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34920800: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34920900: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34921000: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34921100: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34921200: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34921300: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    34921400: Location(LOC_DIF.LEAVE_ALONE, AREA.MOVING_NPC, 9, is_transient=True),
    35000000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    35010000: Location(
        LOC_DIF.EMPTY,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[35010100],
    ),
    35100000: Location(LOC_DIF.LEAVE_ALONE, AREA.FIRELINK, 9),
    35200200: Location(
        LOC_DIF.NPC_HARD,
        AREA.NPC_RNG_DROP,
        9,
        is_transient=True,
        linked_locations=[35200500],
    ),
    35300000: Location(LOC_DIF.HARD, AREA.ASH_LAKE, 9),
    35300100: Location(LOC_DIF.HARD, AREA.DARKROOT_BASIN, 9),
    35310000: Location(
        LOC_DIF.LEAVE_ALONE, AREA.DARKROOT_BASIN, 9, linked_locations=[35310100]
    ),
    40900000: Location(LOC_DIF.MEDIUM, AREA.ROYAL_WOOD, 9, is_transient=True),
    40901000: Location(
        LOC_DIF.LEAVE_ALONE, AREA.OOLACILE_TOWNSHIP, 9, is_transient=True
    ),
    41000000: Location(LOC_DIF.LEAVE_ALONE, AREA.ROYAL_WOOD, 9),
    41100001: Location(LOC_DIF.HARD, AREA.KALAMEET_FIGHT, 8, is_transient=True),
    41200000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    41300000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    41301000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    41500000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    41600000: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    41601000: Location(LOC_DIF.HARD, AREA.OOLACILE_TOWNSHIP, 9),
    41700000: Location(LOC_DIF.NPC_MEDIUM, AREA.NPC_RNG_DROP, 9, is_transient=True),
    41710000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    41720000: Location(LOC_DIF.NPC_EASY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    41800000: Location(LOC_DIF.NPC_HARD, AREA.NPC_RNG_DROP, 9, is_transient=True),
    41900000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    45000000: Location(LOC_DIF.LEAVE_ALONE, AREA.CHASM_OF_THE_ABYSS, 9),
    45100000: Location(LOC_DIF.EMPTY, AREA.KALAMEET_FIGHT, 9),
    45110000: Location(LOC_DIF.HARD, AREA.KALAMEET_FIGHT, 9, is_transient=True),
    45200000: Location(LOC_DIF.HARD, AREA.CHASM_OF_THE_ABYSS, 9, is_transient=True),
    52000000: Location(LOC_DIF.LEAVE_ALONE, AREA.DEMON_RUINS_NO_LAVA_PRE_LV, 9),
    52010000: Location(
        LOC_DIF.LEAVE_ALONE, AREA.DEMON_RUINS_NO_LAVA_PRE_LV, 9, is_transient=True
    ),
    52020000: Location(
        LOC_DIF.LEAVE_ALONE, AREA.DEMON_RUINS_NO_LAVA_PRE_LV, 9, is_transient=True
    ),
    52100000: Location(LOC_DIF.LEAVE_ALONE, AREA.DARKROOT_GARDEN, 9),
    52200000: Location(LOC_DIF.LEAVE_ALONE, AREA.TOMB_OF_THE_GIANTS_POST_LV, 9),
    52300000: Location(LOC_DIF.LEAVE_ALONE, AREA.LOST_IZALITH, 9),
    52400000: Location(LOC_DIF.LEAVE_ALONE, AREA.LOST_IZALITH, 9),
    52500000: Location(LOC_DIF.LEAVE_ALONE, AREA.DEMON_RUINS_NO_LAVA_PRE_LV, 9),
    52600000: Location(LOC_DIF.LEAVE_ALONE, AREA.DEPTHS, 9),
    52610000: Location(LOC_DIF.HARD, AREA.DEPTHS, 9, is_transient=True),
    52710000: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 9, is_transient=True),
    52800000: Location(LOC_DIF.LEAVE_ALONE, AREA.QUELAAGS_DOMAIN, 9),
    52900000: Location(LOC_DIF.LEAVE_ALONE, AREA.DUKES_ARCHIVES, 9),
    52900100: Location(LOC_DIF.LEAVE_ALONE, AREA.CRYSTAL_CAVE, 9),
    52910000: Location(LOC_DIF.HARD, AREA.CRYSTAL_CAVE, 9, is_transient=True),
    53100000: Location(LOC_DIF.LEAVE_ALONE, AREA.ANOR_LONDO, 9),
    53300000: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    53300100: Location(LOC_DIF.IGNORE, AREA.NONE, 1),
    53400000: Location(LOC_DIF.HARD, AREA.QUELAAGS_DOMAIN, 9, is_transient=True),
    53500000: Location(
        LOC_DIF.HARD,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        linked_locations=[53500100],
        has_cumul_flag=CumulFlag(9132, 3, 3, 100, 10),
    ),
    53500001: Location(
        LOC_DIF.MEDIUM,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        has_cumul_flag=CumulFlag(9140, 2, 3, 100, 10),
    ),
    53500002: Location(
        LOC_DIF.MEDIUM,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        linked_locations=[53500101],
        has_cumul_flag=CumulFlag(9148, 3, 3, 100, 100),
    ),
    53510000: Location(LOC_DIF.LEAVE_ALONE, AREA.ANOR_LONDO, 10, is_transient=True),
    53520000: Location(LOC_DIF.HARD, AREA.UNDEAD_PARISH, 9, is_transient=True),
    53530000: Location(LOC_DIF.HARD, AREA.ANOR_LONDO, 9, is_transient=True),
    53600000: Location(LOC_DIF.EMPTY, AREA.NPC_RNG_DROP, 9, is_transient=True),
    53610000: Location(LOC_DIF.EMPTY, AREA.DARKROOT_FOREST, 9, is_transient=True),
    53900000: Location(LOC_DIF.LEAVE_ALONE, AREA.POST_4K, 1),
    53900100: Location(LOC_DIF.LEAVE_ALONE, AREA.POST_4K, 1),
    54000000: Location(LOC_DIF.LEAVE_ALONE, AREA.LOST_IZALITH, 9),
    54010000: Location(LOC_DIF.LEAVE_ALONE, AREA.LOST_IZALITH, 9),
    # Shop locations:
    60000001: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60001101: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001102: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001103: Location(LOC_DIF.SHOP_MEDIUM, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001104: Location(LOC_DIF.SHOP_MEDIUM, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001107: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001108: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001110: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001111: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001112: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001113: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001114: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001115: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001116: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001117: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001118: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001119: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001120: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001121: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001122: Location(LOC_DIF.EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001123: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001124: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001125: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001126: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001127: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001128: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001129: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001130: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001131: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001132: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_BURG, 1, is_transient=True),
    60001133: Location(
        LOC_DIF.MEDIUM,
        AREA.UNDEAD_BURG,
        1,
        is_transient=True,
        linked_locations=[60001501],
    ),
    60001200: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001201: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001202: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001203: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001204: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001205: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001206: Location(
        LOC_DIF.SHOP_MEDIUM, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True
    ),
    60001207: Location(LOC_DIF.MEDIUM, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001208: Location(
        LOC_DIF.SHOP_MEDIUM, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True
    ),
    60001209: Location(
        LOC_DIF.SHOP_MEDIUM, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True
    ),
    60001210: Location(
        LOC_DIF.SHOP_MEDIUM, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True
    ),
    60001211: Location(LOC_DIF.MEDIUM, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001212: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001213: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001214: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001215: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001216: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001217: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001218: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001219: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60001220: Location(LOC_DIF.SHOP_EASY, AREA.LOWER_UNDEAD_BURG, 1, is_transient=True),
    60005300: Location(LOC_DIF.SHOP_EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005301: Location(LOC_DIF.SHOP_MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005302: Location(LOC_DIF.SHOP_MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005303: Location(LOC_DIF.SHOP_MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005304: Location(LOC_DIF.SHOP_HARD, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005306: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005307: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005308: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005309: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005310: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005311: Location(LOC_DIF.EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005312: Location(LOC_DIF.SHOP_EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005313: Location(LOC_DIF.SHOP_EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005314: Location(LOC_DIF.SHOP_EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005315: Location(LOC_DIF.SHOP_EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005316: Location(LOC_DIF.SHOP_EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005317: Location(LOC_DIF.SHOP_EASY, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005318: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005319: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005320: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005321: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005322: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005323: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005324: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005325: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005326: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005327: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005328: Location(LOC_DIF.MEDIUM, AREA.SENS_FORTRESS, 1, is_transient=True),
    60005329: Location(LOC_DIF.HARD, AREA.SENS_FORTRESS, 1, is_transient=True),
    60001400: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001402: Location(
        LOC_DIF.EASY,
        AREA.UNDEAD_PARISH,
        1,
        is_transient=True,
        linked_locations=[60006215, 60006302],
    ),
    60001403: Location(
        LOC_DIF.EASY,
        AREA.UNDEAD_PARISH,
        1,
        is_transient=True,
        linked_locations=[60006216, 60006303],
    ),
    60001404: Location(
        LOC_DIF.EASY,
        AREA.UNDEAD_PARISH,
        1,
        is_transient=True,
        linked_locations=[60001106, 60006217, 60006304],
    ),
    60001405: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001406: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001407: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001408: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001409: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001410: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001411: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001412: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001413: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001414: Location(LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001415: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001416: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001417: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001418: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001419: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001420: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60001500: Location(LOC_DIF.EASY, AREA.MOVING_NPC, 1, is_transient=True),
    60001502: Location(LOC_DIF.EASY, AREA.MOVING_NPC, 1, is_transient=True),
    60001503: Location(LOC_DIF.EASY, AREA.MOVING_NPC, 1, is_transient=True),
    60001504: Location(LOC_DIF.EASY, AREA.MOVING_NPC, 1, is_transient=True),
    60001505: Location(LOC_DIF.MEDIUM, AREA.MOVING_NPC, 1, is_transient=True),
    60001506: Location(LOC_DIF.MEDIUM, AREA.MOVING_NPC, 1, is_transient=True),
    60001507: Location(LOC_DIF.HARD, AREA.MOVING_NPC, 1, is_transient=True),
    60001508: Location(LOC_DIF.HARD, AREA.MOVING_NPC, 1, is_transient=True),
    60001509: Location(LOC_DIF.SHOP_EASY, AREA.MOVING_NPC, 1, is_transient=True),
    60001510: Location(LOC_DIF.SHOP_EASY, AREA.MOVING_NPC, 1, is_transient=True),
    60001511: Location(LOC_DIF.SHOP_EASY, AREA.MOVING_NPC, 1, is_transient=True),
    60001512: Location(LOC_DIF.SHOP_EASY, AREA.MOVING_NPC, 1, is_transient=True),
    60001513: Location(LOC_DIF.SHOP_EASY, AREA.MOVING_NPC, 1, is_transient=True),
    60001514: Location(LOC_DIF.SHOP_MEDIUM, AREA.MOVING_NPC, 1, is_transient=True),
    60001550: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807020, is_transient=True
    ),
    60001551: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807030, is_transient=True
    ),
    60001552: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807040, is_transient=True
    ),
    60001553: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807050, is_transient=True
    ),
    60001554: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807060, is_transient=True
    ),
    60001555: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807070, is_transient=True
    ),
    60001556: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807080, is_transient=True
    ),
    60001557: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807090, is_transient=True
    ),
    60001558: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807100, is_transient=True
    ),
    60001559: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807110, is_transient=True
    ),
    60001560: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807120, is_transient=True
    ),
    60001561: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807130, is_transient=True
    ),
    60001562: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807230, is_transient=True
    ),
    60001563: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807170, is_transient=True
    ),
    60001564: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807180, is_transient=True
    ),
    60001565: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11807190, is_transient=True
    ),
    60001566: Location(
        LOC_DIF.HARD, AREA.FIRELINK, 1, has_flag=11807240, is_transient=True
    ),
    60001567: Location(
        LOC_DIF.HARD, AREA.FIRELINK, 1, has_flag=11807200, is_transient=True
    ),
    60001568: Location(
        LOC_DIF.HARD, AREA.FIRELINK, 1, has_flag=11807210, is_transient=True
    ),
    60001569: Location(
        LOC_DIF.HARD, AREA.FIRELINK, 1, has_flag=11807220, is_transient=True
    ),
    60001580: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60001581: Location(
        LOC_DIF.HARD, AREA.FIRELINK, 1, has_flag=11217060, is_transient=True
    ),
    60001582: Location(
        LOC_DIF.HARD, AREA.FIRELINK, 1, has_flag=11217070, is_transient=True
    ),
    60001583: Location(
        LOC_DIF.HARD, AREA.FIRELINK, 1, has_flag=11217080, is_transient=True
    ),
    60001584: Location(
        LOC_DIF.HARD, AREA.FIRELINK, 1, has_flag=11217090, is_transient=True
    ),
    60001600: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60001601: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60001602: Location(LOC_DIF.SHOP_HARD, AREA.FIRELINK, 1, is_transient=True),
    60001603: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60001604: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60001605: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60001606: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60001607: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60001608: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60001609: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60001610: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60001611: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60001612: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60001613: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60001614: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60001615: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60001616: Location(LOC_DIF.HARD, AREA.FIRELINK, 1, is_transient=True),
    60001617: Location(LOC_DIF.HARD, AREA.FIRELINK, 1, is_transient=True),
    60001700: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 1, is_transient=True),
    60001701: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 1, is_transient=True),
    60001702: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 1, is_transient=True),
    60001703: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 1, is_transient=True),
    60001704: Location(LOC_DIF.EASY, AREA.BLIGHTTOWN, 1, is_transient=True),
    60001705: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 1, is_transient=True),
    60001706: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 1, is_transient=True),
    60001707: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 1, is_transient=True),
    60001708: Location(LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 1, is_transient=True),
    60001709: Location(LOC_DIF.HARD, AREA.BLIGHTTOWN, 1, is_transient=True),
    60002000: Location(
        LOC_DIF.EASY, AREA.FIRELINK, 1, has_flag=11027130, is_transient=True
    ),
    60002001: Location(
        LOC_DIF.EASY, AREA.FIRELINK, 1, has_flag=11027140, is_transient=True
    ),
    60002002: Location(
        LOC_DIF.EASY, AREA.FIRELINK, 1, has_flag=11027150, is_transient=True
    ),
    60002003: Location(
        LOC_DIF.EASY, AREA.FIRELINK, 1, has_flag=11027160, is_transient=True
    ),
    60002004: Location(
        LOC_DIF.EASY, AREA.FIRELINK, 1, has_flag=11027170, is_transient=True
    ),
    60002005: Location(
        LOC_DIF.EASY, AREA.FIRELINK, 1, has_flag=11027180, is_transient=True
    ),
    60002006: Location(
        LOC_DIF.EASY, AREA.FIRELINK, 1, has_flag=11027190, is_transient=True
    ),
    60002007: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11027200, is_transient=True
    ),
    60002008: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11027210, is_transient=True
    ),
    60002009: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11027220, is_transient=True
    ),
    60002010: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60002020: Location(
        LOC_DIF.MEDIUM, AREA.FIRELINK, 1, has_flag=11027230, is_transient=True
    ),
    60002021: Location(
        LOC_DIF.HARD, AREA.FIRELINK, 1, has_flag=11027240, is_transient=True
    ),
    60002100: Location(LOC_DIF.EASY, AREA.NEW_LONDO_PRE_SEAL, 1, is_transient=True),
    60002101: Location(LOC_DIF.EASY, AREA.NEW_LONDO_PRE_SEAL, 1, is_transient=True),
    60002102: Location(
        LOC_DIF.LEAVE_ALONE, AREA.NEW_LONDO_PRE_SEAL, 1, is_transient=True
    ),
    60002200: Location(
        LOC_DIF.EASY, AREA.MOVING_NPC, 1, is_transient=True, linked_locations=[60006502]
    ),
    60002201: Location(
        LOC_DIF.EASY, AREA.MOVING_NPC, 1, is_transient=True, linked_locations=[60006503]
    ),
    60002202: Location(
        LOC_DIF.EASY,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        linked_locations=[60006504],
        default_key="cast_light",
    ),
    60002203: Location(
        LOC_DIF.MEDIUM,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        linked_locations=[60006505],
    ),
    60002204: Location(
        LOC_DIF.MEDIUM,
        AREA.MOVING_NPC,
        1,
        is_transient=True,
        linked_locations=[60006506],
    ),
    60002205: Location(LOC_DIF.MEDIUM, AREA.MOVING_NPC, 1, is_transient=True),
    60002400: Location(
        LOC_DIF.MEDIUM, AREA.MOVING_NPC, 1, has_flag=11607000, is_transient=True
    ),
    60002401: Location(LOC_DIF.SHOP_MEDIUM, AREA.MOVING_NPC, 1, is_transient=True),
    60003000: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60003001: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60003002: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60003003: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60003004: Location(LOC_DIF.HARD, AREA.FIRELINK, 1, is_transient=True),
    60003200: Location(
        LOC_DIF.LEAVE_ALONE,
        AREA.QUELAAGS_DOMAIN,
        1,
        has_flag=11407080,
        is_transient=True,
    ),
    60003210: Location(LOC_DIF.SHOP_HARD, AREA.QUELAAGS_DOMAIN, 1, is_transient=True),
    60003211: Location(LOC_DIF.MEDIUM, AREA.QUELAAGS_DOMAIN, 1, is_transient=True),
    60003212: Location(LOC_DIF.HARD, AREA.QUELAAGS_DOMAIN, 1, is_transient=True),
    60003400: Location(
        LOC_DIF.EASY, AREA.BLIGHTTOWN, 1, has_flag=11407120, is_transient=True
    ),
    60003401: Location(
        LOC_DIF.EASY, AREA.BLIGHTTOWN, 1, has_flag=11407130, is_transient=True
    ),
    60003402: Location(
        LOC_DIF.EASY, AREA.BLIGHTTOWN, 1, has_flag=11407150, is_transient=True
    ),
    60003403: Location(
        LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 1, has_flag=11407160, is_transient=True
    ),
    60003404: Location(
        LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 1, has_flag=11407170, is_transient=True
    ),
    60003405: Location(
        LOC_DIF.MEDIUM, AREA.BLIGHTTOWN, 1, has_flag=11407140, is_transient=True
    ),
    60003406: Location(
        LOC_DIF.HARD, AREA.BLIGHTTOWN, 1, has_flag=11407180, is_transient=True
    ),
    60003407: Location(
        LOC_DIF.HARD, AREA.BLIGHTTOWN, 1, has_flag=11407190, is_transient=True
    ),
    60004000: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60004001: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60004002: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60004003: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60004004: Location(LOC_DIF.EASY, AREA.FIRELINK, 1, is_transient=True),
    60004005: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60004006: Location(LOC_DIF.MEDIUM, AREA.FIRELINK, 1, is_transient=True),
    60004200: Location(
        LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, has_flag=11017050, is_transient=True
    ),
    60004201: Location(
        LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, has_flag=11017060, is_transient=True
    ),
    60004205: Location(
        LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, has_flag=11017100, is_transient=True
    ),
    60004202: Location(
        LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, has_flag=11017070, is_transient=True
    ),
    60004203: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 1, has_flag=11017080, is_transient=True
    ),
    60004204: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 1, has_flag=11017090, is_transient=True
    ),
    60004206: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 1, has_flag=11017110, is_transient=True
    ),
    60004207: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 1, has_flag=11017120, is_transient=True
    ),
    60004208: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 1, has_flag=11017130, is_transient=True
    ),
    60004209: Location(LOC_DIF.HARD, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60004400: Location(
        LOC_DIF.LEAVE_ALONE, AREA.UNDEAD_PARISH, 1, has_flag=11607020, is_transient=True
    ),
    60004401: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60004402: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60004403: Location(
        LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, has_flag=11607030, is_transient=True
    ),
    60004404: Location(LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60004405: Location(
        LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, has_flag=11607050, is_transient=True
    ),
    60004406: Location(
        LOC_DIF.EASY, AREA.UNDEAD_PARISH, 1, has_flag=11607060, is_transient=True
    ),
    60004407: Location(
        LOC_DIF.MEDIUM, AREA.UNDEAD_PARISH, 1, has_flag=11607080, is_transient=True
    ),
    60004408: Location(LOC_DIF.SHOP_EASY, AREA.UNDEAD_PARISH, 1, is_transient=True),
    60005000: Location(
        LOC_DIF.EASY, AREA.MOVING_NPC, 1, has_flag=11707000, is_transient=True
    ),
    60005001: Location(
        LOC_DIF.EASY, AREA.MOVING_NPC, 1, has_flag=11707010, is_transient=True
    ),
    60005002: Location(
        LOC_DIF.EASY, AREA.MOVING_NPC, 1, has_flag=11707020, is_transient=True
    ),
    60005003: Location(
        LOC_DIF.MEDIUM, AREA.MOVING_NPC, 1, has_flag=11707030, is_transient=True
    ),
    60005004: Location(
        LOC_DIF.MEDIUM, AREA.MOVING_NPC, 1, has_flag=11707060, is_transient=True
    ),
    60005005: Location(
        LOC_DIF.MEDIUM, AREA.MOVING_NPC, 1, has_flag=11707070, is_transient=True
    ),
    60005006: Location(
        LOC_DIF.MEDIUM, AREA.MOVING_NPC, 1, has_flag=11707040, is_transient=True
    ),
    60005007: Location(
        LOC_DIF.HARD, AREA.MOVING_NPC, 1, has_flag=11707050, is_transient=True
    ),
    60005020: Location(
        LOC_DIF.MEDIUM, AREA.DUKES_ARCHIVES, 1, has_flag=11707090, is_transient=True
    ),
    60005021: Location(
        LOC_DIF.HARD, AREA.DUKES_ARCHIVES, 1, has_flag=11707100, is_transient=True
    ),
    60005022: Location(
        LOC_DIF.HARD, AREA.DUKES_ARCHIVES, 1, has_flag=11707110, is_transient=True
    ),
    60006100: Location(LOC_DIF.SHOP_HARD, AREA.POST_4K, 1, is_transient=True),
    60006200: Location(LOC_DIF.EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006201: Location(LOC_DIF.EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006202: Location(LOC_DIF.SHOP_EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006203: Location(LOC_DIF.SHOP_EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006204: Location(LOC_DIF.SHOP_EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006205: Location(LOC_DIF.SHOP_EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006206: Location(LOC_DIF.SHOP_EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006207: Location(LOC_DIF.SHOP_EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006208: Location(LOC_DIF.SHOP_EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006209: Location(LOC_DIF.SHOP_EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006210: Location(LOC_DIF.SHOP_EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006211: Location(LOC_DIF.EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006212: Location(LOC_DIF.EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006213: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 1, is_transient=True),
    60006214: Location(LOC_DIF.MEDIUM, AREA.ANOR_LONDO, 1, is_transient=True),
    60006218: Location(LOC_DIF.SHOP_EASY, AREA.ANOR_LONDO, 1, is_transient=True),
    60006219: Location(LOC_DIF.SHOP_MEDIUM, AREA.ANOR_LONDO, 1, is_transient=True),
    60006220: Location(LOC_DIF.SHOP_MEDIUM, AREA.ANOR_LONDO, 1, is_transient=True),
    60006221: Location(LOC_DIF.SHOP_HARD, AREA.ANOR_LONDO, 1, is_transient=True),
    60006300: Location(LOC_DIF.SHOP_MEDIUM, AREA.CATACOMBS, 1, is_transient=True),
    60006301: Location(LOC_DIF.SHOP_HARD, AREA.CATACOMBS, 1, is_transient=True),
    60006305: Location(LOC_DIF.SHOP_EASY, AREA.CATACOMBS, 1, is_transient=True),
    60006306: Location(LOC_DIF.SHOP_EASY, AREA.CATACOMBS, 1, is_transient=True),
    60006307: Location(LOC_DIF.SHOP_EASY, AREA.CATACOMBS, 1, is_transient=True),
    60006308: Location(LOC_DIF.SHOP_EASY, AREA.CATACOMBS, 1, is_transient=True),
    60006309: Location(LOC_DIF.SHOP_EASY, AREA.CATACOMBS, 1, is_transient=True),
    60006310: Location(LOC_DIF.SHOP_EASY, AREA.CATACOMBS, 1, is_transient=True),
    60006410: Location(LOC_DIF.SHOP_EASY, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006411: Location(LOC_DIF.SHOP_EASY, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006412: Location(LOC_DIF.SHOP_MEDIUM, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006413: Location(LOC_DIF.SHOP_MEDIUM, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006414: Location(LOC_DIF.SHOP_MEDIUM, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006415: Location(LOC_DIF.SHOP_MEDIUM, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006416: Location(LOC_DIF.SHOP_MEDIUM, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006417: Location(LOC_DIF.SHOP_HARD, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006418: Location(LOC_DIF.SHOP_HARD, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006419: Location(LOC_DIF.SHOP_HARD, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006420: Location(LOC_DIF.HARD, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006421: Location(LOC_DIF.SHOP_EASY, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006422: Location(LOC_DIF.SHOP_EASY, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006423: Location(LOC_DIF.SHOP_EASY, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006424: Location(LOC_DIF.SHOP_EASY, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006425: Location(LOC_DIF.SHOP_EASY, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006426: Location(LOC_DIF.SHOP_EASY, AREA.ROYAL_WOOD, 1, is_transient=True),
    60006500: Location(
        LOC_DIF.SHOP_HARD, AREA.OOLACILE_SANCTUARY, 1, is_transient=True
    ),
    60006501: Location(
        LOC_DIF.LEAVE_ALONE,
        AREA.OOLACILE_SANCTUARY,
        1,
        has_flag=11217000,
        is_transient=True,
    ),
    60006507: Location(LOC_DIF.MEDIUM, AREA.OOLACILE_SANCTUARY, 1, is_transient=True),
    60006600: Location(LOC_DIF.SHOP_EASY, AREA.KALAMEET_FIGHT, 1, is_transient=True),
    60006601: Location(LOC_DIF.SHOP_MEDIUM, AREA.KALAMEET_FIGHT, 1, is_transient=True),
    60006602: Location(LOC_DIF.SHOP_MEDIUM, AREA.KALAMEET_FIGHT, 1, is_transient=True),
    60006603: Location(LOC_DIF.MEDIUM, AREA.KALAMEET_FIGHT, 1, is_transient=True),
    60006604: Location(LOC_DIF.HARD, AREA.KALAMEET_FIGHT, 1, is_transient=True),
    60006608: Location(LOC_DIF.SHOP_HARD, AREA.KALAMEET_FIGHT, 1, is_transient=True),
    60006609: Location(LOC_DIF.SHOP_HARD, AREA.KALAMEET_FIGHT, 1, is_transient=True),
    60006610: Location(LOC_DIF.SHOP_HARD, AREA.KALAMEET_FIGHT, 1, is_transient=True),
    60006611: Location(LOC_DIF.SHOP_EASY, AREA.KALAMEET_FIGHT, 1, is_transient=True),
    60010000: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010001: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010002: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010003: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010004: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010005: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010008: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010009: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010010: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010011: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010012: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010013: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010014: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010015: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010016: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010017: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010018: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010019: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010020: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010021: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010022: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010023: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010024: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010025: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010026: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010027: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010028: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010029: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010030: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010031: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010034: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010035: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010036: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010037: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010038: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010039: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010040: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010041: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010042: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010043: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010044: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010045: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010046: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010047: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010048: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010049: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010050: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010051: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010052: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010053: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010054: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010055: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010056: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010057: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010058: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010059: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010060: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010061: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010062: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010063: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010064: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010065: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010066: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010068: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010069: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010070: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010071: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010072: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010073: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010074: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010075: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
    60010076: Location(LOC_DIF.LEAVE_ALONE, AREA.NONE, 1, is_transient=True),
}

for loc_id in LOCATIONS:
    LOCATIONS[loc_id].location_id = loc_id

# Basic sanity check to prevent locations that share item lots from sharing indices.
# This problem should really be fixed a different way (namely, shared
#  item lots should be compressed, but this will do until later).
# Because of this, shared item lots can really only have the lower indexed
#  portion be of max_size 1 (as without compression, the item lot will be
#  split and thus not function properly).
collision_dict = {}
for loc_id in LOCATIONS:
    loc = LOCATIONS[loc_id]
    for i in [loc_id] + loc.linked_locations:
        for j in range(i, i + loc.max_size):
            if j not in collision_dict:
                collision_dict[j] = loc_id
            else:
                print(
                    "Location collision on index "
                    + str(j)
                    + " between "
                    + str(loc_id)
                    + " & "
                    + str(collision_dict[j])
                )

STARTING_ITEM_TABLE = {
    "warrior": {"right_hand": 1810100, "left_hand": 1810110},
    "knight": {"right_hand": 1810120, "left_hand": 1810130},
    "wanderer": {"right_hand": 1810140, "left_hand": 1810150},
    "thief": {"right_hand": 1810160, "left_hand": 1810170},
    "bandit": {"right_hand": 1810180, "left_hand": 1810190},
    "hunter": {"right_hand": 1810200, "left_hand": 1810210, "extra": 1810220},
    "sorcerer": {"right_hand": 1810230, "left_hand": 1810240, "extra": 1810250},
    "pyromancer": {"right_hand": 1810260, "left_hand": 1810270, "extra": 1810280},
    "cleric": {"right_hand": 1810290, "left_hand": 1810300, "extra": 1810310},
    "deprived": {"right_hand": 1810320, "left_hand": 1810330},
}
