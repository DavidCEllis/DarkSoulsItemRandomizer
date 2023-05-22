import logging

log = logging.getLogger(__name__)


class ITEM_TYPE:
    NONE = -1
    WEAPON = 0
    ARMOR = 1
    RING = 2
    ITEM = 4
    SHOP_SPELL = -4


class ITEM_DIF:
    IGNORE = -1  # Not used by the game.
    EASY = 0
    MEDIUM = 1
    HARD = 2
    KEY = 3
    SMALL_SOUL = 4
    BIG_SOUL = 5
    BOSS_SOUL = 6
    NPC_EASY = 7
    NPC_MEDIUM = 8
    NPC_HARD = 9
    SALABLE_EASY = 10
    SALABLE_MEDIUM = 11
    SALABLE_HARD = 12
    NOT_IN_POOL = (
        13  # Items that aren't appropriate to shuffle, or should be left alone.
    )


class ItemLotEntry:
    def __init__(self, item_type, item_id, count=1, luck=True, rate=100):
        self.item_type = item_type
        self.item_id = item_id
        self.count = count
        self.luck = luck
        self.rate = rate


class ItemLotPart:
    def __init__(
        self,
        difficulty,
        rarity,
        items,
        flag=-1,
        needs_flag=False,
        follow_items=[],
        always_follow_items=False,
        key_name=None,
        flag_can_tolerate_shop=True,
    ):
        if needs_flag and flag == -1:
            log.warn("Warning: ItemLotPart indicates it needs flag, but has none.")
        if len(items) > 8:
            log.warn("Warning: ItemLotPart exceeds maximum item limit (8)")
        if difficulty == ITEM_DIF.KEY and follow_items:
            log.warn(
                "Warning: Key ItemLotPart has follow items, which is not sensible."
            )

        self.diff = difficulty
        self.rarity = rarity
        self.items = items
        self.flag = flag
        self.needs_flag = needs_flag
        self.follow_items = follow_items
        self.always_follow_items = always_follow_items
        self.key_name = key_name
        self.flag_can_tolerate_shop = flag_can_tolerate_shop

    def get_max_effective_size(self):
        if self.needs_flag:
            return 1 + len(self.follow_items) + 1
        else:
            return 1 + len(self.follow_items)


ITEMS = {
    0: ItemLotPart(
        ITEM_DIF.IGNORE,
        9,
        [
            ItemLotEntry(ITEM_TYPE.WEAPON, 100000, luck=False),
            ItemLotEntry(ITEM_TYPE.ARMOR, 10000, count=2, rate=50, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 240, count=99, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 101000, rate=50, luck=False),
            ItemLotEntry(ITEM_TYPE.ARMOR, 11000, count=2, rate=40, luck=False),
        ],
    ),
    1: ItemLotPart(
        ITEM_DIF.IGNORE,
        0,
        [
            ItemLotEntry(ITEM_TYPE.ITEM, 240, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 240, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 2001, rate=300, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 240, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 240, luck=False),
        ],
    ),
    2: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=375),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, count=2, rate=20, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate=30, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1013, count=2, rate=20, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1013, rate=30, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1023, rate=50, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1001, count=3, rate=50, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1001, rate=50, luck=False),
        ],
    ),
    1000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 100)],
        flag=50000000,
        needs_flag=True,
    ),
    1010: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 111)], flag=50000010
    ),
    1020: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1475000)], flag=50000020
    ),
    1030: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 274)], flag=50000030
    ),
    1040: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1475000)], flag=50000040
    ),
    1050: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.RING, 108)], flag=50000070
    ),
    1060: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5320)], flag=50000060
    ),
    # 1070: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.RING, 108)], flag = 50000070),
    1080: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2012)],
        flag=50000080,
        needs_flag=True,
        flag_can_tolerate_shop=False,
    ),
    1081: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2011)]),
    1082: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 201, count=5)]
    ),
    1090: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2510)],
        flag=50000090,
        needs_flag=True,
        key_name="lordvessel",
    ),
    1100: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2013)],
        flag=50000100,
        needs_flag=True,
        key_name="key_to_the_seal",
    ),
    1110: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1330000)], flag=50000110
    ),
    1120: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 5500)],
        flag=50000120,
        needs_flag=True,
    ),
    1130: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 5510)],
        flag=50000130,
        needs_flag=True,
    ),
    1140: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 381)], flag=50000140
    ),
    1150: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 375)], flag=50000150
    ),
    1160: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.RING, 103)],
        flag=50000160,
        needs_flag=True,
    ),
    1170: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 240)],
        flag=50000170,
        needs_flag=True,
    ),
    1180: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.RING, 124)],
        flag=50000180,
        needs_flag=True,
    ),
    1190: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=50000190
    ),
    1200: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=50000200
    ),
    1210: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5040)], flag=50000210
    ),
    1220: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 453000)],
        flag=50000220,
        needs_flag=True,
        flag_can_tolerate_shop=False,
        follow_items=[1221],
    ),
    1221: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 5100)],
        flag=50000225,
        needs_flag=True,
        flag_can_tolerate_shop=False,
    ),
    1230: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 5110)],
        flag=50000230,
        needs_flag=True,
    ),
    1240: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)], flag=50000240
    ),
    1250: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1070)], flag=50000250
    ),
    1260: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 114)],
        flag=50000265,
        needs_flag=True,
        flag_can_tolerate_shop=False,
        follow_items=[1261],
        always_follow_items=True,
    ),
    1261: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 377)],
        flag=50000260,
        needs_flag=True,
        flag_can_tolerate_shop=False,
    ),
    1270: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 378)],
        flag=50000270,
        needs_flag=True,
    ),
    1280: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 275)]),
    1290: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1330000)], flag=50000290
    ),
    1300: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4040)], flag=50000300
    ),
    1310: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 4500)],
        flag=50000310,
        needs_flag=True,
    ),
    1320: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 4520)],
        flag=50000320,
        needs_flag=True,
    ),
    1330: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 4510)],
        flag=50000330,
        needs_flag=True,
    ),
    1340: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 408)], flag=50000340
    ),
    1350: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.RING, 130)],
        flag=50000350,
        needs_flag=True,
    ),
    1360: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 113)],
        flag=50000360,
        needs_flag=True,
        flag_can_tolerate_shop=False,
        follow_items=[1361],
        always_follow_items=True,
    ),
    1361: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.RING, 102)],
        flag=50000365,
        needs_flag=True,
        flag_can_tolerate_shop=False,
    ),
    1370: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 5910)],
        flag=50000370,
        flag_can_tolerate_shop=False,
        needs_flag=True,
    ),
    1371: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1366000)],
        flag=50000375,
        flag_can_tolerate_shop=False,
        needs_flag=True,
    ),
    1380: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 904000)],
        flag=50000380,
        needs_flag=True,
    ),
    1390: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 102)],
        flag=50000390,
        needs_flag=True,
    ),
    1400: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 210000)],
        flag=50000400,
        needs_flag=True,
    ),
    1401: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 40000)],
        flag=50000410,
        needs_flag=True,
    ),
    1402: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 41000)],
        flag=50000420,
        needs_flag=True,
    ),
    1403: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 42000)],
        flag=50000430,
        needs_flag=True,
    ),
    1404: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 43000)],
        flag=50000440,
        needs_flag=True,
    ),
    1410: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5520)]),
    1420: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 116)], flag=50000420
    ),
    1500: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 9011000)],
        flag=50000530,
        follow_items=[1501],
    ),  # FLAG MOD: 50000501 -> 50000530
    1501: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9010000)], flag=50000530
    ),
    1510: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9021000)], flag=50000540
    ),  # FLAG MOD: 50000511 -> 50000540
    1520: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 230, count=3)], flag=50000520
    ),
    2020: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2006)], flag=50001020
    ),
    2030: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 115)], flag=50001031
    ),
    2031: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 400000)],
        flag=50001050,
        follow_items=[2032, 2033, 2034],
    ),  # FLAG MOD: 50001030 -> 50001050
    2032: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 401000)], flag=50001050
    ),  # FLAG MOD!
    2033: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 402000)], flag=50001050
    ),  # FLAG MOD!
    2034: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 403000)], flag=50001050
    ),  # FLAG MOD!
    2060: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 390)], flag=50001060
    ),
    2070: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 376)], flag=50001070
    ),
    2200: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 118)],
        flag=50001200,
        needs_flag=True,
        key_name="purple_cowards_crystal",
    ),
    2500: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2007)],
        flag=50001500,
        needs_flag=True,
        key_name="blighttown_key",
    ),
    2510: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2014)],
        flag=50001510,
        needs_flag=True,
        key_name="key_to_depths",
    ),
    2520: ItemLotPart(
        ITEM_DIF.BOSS_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 707)], flag=50001520
    ),
    2530: ItemLotPart(
        ITEM_DIF.BOSS_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 705)], flag=50001530
    ),
    2540: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.RING, 138)],
        flag=50001540,
        needs_flag=True,
        key_name="covenant_of_artorias",
    ),
    2541: ItemLotPart(ITEM_DIF.BOSS_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 701)]),
    2550: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2607)],
        flag=50001550,
        needs_flag=True,
        key_name="rite_of_kindling",
    ),
    2560: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2500)],
        flag=50001560,
        needs_flag=True,
        key_name="lord_soul_nito",
    ),
    2570: ItemLotPart(
        ITEM_DIF.BOSS_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 700)], flag=50001570
    ),
    2580: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2501)],
        flag=50001580,
        needs_flag=True,
        key_name="lord_soul_bed_of_chaos",
    ),
    2590: ItemLotPart(
        ITEM_DIF.BOSS_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 703)], flag=50001590
    ),
    2600: ItemLotPart(
        ITEM_DIF.BOSS_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 708)], flag=50001600
    ),
    2611: ItemLotPart(
        ITEM_DIF.BOSS_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 704)], flag=50001610
    ),
    2621: ItemLotPart(
        ITEM_DIF.BOSS_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 706)], flag=50001620
    ),
    2630: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2502)],
        flag=50001630,
        needs_flag=True,
        key_name="lord_soul_shard_four_kings",
    ),
    2640: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2503)],
        flag=50001640,
        needs_flag=True,
        key_name="lord_soul_shard_seath",
    ),
    2650: ItemLotPart(
        ITEM_DIF.BOSS_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 702)], flag=50001650
    ),
    2660: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2011)]),
    2661: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 852000)]),
    2670: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.RING, 139)],
        flag=50001670,
        needs_flag=True,
        key_name="orange_charred_ring",
    ),
    2680: ItemLotPart(
        ITEM_DIF.BOSS_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 709)], flag=50001680
    ),
    2690: ItemLotPart(
        ITEM_DIF.BOSS_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 710)], flag=50001690
    ),
    2700: ItemLotPart(
        ITEM_DIF.BOSS_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 711)], flag=50001700
    ),
    2710: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 150)], flag=50001710
    ),
    2800: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 503000)], flag=50001800
    ),
    2810: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 503100)], flag=50001810
    ),
    2820: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 503200)], flag=50001820
    ),
    3000: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 274, count=2)]),
    3010: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1130)]),
    3020: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1130)]),
    3030: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1130, count=2)]
    ),
    3040: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1110)]),
    3050: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1120)]),
    3060: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.RING, 126)]),
    3070: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1120)]),
    3080: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1050)]),
    3090: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 374)]),
    3100: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1030)]),
    3110: ItemLotPart(ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1040)]),
    3120: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.RING, 127)]),
    3130: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1060)]),
    3140: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1100)]),
    3150: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 124)]),
    3160: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.RING, 137)]),
    3170: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 143)]),
    3180: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 852000)]),
    3190: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 240, count=2)]),
    3200: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3740)]),
    4000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2001)], flag=50004000
    ),
    4001: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2002)], flag=50004001
    ),
    4002: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2003)], flag=50004002
    ),
    4003: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2004)], flag=50004003
    ),
    4004: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2005)], flag=50004004
    ),
    4005: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2006)], flag=50004005
    ),
    4006: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2007)], flag=50004006
    ),
    4007: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2008)], flag=50004007
    ),
    4008: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2009)], flag=50004008
    ),
    4010: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2010)], flag=50004009
    ),
    4011: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2011)], flag=50004010
    ),
    4012: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2012)], flag=50004011
    ),
    4013: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2013)], flag=50004012
    ),
    4014: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2014)], flag=50004013
    ),
    4015: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2015)], flag=50004014
    ),
    4016: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2016)], flag=50004015
    ),
    4017: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2017)], flag=50004016
    ),
    4018: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2018)], flag=50004017
    ),
    4020: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2019)], flag=50004018
    ),
    4021: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2020)], flag=50004019
    ),
    4022: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2021)], flag=50004020
    ),
    4023: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2500)], flag=50004021
    ),
    4024: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2501)], flag=50004022
    ),
    4025: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2502)], flag=50004023
    ),
    4026: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2503)], flag=50004024
    ),
    4027: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2510)], flag=50004025
    ),
    4028: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.RING, 138)], flag=50004026
    ),
    4030: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.RING, 139)], flag=50004027
    ),
    4031: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 100)], flag=50004028
    ),
    4032: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 101)], flag=50004029
    ),
    4033: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 102)], flag=50004030
    ),
    4034: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 103)], flag=50004031
    ),
    4035: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 106)], flag=50004032
    ),
    4036: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 108)], flag=50004033
    ),
    4037: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 112)], flag=50004034
    ),
    4038: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 113)], flag=50004035
    ),
    4040: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 114)], flag=50004036
    ),
    4041: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 117)], flag=50004037
    ),
    4042: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 200)], flag=50004038
    ),
    4043: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 202)], flag=50004039
    ),
    4044: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 204)], flag=50004040
    ),
    4045: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 206)], flag=50004041
    ),
    4046: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 208)], flag=50004042
    ),
    4047: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 210)], flag=50004043
    ),
    4048: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 212)], flag=50004044
    ),
    4050: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 214)], flag=50004045
    ),
    4051: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 384)], flag=50004046
    ),
    4052: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2600)], flag=50004047
    ),
    4053: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2601)], flag=50004048
    ),
    4054: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2602)], flag=50004049
    ),
    4055: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2607)], flag=50004050
    ),
    4056: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2608)], flag=50004051
    ),
    4057: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.RING, 102)], flag=50004052
    ),
    4058: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.RING, 103)], flag=50004053
    ),
    4060: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 377)], flag=50004054
    ),
    4061: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 378)], flag=50004055
    ),
    4062: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 800)], flag=50004056
    ),
    4063: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 801)], flag=50004057
    ),
    4064: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 802)], flag=50004058
    ),
    4065: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 806)], flag=50004059
    ),
    4066: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 807)], flag=50004060
    ),
    4067: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 808)], flag=50004061
    ),
    4068: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 809)], flag=50004062
    ),
    4070: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 810)], flag=50004063
    ),
    4071: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 812)], flag=50004064
    ),
    4072: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 813)], flag=50004065
    ),
    4073: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2100)], flag=50004066
    ),
    4074: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2022)], flag=50004067
    ),
    4075: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2520)], flag=50004068
    ),
    4076: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 118)], flag=50004069
    ),
    # Add Dried Finger to recovery chest, which is needed for DS1R and will be ignored in PTDE
    4077: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 385)], flag=50004070
    ),
    5000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate=10),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate=25),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, rate=25),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, rate=10),
            ItemLotEntry(ITEM_TYPE.ITEM, 1040, rate=10),
            ItemLotEntry(ITEM_TYPE.ITEM, 1050, rate=10),
            ItemLotEntry(ITEM_TYPE.ITEM, 380, rate=5, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 376, rate=5, luck=False),
        ],
    ),
    5010: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 109)]),
    5020: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 374)]),
    5030: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 375)]),
    5040: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1110)]),
    5200: ItemLotPart(ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 2)]),
    5210: ItemLotPart(ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 3)]),
    5220: ItemLotPart(ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 6)]),
    5230: ItemLotPart(ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 10)]),
    5240: ItemLotPart(ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 20)]),
    5250: ItemLotPart(ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 30)]),
    5260: ItemLotPart(ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 40)]),
    5270: ItemLotPart(ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 50)]),
    5280: ItemLotPart(ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 100)]),
    6000: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 160000)],
        flag=50006000,
        follow_items=[6001, 6002, 6003, 6004, 6005, 6006, 6008],
    ),
    6001: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 161000)], flag=50006000
    ),
    6002: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 162000)], flag=50006000
    ),
    6003: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 163000)], flag=50006000
    ),
    6004: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 206000)], flag=50006020
    ),  # FLAG MOD: 50006001 -> 50006020
    6005: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1472000)], flag=50006020
    ),  # FLAG MOD!
    6006: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1365000)], flag=50006020
    ),  # FLAG MOD!
    # 6007: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 100)], flag = 50000000, needs_flag = True),
    6008: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=2)], flag=50006030
    ),  # FLAG MOD: 50006002 -> 50006030
    6010: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 391)], flag=50006010
    ),
    6020: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2012)],
        flag=50000080,
        needs_flag=True,
        flag_can_tolerate_shop=False,
    ),
    6021: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        0,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2011)],
        flag=50000081,
        needs_flag=True,
        flag_can_tolerate_shop=False,
    ),
    # 6022: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 201, count = 5)]),
    6040: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 3510)],
        flag=50006040,
        follow_items=[6041, 6042],
    ),
    6041: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 123)], flag=50006040
    ),
    6042: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=50006050
    ),  # FLAG MOD: 50006041 -> 50006050
    6070: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1363000)]),
    6071: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 376)]),
    6072: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=7)]),
    6080: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1363000)]),
    6081: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=2)]),
    6160: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 112)],
        flag=11407080,
        needs_flag=True,
    ),
    # 6170: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4040)], flag = 50000300),
    6180: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2013)], flag=50000100
    ),
    6181: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=50006180
    ),
    6190: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2002)],
        flag=11017140,
        needs_flag=True,
        key_name="crest_of_artorias",
    ),
    6191: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=3)], flag=50006190
    ),
    6230: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 106)],
        flag=11017020,
        needs_flag=True,
    ),
    6231: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2021)],
        flag=11017030,
        needs_flag=True,
        key_name="residence_key",
    ),
    6232: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=50006230
    ),
    # Add the Twin Humanities from DS1R as Undead Merchant's extra drop. Not strictly correct, but will work.
    6233: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)], flag=51100050
    ),
    # 6280: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.RING, 108)], flag = 50000070),
    6281: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=3)], flag=50006280
    ),
    6300: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.RING, 143)],
        flag=50006300,
        follow_items=[6301],
    ),
    6301: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=5)], flag=50006330
    ),  # FLAG MOD: 50006301 -> 50006330
    6310: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 451000)],
        flag=50006310,
        follow_items=[6311, 6312],
    ),
    6311: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1461000)], flag=50006310
    ),
    6312: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=2)], flag=50006340
    ),  # FLAG MOD: 50006311 -> 50006340
    6320: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 702000)],
        flag=50006320,
        follow_items=[6321],
    ),
    6321: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=4)], flag=50006321
    ),
    6370: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 108)],
        flag=11607020,
        needs_flag=True,
    ),
    6371: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501, count=2)], flag=50006371
    ),
    6420: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.RING, 128)],
        flag=50006420,
        follow_items=[6421],
    ),
    6421: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=50006430
    ),  # FLAG MOD: 50006421 -> 50006430
    6500: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 302000)], flag=50006500
    ),
    6530: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 703000)],
        flag=50006530,
        follow_items=[6531],
    ),
    6531: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=3)], flag=50006540
    ),  # FLAG MOD: 50006531 -> 50006540
    6550: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 851000)],
        flag=50006550,
        follow_items=[6551, 6552],
    ),
    6551: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9001000)], flag=50006550
    ),
    6552: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=2)], flag=50006590
    ),  # FLAG MOD: 50006551 -> 50006590
    6560: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 207000)], flag=50006560
    ),
    6561: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1470000)], flag=50006610
    ),  # FLAG MOD: 50006561 -> 50006610
    6570: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1601000)], flag=50006570
    ),
    6580: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 100)], flag=50006580
    ),
    6600: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 604000)], flag=50006600
    ),
    6620: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1308000)], flag=50006620
    ),
    6640: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)],
        flag=50006640,
    ),
    6650: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)],
        flag=50006650,
    ),
    6740: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 670000)],
        flag=50000500,
        follow_items=[6741, 6742, 6743],
    ),
    6741: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 671000)], flag=50000500
    ),
    6742: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 672000)], flag=50000500
    ),
    6743: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 673000)], flag=50000500
    ),
    # 6744: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9011000)], flag = 50000460, follow_items = [6745]), # FLAG MOD!
    # 6745: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9010000)], flag = 50000460),
    7020: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1456000)], flag=50007020
    ),
    7030: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 380000)],
        flag=50007030,
        follow_items=[7031, 7032],
    ),
    7031: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1306000)], flag=50007030
    ),
    7032: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3700)], flag=50007040
    ),  # FLAG MOD: 50007031 -> 50007040
    8000: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1202000)],
        flag=50008000,
        follow_items=[8001, 8002],
    ),
    8001: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 240000)], flag=50008000
    ),
    8002: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)], flag=50008010
    ),  # FLAG MOD: 50008001 -> 50008010
    9000: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    9010: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=4)]),
    9020: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    9030: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 330)]),
    9040: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=10)]),
    # Snipped several rows of un-used testing data that does not fit the
    #  standards of any other row. Rather than supporting this, it will
    #  not be included in the file, unless it is later deemed necessary.
    100000: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 370)]),
    100010: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 370, count=2)]
    ),
    100020: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 240)]),
    100100: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 296)]),
    100110: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 312)]),
    100120: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 274)]),
    100200: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 380)]),
    100210: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 310)]),
    100220: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 311)]),
    100300: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 380)]),
    100310: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 293)]),
    100320: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 275)]),
    100400: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 380)]),
    100410: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 271)]),
    100420: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 272)]),
    100500: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 400)]),
    100510: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 401)]),
    100520: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 403)]),
    100600: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 401)]),
    100610: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 402)]),
    100620: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 405)]),
    100700: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1000)]),
    100710: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1010)]),
    100720: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1030)]),
    100800: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1000)]),
    100810: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1020)]),
    100820: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1040)]),
    100900: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1000)]),
    100910: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1020)]),
    100920: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1050)]),
    101000: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1000)]),
    101010: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1020)]),
    101020: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1060)]),
    101100: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 380)]),
    101110: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 280)]),
    101120: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1110)]),
    101200: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 380)]),
    101210: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 280)]),
    101220: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1120)]),
    101300: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 380)]),
    101310: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 280)]),
    101320: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1130)]),
    101400: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 370)]),
    101410: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 370, count=2)]
    ),
    101420: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [
            ItemLotEntry(ITEM_TYPE.ITEM, 381, rate=60),
            ItemLotEntry(ITEM_TYPE.ITEM, 382, rate=30),
            ItemLotEntry(ITEM_TYPE.ITEM, 383, rate=10, luck=False),
        ],
    ),
    1000000: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51000000
    ),
    1000010: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 402)], flag=51000010
    ),
    1000020: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 750000)], flag=51000020
    ),
    1000030: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 402)], flag=51000030
    ),
    1000040: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51000040
    ),
    1000050: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51000050
    ),
    1000090: ItemLotPart(
        ITEM_DIF.EASY, 0, [ItemLotEntry(ITEM_TYPE.WEAPON, 1462000)], flag=51000090
    ),
    1000100: ItemLotPart(
        ITEM_DIF.MEDIUM, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 1010)], flag=51000100
    ),
    1000120: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 402)], flag=51000120
    ),
    1000140: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 402)], flag=51000140
    ),
    1000170: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 142)], flag=51000170
    ),
    1000180: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 402)], flag=51000180
    ),
    1000190: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1251000)],
        flag=51000190,
        follow_items=[1000191],
    ),
    1000191: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 2101000, count=11)],
        flag=51000190,
    ),
    1000210: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 210000)],
        flag=51000210,
        follow_items=[1000211, 1000212, 1000213],
    ),
    1000211: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 211000)], flag=51000210
    ),
    1000212: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 212000)], flag=51000210
    ),
    1000213: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 213000)], flag=51000210
    ),
    1000240: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2018)],
        flag=51000240,
        needs_flag=True,
        key_name="sewer_chamber_key",
    ),
    1000500: ItemLotPart(
        ITEM_DIF.KEY,
        3,
        [ItemLotEntry(ITEM_TYPE.ITEM, 800)],
        flag=51000500,
        needs_flag=True,
        key_name="large_ember",
    ),
    1010000: ItemLotPart(
        ITEM_DIF.KEY,
        0,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2017)],
        flag=51010000,
        needs_flag=True,
        key_name="mystery_key",
    ),
    1010020: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 600000)], flag=51010020
    ),
    1010040: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51010040
    ),
    1010050: ItemLotPart(ITEM_DIF.HARD, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 396)]),
    1010070: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 401)], flag=51010070
    ),
    1010080: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 380)], flag=51010080
    ),
    1010090: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1250000)],
        flag=51010090,
        follow_items=[1010091],
    ),
    1010091: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 2100000, count=16)],
        flag=51010090,
    ),
    1010100: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51010100
    ),
    1010120: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 290, count=10)], flag=51010120
    ),
    1010130: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1401000)], flag=51010130
    ),
    1010140: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2001)],
        flag=51010140,
        needs_flag=True,
        key_name="basement_key",
    ),
    1010160: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.RING, 147)], flag=51010160
    ),
    1010210: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 301000)], flag=51010210
    ),
    1010220: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 402)], flag=51010220
    ),
    1010260: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 294, count=4)], flag=51010260
    ),
    1010280: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 401)], flag=51010280
    ),
    1010300: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1451000)], flag=51010300
    ),
    1010370: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 401)], flag=51010370
    ),
    1010380: ItemLotPart(
        ITEM_DIF.MEDIUM,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 300000)],
        flag=51010380,
        follow_items=[1010381, 1010382, 1010383, 1010384],
    ),
    1010381: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 301000)], flag=51010380
    ),
    1010382: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 302000)], flag=51010380
    ),
    1010383: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 303000)], flag=51010380
    ),
    1010384: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1404000)], flag=51010530
    ),  # FLAG MOD: 51010381 -> 51010530
    1010390: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51010390
    ),
    1010400: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51010400
    ),
    1010410: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51010410
    ),
    1010420: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51010420
    ),
    1010430: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 401)], flag=51010430
    ),
    1010440: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51010440
    ),
    1010450: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 297, count=5)], flag=51010450
    ),
    1010460: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 311, count=3)], flag=51010460
    ),
    1010470: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51010470
    ),
    1010480: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 401)], flag=51010480
    ),
    1010490: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)], flag=51010490
    ),
    1010500: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51010500
    ),
    1010510: ItemLotPart(
        ITEM_DIF.MEDIUM,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 220000)],
        flag=51010510,
        follow_items=[1010511, 1010512, 1010513, 1010514],
    ),
    1010511: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 221000)], flag=51010510
    ),
    1010512: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 222000)], flag=51010510
    ),
    1010513: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 223000)], flag=51010510
    ),
    1010514: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1300000)], flag=51010540
    ),  # FLAG MOD: 51010511 -> 51010540
    1010520: ItemLotPart(
        ITEM_DIF.HARD, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1100000)], flag=51010520
    ),
    1020000: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=3)], flag=51020000
    ),
    1020010: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 401)], flag=51020010
    ),
    1020020: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1410000)], flag=51020020
    ),
    1020030: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 401)], flag=51020030
    ),
    1020040: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51020040
    ),
    1020050: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51020050
    ),
    1020060: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51020060
    ),
    1020070: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 296, count=4)], flag=51020070
    ),
    1020090: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51020090
    ),
    1020110: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 292, count=6)], flag=51020110
    ),
    1020120: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51020120
    ),
    1020130: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.RING, 126)], flag=51020130
    ),
    1020140: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51020140
    ),
    1020150: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 350000)], flag=51020150
    ),
    1020160: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1001000)], flag=51020160
    ),
    1020170: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 371)], flag=51020170
    ),
    1020180: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 802000)],
        flag=51020180,
        follow_items=[1020181],
    ),
    1020181: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1360000)], flag=51020180
    ),
    1020190: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 330, count=6)], flag=51020190
    ),
    1020200: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 111, count=4)], flag=51020200
    ),
    1020210: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2016)],
        flag=51020210,
        needs_flag=True,
        key_name="undead_asylum_f2_west_key",
    ),
    1100010: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51100010
    ),
    # Attach Dried Finger's flag to it for DS1R, and will be okay but unused in PTDE.
    1100020: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.ITEM, 385)],
        flag=11017210,
        needs_flag=True,
    ),
    1100030: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51100030
    ),
    1100040: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51100040
    ),
    1100060: ItemLotPart(
        ITEM_DIF.MEDIUM,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 150000)],
        flag=51100060,
        follow_items=[1100061, 1100062, 1100063],
    ),
    1100061: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 151000)], flag=51100060
    ),
    1100062: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 152000)], flag=51100060
    ),
    1100063: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 153000)], flag=51100060
    ),
    1100070: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51100070
    ),
    1100090: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5810)], flag=51100090
    ),
    1100100: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 383)], flag=51100100
    ),
    1100120: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51100120
    ),
    1100130: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51100130
    ),
    1100140: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2009)],
        flag=51100140,
        needs_flag=True,
        key_name="annex_key",
    ),
    1100150: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 290000)],
        flag=51100150,
        follow_items=[1100151, 1100152, 1100153],
    ),
    1100151: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 291000)], flag=51100150
    ),
    1100152: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 292000)], flag=51100150
    ),
    1100153: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 293000)], flag=51100150
    ),
    1100160: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.RING, 126)], flag=51100160
    ),
    1100170: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51100170
    ),
    1100190: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4220)], flag=51100190
    ),
    1100200: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9002000)], flag=51100200
    ),
    1100210: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51100210
    ),
    1100230: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51100230
    ),
    1100240: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51100240
    ),
    1100250: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 275)], flag=51100250
    ),
    1100260: ItemLotPart(ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 404)]),
    1100280: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51100280
    ),
    1100290: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51100290
    ),
    1100300: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51100300
    ),
    1100310: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51100310
    ),
    1100320: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 603000)], flag=51100320
    ),
    1100330: ItemLotPart(
        ITEM_DIF.EASY,
        3,
        [ItemLotEntry(ITEM_TYPE.ITEM, 101)],
        flag=51100330,
        needs_flag=True,
    ),
    1100340: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51100340
    ),
    1100350: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51100350
    ),
    1100370: ItemLotPart(
        ITEM_DIF.KEY,
        3,
        [ItemLotEntry(ITEM_TYPE.ITEM, 810)],
        flag=51100370,
        needs_flag=True,
        key_name="dark_ember",
    ),
    1100500: ItemLotPart(
        ITEM_DIF.HARD,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 250000)],
        flag=51100500,
        follow_items=[1100501, 1100502, 1100503],
    ),
    1100501: ItemLotPart(
        ITEM_DIF.HARD, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 251000)], flag=51100500
    ),
    1100502: ItemLotPart(
        ITEM_DIF.HARD, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 252000)], flag=51100500
    ),
    1100503: ItemLotPart(
        ITEM_DIF.HARD, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 253000)], flag=51100500
    ),
    1200010: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1002000)], flag=51200010
    ),
    1200020: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 241000)],
        flag=51200020,
        follow_items=[1200021, 1200022, 1200023, 1200024],
    ),
    1200021: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 242000)], flag=51200020
    ),
    1200022: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 243000)], flag=51200020
    ),
    1200023: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1201000)], flag=51200021
    ),  # FLAG MOD: 51200021 -> 51200050
    1200024: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 2002000, count=16)],
        flag=51200021,
    ),  # FLAG MOD!
    1200030: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51200030
    ),
    1200040: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51200040
    ),
    1200060: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 146)], flag=51200060
    ),
    1200070: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 350000)],
        flag=51200070,
        follow_items=[1200071, 1200072, 1200073],
    ),
    1200071: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 351000)], flag=51200070
    ),
    1200072: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 352000)], flag=51200070
    ),
    1200073: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 353000)], flag=51200070
    ),
    1200080: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 280000)],
        flag=51200080,
        follow_items=[1200081, 1200082, 1200083],
    ),
    1200081: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 281000)], flag=51200080
    ),
    1200082: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 282000)], flag=51200080
    ),
    1200083: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 283000)], flag=51200080
    ),
    1200120: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51200120
    ),
    1200140: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2019)],
        flag=51200140,
        needs_flag=True,
        flag_can_tolerate_shop=False,
        key_name="watchtower_basement_key",
    ),
    1200141: ItemLotPart(
        ITEM_DIF.KEY,
        3,
        [ItemLotEntry(ITEM_TYPE.ITEM, 808)],
        flag=51200141,
        needs_flag=True,
        flag_can_tolerate_shop=False,
        key_name="divine_ember",
    ),
    1200142: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 330)], flag=51200220
    ),  # FLAG MOD: 51200142 -> 51200220
    1200150: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 330000)],
        flag=51200150,
        follow_items=[1200151, 1200152, 1200153],
    ),
    1200151: ItemLotPart(
        ITEM_DIF.HARD, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 331000)], flag=51200150
    ),
    1200152: ItemLotPart(
        ITEM_DIF.HARD, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 332000)], flag=51200150
    ),
    1200153: ItemLotPart(
        ITEM_DIF.HARD, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 333000)], flag=51200150
    ),
    1200160: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 117)], flag=51200160
    ),
    1200170: ItemLotPart(ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 403)]),
    1200500: ItemLotPart(
        ITEM_DIF.KEY,
        3,
        [ItemLotEntry(ITEM_TYPE.ITEM, 807)],
        flag=51200500,
        needs_flag=True,
        key_name="enchanted_ember",
    ),
    1200510: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 120000)],
        flag=51200510,
        follow_items=[1200511, 1200512, 1200513],
    ),
    1200511: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 121000)], flag=51200510
    ),
    1200512: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 122000)], flag=51200510
    ),
    1200513: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 123000)], flag=51200510
    ),
    1200180: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51200180
    ),
    1200190: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51200190
    ),
    1200200: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1453000)], flag=51200200
    ),
    1200210: ItemLotPart(
        ITEM_DIF.MEDIUM,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 390000)],
        flag=51200210,
        follow_items=[1200211, 1200212, 1200213],
    ),
    1200211: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 391000)], flag=51200210
    ),
    1200212: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 392000)], flag=51200210
    ),
    1200213: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 393000)], flag=51200210
    ),
    1210000: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210000
    ),
    1210010: ItemLotPart(
        ITEM_DIF.EASY, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51210010
    ),
    1210020: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51210020
    ),
    1210030: ItemLotPart(ITEM_DIF.MEDIUM, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 383)]),
    1210040: ItemLotPart(
        ITEM_DIF.EASY, 0, [ItemLotEntry(ITEM_TYPE.ARMOR, 693000)], flag=51210040
    ),
    1210050: ItemLotPart(
        ITEM_DIF.EASY, 0, [ItemLotEntry(ITEM_TYPE.ARMOR, 691000)], flag=51210050
    ),
    1210060: ItemLotPart(
        ITEM_DIF.MEDIUM, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 230)], flag=51210060
    ),
    1210070: ItemLotPart(
        ITEM_DIF.EASY, 0, [ItemLotEntry(ITEM_TYPE.ARMOR, 690000)], flag=51210070
    ),
    1210080: ItemLotPart(
        ITEM_DIF.EASY,
        0,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 2008000, count=8)],
        flag=51210080,
    ),
    1210090: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51210090
    ),
    1210100: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210100
    ),
    1210110: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51210110
    ),
    1210120: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210120
    ),
    1210130: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210130
    ),
    1210140: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210140
    ),
    1210150: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210150
    ),
    1210160: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51210160
    ),
    1210170: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210170
    ),
    1210180: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210180
    ),
    1210190: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 408)], flag=51210190
    ),
    1210200: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210200
    ),
    1210210: ItemLotPart(
        ITEM_DIF.EASY, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 380)], flag=51210210
    ),
    1210220: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 408)], flag=51210220
    ),
    1210230: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51210230
    ),
    1210240: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51210240
    ),
    1210250: ItemLotPart(
        ITEM_DIF.EASY,
        0,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 2008000, count=3)],
        flag=51210250,
    ),
    1210260: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51210260
    ),
    1210270: ItemLotPart(
        ITEM_DIF.HARD, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 3720)], flag=51210270
    ),
    1210280: ItemLotPart(
        ITEM_DIF.HARD, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 4530)], flag=51210280
    ),
    1210290: ItemLotPart(
        ITEM_DIF.HARD, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 1090)], flag=51210290
    ),
    1210300: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 408)], flag=51210300
    ),
    1210310: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210310
    ),
    1210320: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210320
    ),
    1210330: ItemLotPart(
        ITEM_DIF.EASY, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51210330
    ),
    1210340: ItemLotPart(
        ITEM_DIF.HARD,
        0,
        [ItemLotEntry(ITEM_TYPE.ITEM, 514)],
        flag=51210340,
        needs_flag=True,
    ),
    1210350: ItemLotPart(
        ITEM_DIF.EASY, 0, [ItemLotEntry(ITEM_TYPE.ARMOR, 692000)], flag=51210350
    ),
    1210360: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210360
    ),
    1210370: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210370
    ),
    1210380: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400, count=3)], flag=51210380
    ),
    1210390: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51210390
    ),
    1210400: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51210400
    ),
    1210410: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210410
    ),
    1210420: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210420
    ),
    1210430: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51210430
    ),
    1210440: ItemLotPart(
        ITEM_DIF.EASY, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 501)], flag=51210440
    ),
    1210450: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 408)], flag=51210450
    ),
    1210460: ItemLotPart(
        ITEM_DIF.EASY, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 501)], flag=51210460
    ),
    1210470: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51210470
    ),
    1210500: ItemLotPart(
        ITEM_DIF.HARD, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 1080)], flag=51210500
    ),
    1210510: ItemLotPart(
        ITEM_DIF.MEDIUM, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 1060)], flag=51210510
    ),
    1210520: ItemLotPart(
        ITEM_DIF.HARD, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 220)], flag=51210520
    ),
    1210530: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51210530
    ),
    1210540: ItemLotPart(
        ITEM_DIF.HARD, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 3710)], flag=51210540
    ),
    1210550: ItemLotPart(
        ITEM_DIF.HARD, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 1070)], flag=51210550
    ),
    1210560: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 2022)], flag=51210560
    ),
    1211000: ItemLotPart(
        ITEM_DIF.MEDIUM, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 3730)], flag=51211000
    ),
    1300000: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51300000
    ),
    1300010: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51300010
    ),
    1300020: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.RING, 149)],
        flag=51300020,
        key_name="darkmoon_seance_ring",
    ),
    1300030: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 109, count=3)], flag=51300030
    ),
    1300070: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1106000)], flag=51300070
    ),
    1300100: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1020)], flag=51300100
    ),
    1300110: ItemLotPart(
        ITEM_DIF.HARD, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1150000)], flag=51300110
    ),
    1300140: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51300140
    ),
    1300150: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51300150
    ),
    1300190: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 310000)],
        flag=51300190,
        follow_items=[1300191, 1300192, 1300193, 1300194],
    ),
    1300191: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 311000)], flag=51300190
    ),
    1300192: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 312000)], flag=51300190
    ),
    1300193: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 313000)], flag=51300190
    ),
    1300194: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 801000)], flag=51300200
    ),  # FLAG MOD: 51300191 -> 51300200
    1300210: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51300210
    ),
    1300220: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51300220
    ),
    1300230: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5800)], flag=51300230
    ),
    1300240: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51300240
    ),
    1300250: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51300250
    ),
    1310000: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51310000
    ),
    1310010: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51310010
    ),
    1310020: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51310020
    ),
    1310030: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51310030
    ),
    1310040: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51310040
    ),
    1310050: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51310050
    ),
    1310070: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51310070
    ),
    1310080: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 109, count=3)], flag=51310080
    ),
    1310090: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1396000)], flag=51310090
    ),
    1310100: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1050)]),
    1310110: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51310110
    ),
    1310120: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9000000)], flag=51310120
    ),
    1310140: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 122)], flag=51310140
    ),
    1310160: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1050)], flag=51310160
    ),
    1310180: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51310180
    ),
    1310200: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 408)], flag=51310200
    ),
    1310220: ItemLotPart(
        ITEM_DIF.HARD, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1090)], flag=51310220
    ),
    1310230: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 408)], flag=51310230
    ),
    1310240: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 20000)],
        flag=51310240,
        follow_items=[1310241, 1310242, 1310243],
    ),
    1310241: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 21000)], flag=51310240
    ),
    1310242: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 22000)], flag=51310240
    ),
    1310243: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 23000)], flag=51310240
    ),
    1310290: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1050)], flag=51310290
    ),
    1310300: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51310300
    ),
    1310500: ItemLotPart(
        ITEM_DIF.KEY,
        3,
        [ItemLotEntry(ITEM_TYPE.ITEM, 809)],
        flag=51310500,
        needs_flag=True,
        key_name="large_divine_ember",
    ),
    1320000: ItemLotPart(
        ITEM_DIF.EASY, 0, [ItemLotEntry(ITEM_TYPE.WEAPON, 1409000)], flag=51320000
    ),
    1320020: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 104)], flag=51320020
    ),
    1320040: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1030)], flag=51320040
    ),
    1320050: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51320050
    ),
    1320060: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1040)], flag=51320060
    ),
    1320070: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1050)], flag=51320070
    ),
    1320080: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1060)], flag=51320080
    ),
    1320090: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1040)], flag=51320090
    ),
    1320100: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1050)], flag=51320100
    ),
    1320110: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51320110
    ),
    1320120: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1030)], flag=51320120
    ),
    1320140: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1110)], flag=51320140
    ),
    1320150: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1110)], flag=51320150
    ),
    1320160: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1110)], flag=51320160
    ),
    1320170: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5610)], flag=51320170
    ),
    1320180: ItemLotPart(
        ITEM_DIF.EASY, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 501)], flag=51320180
    ),
    1320190: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1060)], flag=51320190
    ),
    1400020: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51400020
    ),
    1400040: ItemLotPart(
        ITEM_DIF.MEDIUM,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 60000)],
        flag=51400040,
        follow_items=[1400041, 1400042, 1400043],
    ),
    1400041: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 61000)], flag=51400040
    ),
    1400042: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 62000)], flag=51400040
    ),
    1400043: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 63000)], flag=51400040
    ),
    1400050: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51400050
    ),
    1400060: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51400060
    ),
    1400080: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 272, count=3)], flag=51400080
    ),
    1400090: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51400090
    ),
    1400100: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51400100
    ),
    1400130: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4400)], flag=51400130
    ),
    1400140: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51400140
    ),
    1400150: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51400150
    ),
    1400160: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1500000)], flag=51400160
    ),
    1400180: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1600000)], flag=51400180
    ),
    1400190: ItemLotPart(
        ITEM_DIF.HARD,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 140000)],
        flag=51400190,
        follow_items=[1400191, 1400192, 1400193, 1400194],
    ),
    1400191: ItemLotPart(
        ITEM_DIF.HARD, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 141000)], flag=51400190
    ),
    1400192: ItemLotPart(
        ITEM_DIF.HARD, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 142000)], flag=51400190
    ),
    1400193: ItemLotPart(
        ITEM_DIF.HARD, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 143000)], flag=51400190
    ),
    1400194: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1302000)], flag=51400200
    ),  # FLAG MOD: 51400191 -> 51400200
    1400210: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51400210
    ),
    1400230: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1010)], flag=51400230
    ),
    1400250: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 850000)], flag=51400250
    ),
    1400260: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51400260
    ),
    1400270: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 230000)],
        flag=51400270,
        follow_items=[1400271, 1400272, 1400273, 1400274],
    ),
    1400271: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 231000)], flag=51400270
    ),
    1400272: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 232000)], flag=51400270
    ),
    1400273: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 233000)], flag=51400270
    ),
    1400274: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4200)], flag=51000271
    ),
    1400280: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51400280
    ),
    1400290: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1020)], flag=51400290
    ),
    1400300: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1010)], flag=51400300
    ),
    1400310: ItemLotPart(
        ITEM_DIF.MEDIUM,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 360000)],
        flag=51400310,
        follow_items=[1400311, 1400312, 1400313, 1400314],
    ),
    1400311: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 361000)], flag=51400310
    ),
    1400312: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 362000)], flag=51400310
    ),
    1400313: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 363000)], flag=51400310
    ),
    1400314: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 401000)], flag=51400330
    ),  # FLAG MOD: 51400311 -> 51400330
    1400320: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51400320
    ),
    1400340: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 502000)], flag=51400340
    ),
    1400350: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 394)]),
    1400360: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 450000)], flag=51400360
    ),
    1400370: ItemLotPart(
        ITEM_DIF.MEDIUM,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 200000)],
        flag=51400370,
        follow_items=[1400371, 1400372, 1400373],
    ),
    1400371: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 201000)], flag=51400370
    ),
    1400372: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 202000)], flag=51400370
    ),
    1400373: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 203000)], flag=51400370
    ),
    1400500: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2008)],
        flag=51400500,
        needs_flag=True,
        key_name="key_to_new_londo_ruins",
    ),
    1400510: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1110)], flag=51400510
    ),
    1400520: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3610)], flag=51400520
    ),
    1410000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1060)], flag=51410000
    ),
    1410010: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1060)], flag=51410010
    ),
    1410020: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51410020
    ),
    1410030: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2)], flag=51410030
    ),
    1410050: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51410050
    ),
    1410060: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51410060
    ),
    1410080: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51410080
    ),
    1410090: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2)], flag=51410090
    ),
    1410100: ItemLotPart(
        ITEM_DIF.KEY,
        3,
        [ItemLotEntry(ITEM_TYPE.ITEM, 812)],
        flag=51410100,
        needs_flag=True,
        key_name="large_flame_ember",
    ),
    1410140: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51410140
    ),
    1410160: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51410160
    ),
    1410180: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 460000)],
        follow_items=[1410181, 1410182, 1410183],
    ),
    1410181: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 461000)]),
    1410182: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 462000)]),
    1410183: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 463000)]),
    1410190: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51410190
    ),
    1410200: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51410200
    ),
    1410210: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51410210
    ),
    1410220: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51410220
    ),
    1410230: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51410230
    ),
    1410240: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51410240
    ),
    1410250: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51410250
    ),
    1410260: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51410260
    ),
    1410270: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2)], flag=51410270
    ),
    1410280: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51410280
    ),
    1410290: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51410290
    ),
    1410300: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51410300
    ),
    1410310: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51410310
    ),
    1410320: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51410320
    ),
    1410330: ItemLotPart(
        ITEM_DIF.MEDIUM, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 240)], flag=51410330
    ),
    1410340: ItemLotPart(
        ITEM_DIF.MEDIUM, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 240)], flag=51410340
    ),
    1410350: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51410350
    ),
    1410360: ItemLotPart(
        ITEM_DIF.EASY, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 501)], flag=51410360
    ),
    1410370: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51410370
    ),
    1410380: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.RING, 127)], flag=51410380
    ),
    1410390: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51410390
    ),
    1410400: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 408)], flag=51410400
    ),
    1410410: ItemLotPart(
        ITEM_DIF.HARD, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1100)], flag=51410410
    ),
    1410500: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 409)], flag=51410500
    ),
    1410510: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51410510
    ),
    1410520: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4520)], flag=51410520
    ),
    1410530: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 813)],
        flag=51410530,
        needs_flag=True,
        key_name="chaos_flame_ember",
    ),
    1500000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 120)], flag=51500000
    ),
    1500010: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51500010
    ),
    1500020: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1010, count=2)], flag=51500020
    ),
    1500030: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51500030
    ),
    1500040: ItemLotPart(
        ITEM_DIF.MEDIUM, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 240)], flag=51500040
    ),
    1500050: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51500050
    ),
    1500060: ItemLotPart(
        ITEM_DIF.MEDIUM,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 640000)],
        flag=51500060,
        follow_items=[1500061, 1500062, 1500063, 1500064],
    ),
    1500061: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 641000)], flag=51500060
    ),
    1500062: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 642000)], flag=51500060
    ),
    1500063: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 643000)], flag=51500060
    ),
    1500064: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3510)], flag=51500110
    ),  # FLAG MOD: 51500061 -> 51500110
    1500070: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 121)], flag=51500070
    ),
    1500080: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1010, count=2)], flag=51500080
    ),
    1500090: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 105)], flag=51500090
    ),
    1500100: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.RING, 127)], flag=51500100
    ),
    1500150: ItemLotPart(
        ITEM_DIF.KEY,
        3,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2003)],
        flag=51500150,
        needs_flag=True,
        key_name="cage_key",
    ),
    1500300: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 402000)], flag=51500300
    ),
    1500310: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51500310
    ),
    1500320: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 123)], flag=51500320
    ),
    1500330: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51500330
    ),
    1500350: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51500350
    ),
    1500360: ItemLotPart(
        ITEM_DIF.HARD, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1107000)], flag=51500360
    ),
    1500400: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51500400
    ),
    1500410: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1010, count=2)], flag=51500410
    ),
    1500420: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 408)], flag=51500420
    ),
    1500430: ItemLotPart(
        ITEM_DIF.IGNORE, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51500430
    ),
    1500440: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1253000)],
        flag=51500440,
        follow_items=[1500441],
    ),
    1500441: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 2102000, count=12)],
        flag=51500440,
    ),
    1510000: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3110)], flag=51510000
    ),
    1510030: ItemLotPart(
        ITEM_DIF.MEDIUM, 3, [ItemLotEntry(ITEM_TYPE.RING, 148)], flag=51510030
    ),
    1510040: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1030)], flag=51510040
    ),
    1510050: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 408)], flag=51510050
    ),
    1510060: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1203000)],
        flag=51510060,
        follow_items=[1510061],
    ),
    1510061: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2007000)], flag=51510060
    ),
    1510070: ItemLotPart(
        ITEM_DIF.MEDIUM,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 70000)],
        flag=51510070,
        follow_items=[1510071, 1510072, 1510073, 1510074, 1510075],
    ),
    1510071: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 71000)], flag=51510070
    ),
    1510072: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 72000)], flag=51510070
    ),
    1510073: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 73000)], flag=51510070
    ),
    1510074: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 351000)], flag=51510090
    ),  # FLAG MOD: 51510071 -> 51510090
    1510075: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 9003000)], flag=51510090
    ),  # FLAG MOD!
    1510080: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 100000)],
        flag=51510080,
        follow_items=[1510081, 1510082, 1510083],
    ),
    1510081: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 101000)], flag=51510080
    ),
    1510082: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 102000)], flag=51510080
    ),
    1510083: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 103000)], flag=51510080
    ),
    1510510: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1120)], flag=51510510
    ),
    1510520: ItemLotPart(
        ITEM_DIF.MEDIUM, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 240)], flag=51510520
    ),
    1510530: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 440000)],
        flag=51510530,
        follow_items=[1510531],
    ),
    1510531: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 441000)], flag=51510530
    ),
    1510540: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 442000)],
        flag=51510540,
        follow_items=[1510541],
    ),
    1510541: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 443000)], flag=51510540
    ),
    1510560: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1505000)], flag=51510570
    ),
    1510570: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 854000)], flag=51510560
    ),
    1510580: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 420000)],
        flag=51510580,
        follow_items=[1510581],
    ),
    1510581: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 421000)], flag=51510580
    ),
    1510590: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 422000)],
        flag=51510590,
        follow_items=[1510591],
    ),
    1510591: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 423000)], flag=51510590
    ),
    1510600: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1120, count=2)], flag=51510600
    ),
    1510610: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 119)], flag=51510610
    ),
    1510620: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5900)], flag=51510620
    ),
    # Mark the shuffled None item as requiring its flag, so that it cannot be used as a flag-bearing
    #  item for location purposes. This is needed since items of count = 0 do not
    #  trigger their GetItemFlag upon pick-up.
    1510650: ItemLotPart(
        ITEM_DIF.HARD,
        0,
        [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)],
        flag=51510650,
        needs_flag=True,
    ),
    1510660: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 450000)],
        flag=51510660,
        follow_items=[1510661, 1510662, 1510663],
    ),
    1510661: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 451000)], flag=51510660
    ),
    1510662: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 452000)], flag=51510660
    ),
    1510663: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 453000)], flag=51510660
    ),
    1510670: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1130)], flag=51510670
    ),
    1510680: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1120)], flag=51510680
    ),
    1510690: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 375, count=3)], flag=51510690
    ),
    1510700: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 408)], flag=51510700
    ),
    1600000: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 402)], flag=51600000
    ),
    1600020: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 602000)], flag=51600020
    ),
    1600030: ItemLotPart(
        ITEM_DIF.HARD, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 393)], flag=51600030
    ),
    1600040: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 312, count=2)], flag=51600040
    ),
    1600060: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 101000)], flag=51600060
    ),
    1600070: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 312, count=2)], flag=51600070
    ),
    1600090: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51600090
    ),
    1600100: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1020)], flag=51600100
    ),
    1600110: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51600110
    ),
    1600120: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51600120
    ),
    1600130: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.RING, 127)], flag=51600130
    ),
    1600140: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 113)], flag=51600140
    ),
    1600150: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51600150
    ),
    1600160: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1204000)],
        flag=51600160,
        follow_items=[1600161],
    ),
    1600161: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 2001000, count=16)],
        flag=51600160,
    ),
    1600170: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 403)], flag=51600170
    ),
    1600180: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 209000)], flag=51600180
    ),
    1600190: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=51600190
    ),
    1600200: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1457000)], flag=51600200
    ),
    1600210: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51600210
    ),
    1600220: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 50000)],
        flag=51600220,
        follow_items=[1600221, 1600222, 1600223, 1600224],
    ),
    1600221: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 51000)], flag=51600220
    ),
    1600222: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 52000)], flag=51600220
    ),
    1600223: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 53000)], flag=51600220
    ),
    1600224: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1462000)], flag=51600230
    ),  # FLAG MOD: 51600221 -> 51600230
    1600250: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51600250
    ),
    1600260: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51600260
    ),
    1600270: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51600270
    ),
    1600280: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51600280
    ),
    1600290: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1030)], flag=51600290
    ),
    1600310: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 111, count=6)], flag=51600310
    ),
    1600330: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51600330
    ),
    1600360: ItemLotPart(
        ITEM_DIF.EASY,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 340000)],
        flag=51600360,
        follow_items=[1600361, 1600362, 1600363, 1600364],
    ),
    1600361: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 341000)], flag=51600360
    ),
    1600362: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 342000)], flag=51600360
    ),
    1600363: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 343000)], flag=51600360
    ),
    1600364: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1301000)], flag=51600390
    ),  # FLAG MOD: 51600361 -> 51600390
    1600370: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 0, [ItemLotEntry(ITEM_TYPE.ITEM, 405)], flag=51600370
    ),
    1600380: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 101)], flag=51600380
    ),
    1600500: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 801)],
        flag=51600500,
        needs_flag=True,
        key_name="very_large_ember",
    ),
    1600510: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 1030)], flag=51600510
    ),
    1600520: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 312, count=2)], flag=51600520
    ),
    1700000: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51700000
    ),
    1700010: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1130)], flag=51700010
    ),
    1700020: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1252000)], flag=51700020
    ),
    1700040: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 409)], flag=51700040
    ),
    1700050: ItemLotPart(
        ITEM_DIF.EASY, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 370, count=20)], flag=51700050
    ),
    1700060: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 406)], flag=51700060
    ),
    1700070: ItemLotPart(
        ITEM_DIF.MEDIUM,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 410000)],
        flag=51700070,
        follow_items=[1700071, 1700072, 1700073, 1700074],
    ),
    1700071: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 411000)], flag=51700070
    ),
    1700072: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 412000)], flag=51700070
    ),
    1700073: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 413000)], flag=51700070
    ),
    1700074: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 114)], flag=51700090
    ),  # FLAG MOD: 51700071 -> 51700090
    1700080: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 407)], flag=51700080
    ),
    1700120: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1040)], flag=51700120
    ),
    1700150: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=51700150
    ),
    1700160: ItemLotPart(
        ITEM_DIF.HARD, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1080)], flag=51700160
    ),
    1700170: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1040)], flag=51700170
    ),
    1700180: ItemLotPart(
        ITEM_DIF.BIG_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 408)], flag=51700180
    ),
    1700200: ItemLotPart(
        ITEM_DIF.HARD, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 395)], flag=51700200
    ),
    1700210: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2020)],
        flag=51700210,
        needs_flag=True,
        key_name="archive_prison_extra_key",
    ),
    1700510: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1130)], flag=51700510
    ),
    1700520: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1130)], flag=51700520
    ),
    1700530: ItemLotPart(
        ITEM_DIF.KEY,
        3,
        [ItemLotEntry(ITEM_TYPE.ITEM, 806)],
        flag=51700530,
        needs_flag=True,
        key_name="large_magic_ember",
    ),
    1700540: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3310)], flag=51700540
    ),
    1700560: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1040)], flag=51700560
    ),
    1700580: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 90000)],
        flag=51700580,
        follow_items=[1700581, 1700582, 1700583],
    ),
    1700581: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 91000)], flag=51700580
    ),
    1700582: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 92000)], flag=51700580
    ),
    1700583: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 93000)], flag=51700580
    ),
    1700590: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2006)],
        flag=51700590,
        needs_flag=True,
        key_name="archive_tower_giant_cell_key",
    ),
    1700600: ItemLotPart(
        ITEM_DIF.KEY,
        3,
        [ItemLotEntry(ITEM_TYPE.ITEM, 802)],
        flag=51700600,
        needs_flag=True,
        key_name="crystal_ember",
    ),
    1700630: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2005)],
        flag=51700630,
        needs_flag=True,
        key_name="archive_tower_giant_door_key",
    ),
    1700640: ItemLotPart(
        ITEM_DIF.MEDIUM,
        1,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 381000)],
        flag=51700640,
        follow_items=[1700641, 1700642, 1700643],
    ),
    1700641: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 382000)], flag=51700640
    ),
    1700642: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.ARMOR, 383000)], flag=51700640
    ),
    1700643: ItemLotPart(
        ITEM_DIF.MEDIUM, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1303000)], flag=51700660
    ),  # FLAG MOD: 51700641 -> 51700660
    1700650: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 130000)],
        flag=51700650,
        follow_items=[1700651, 1700652, 1700653],
    ),
    1700651: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 131000)], flag=51700650
    ),
    1700652: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 132000)], flag=51700650
    ),
    1700653: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 133000)], flag=51700650
    ),
    1800050: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 320000)],
        flag=51800050,
        follow_items=[1800051, 1800052, 1800053],
    ),
    1800051: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 321000)], flag=51800050
    ),
    1800052: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 322000)], flag=51800050
    ),
    1800053: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 323000)], flag=51800050
    ),
    1810000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2010)],
        flag=51810000,
        needs_flag=True,
    ),
    1810060: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 125)], flag=51810060
    ),
    1810070: ItemLotPart(
        ITEM_DIF.SMALL_SOUL, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 400)], flag=51810070
    ),
    1810080: ItemLotPart(
        ITEM_DIF.KEY,
        3,
        [ItemLotEntry(ITEM_TYPE.ITEM, 384)],
        flag=51810080,
        needs_flag=True,
        key_name="peculiar_doll",
    ),
    1810100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 4, [ItemLotEntry(ITEM_TYPE.WEAPON, 201000)], flag=51810100
    ),
    1810110: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1450000)],
        flag=51810110,
    ),
    1810120: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 4, [ItemLotEntry(ITEM_TYPE.WEAPON, 202000)], flag=51810120
    ),
    1810130: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1452000)],
        flag=51810130,
    ),
    1810140: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 4, [ItemLotEntry(ITEM_TYPE.WEAPON, 400000)], flag=51810140
    ),
    1810150: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1408000)],
        flag=51810150,
    ),
    1810160: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 4, [ItemLotEntry(ITEM_TYPE.WEAPON, 103000)], flag=51810160
    ),
    1810170: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1404000)],
        flag=51810170,
    ),
    1810180: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 4, [ItemLotEntry(ITEM_TYPE.WEAPON, 701000)], flag=51810180
    ),
    1810190: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1462000)],
        flag=51810190,
    ),
    1810200: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 4, [ItemLotEntry(ITEM_TYPE.WEAPON, 200000)], flag=51810200
    ),
    1810210: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1402000)],
        flag=51810210,
    ),
    1810220: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1200000)],
        flag=51810220,
    ),
    1810221: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 2000000, count=30)],
        flag=51810220,
    ),
    1810230: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 4, [ItemLotEntry(ITEM_TYPE.WEAPON, 100000)], flag=51810230
    ),
    1810240: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1403000)],
        flag=51810240,
    ),
    1810250: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1300000)],
        flag=51810250,
    ),
    1810260: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 4, [ItemLotEntry(ITEM_TYPE.WEAPON, 700000)], flag=51810260
    ),
    1810270: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1406000)],
        flag=51810270,
    ),
    1810280: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1330000)],
        flag=51810280,
    ),
    1810290: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 4, [ItemLotEntry(ITEM_TYPE.WEAPON, 801000)], flag=51810290
    ),
    1810300: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1400000)],
        flag=51810300,
    ),
    1810310: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1361000)],
        flag=51810310,
    ),
    1810320: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 4, [ItemLotEntry(ITEM_TYPE.WEAPON, 800000)], flag=51810320
    ),
    1810330: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        4,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 1409000)],
        flag=51810330,
    ),
    9990000: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=59990000
    ),
    9990010: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=59990010
    ),
    9990011: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=59990011
    ),
    9990020: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=59990020
    ),
    9990021: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=59990021
    ),
    9990022: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=59990022
    ),
    9990030: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=59990030
    ),
    9990031: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=59990031
    ),
    9990032: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=59990032
    ),
    9990033: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=59990033
    ),
    9990034: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.ITEM, 404)], flag=59990034
    ),
    9990100: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1400000)], flag=59990100
    ),
    9990110: ItemLotPart(
        ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 200000)], flag=59990110
    ),
    9990500: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 102000)]),
    9990510: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 104000)]),
    9990520: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 208000)]),
    9990530: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 211000)]),
    9990540: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 306000)]),
    9990550: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 307000)]),
    9990560: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 314000)]),
    9990570: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 309000)]),
    9990580: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 310000)]),
    9990590: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 311000)]),
    9990600: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 354000)]),
    9990610: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 355000)]),
    9990620: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 403000)]),
    9990630: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 406000)]),
    9990640: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 453000)]),
    9990650: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 503000)]),
    9990660: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 603000)]),
    9990670: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 704000)]),
    9990680: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 752000)]),
    9990690: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 753000)]),
    9990700: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 856000)]),
    9990710: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 851000)]),
    9990720: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 854000)]),
    9990730: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 903000)]),
    9990740: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1006000)]),
    9990750: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1051000)]),
    9990760: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1052000)]),
    9990770: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1102000)]),
    9990780: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1105000)]),
    9990790: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1151000)]),
    9990800: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1203000)]),
    9990810: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1205000)]),
    9990820: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1304000)]),
    9990830: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1411000)]),
    9990840: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1456000)]),
    9990850: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1457000)]),
    9990860: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1473000)]),
    9990870: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1474000)]),
    9990880: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1503000)]),
    9990890: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1507000)]),
    9990900: ItemLotPart(ITEM_DIF.IGNORE, 1, [ItemLotEntry(ITEM_TYPE.WEAPON, 1505000)]),
    12000000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=95),
            ItemLotEntry(ITEM_TYPE.ITEM, 500, rate=5, luck=False),
        ],
    ),
    # 12010000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 95), ItemLotEntry(ITEM_TYPE.ITEM, 500, rate = 5, luck = False)]),
    # 12010100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 95), ItemLotEntry(ITEM_TYPE.ITEM, 500, rate = 5, luck = False)]),
    12010200: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.ITEM, 500, rate=3, luck=False),
        ],
    ),
    # 12010300: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.ITEM, 500, rate = 3, luck = False)]),
    12020000: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    # 12030000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 95), ItemLotEntry(ITEM_TYPE.ITEM, 500, rate = 5, luck = False)]),
    20600000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 203000, rate=2, luck=False),
        ],
    ),
    20600100: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1000000, rate=2, luck=False),
        ],
    ),
    20600200: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=64),
            ItemLotEntry(ITEM_TYPE.ITEM, 400, rate=20, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 401, rate=10, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 402, rate=5, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 500, rate=1, luck=False),
        ],
    ),
    22300000: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1070)]),
    22300010: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1307000)]
    ),
    22310000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1307000)]
    ),
    22400000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=95),
            ItemLotEntry(ITEM_TYPE.WEAPON, 352000, rate=5, luck=False),
        ],
    ),
    # 22400100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 95), ItemLotEntry(ITEM_TYPE.WEAPON, 352000, rate = 5, luck = False)]),
    22500000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=95),
            ItemLotEntry(ITEM_TYPE.WEAPON, 751000, rate=5, luck=False),
        ],
    ),
    # 22500200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 95), ItemLotEntry(ITEM_TYPE.WEAPON, 751000, rate = 5, luck = False)]),
    22600000: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1003000, rate=2, luck=False),
        ],
    ),
    22600100: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1003000, rate=2, luck=False),
        ],
    ),
    22700000: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.ITEM, 311, rate=80),
            ItemLotEntry(ITEM_TYPE.ITEM, 311, count=2, rate=20, luck=False),
        ],
    ),
    22700100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    22800000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=95),
            ItemLotEntry(ITEM_TYPE.ITEM, 311, rate=5, luck=False),
        ],
    ),
    22800100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    23000000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1102000)]
    ),
    23000001: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1120)]),
    # 23000100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1102000)]),
    23000101: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1120)]
    ),
    # 23000200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1102000)]),
    23000201: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1120)]
    ),
    # 23000300: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1102000)]),
    23000301: ItemLotPart(ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1120)]),
    # 23000400: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1102000)]),
    23000401: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1120, count=2)]
    ),
    # 23000500: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1102000)]),
    23000501: ItemLotPart(
        ITEM_DIF.NPC_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1120, count=2)]
    ),
    23100000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.ITEM, 374, rate=6, luck=False),
        ],
    ),
    23300000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=55),
            ItemLotEntry(ITEM_TYPE.ITEM, 270, rate=20, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 271, rate=20, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 272, rate=5, luck=False),
        ],
    ),
    # 23300100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 55), ItemLotEntry(ITEM_TYPE.ITEM, 270, rate = 20, luck = False), ItemLotEntry(ITEM_TYPE.ITEM, 271, rate = 20, luck = False), ItemLotEntry(ITEM_TYPE.ITEM, 272, rate = 5, luck = False)]),
    23700000: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1004000, rate=1, luck=False),
        ],
    ),
    # 23700100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.WEAPON, 1004000, rate = 1, luck = False)]),
    # 23700200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.WEAPON, 1004000, rate = 1, luck = False)]),
    23800000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=96),
            ItemLotEntry(ITEM_TYPE.WEAPON, 306000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1503000, rate=2, luck=False),
        ],
    ),
    # 23800100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 96), ItemLotEntry(ITEM_TYPE.WEAPON, 306000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1503000, rate = 2, luck = False)]),
    23900000: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=859),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, rate=80, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, count=2, rate=3, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1070, rate=2, luck=False),
        ],
        follow_items=[23900001],
    ),
    23900001: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.WEAPON, 904000, rate=1, luck=False),
        ],
    ),
    23900220: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=859),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, rate=80, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, count=2, rate=3, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1070, rate=2, luck=False),
        ],
    ),
    24000000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=83),
            ItemLotEntry(ITEM_TYPE.WEAPON, 405000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 290, count=2, rate=10, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 290, count=5, rate=5, luck=False),
        ],
    ),
    24100000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 208000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1473000, rate=1, luck=False),
        ],
    ),
    24100300: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1006000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1473000, rate=1, luck=False),
        ],
    ),
    24100400: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=90),
            ItemLotEntry(ITEM_TYPE.WEAPON, 2007000, rate=7, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 2007000, count=3, rate=3, luck=False),
        ],
    ),
    24300000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    25000000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 203000, rate=2, luck=False),
        ],
    ),
    25000100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    25000200: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1200000, rate=2, luck=False),
        ],
    ),
    # 25000300: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 203000, rate = 2, luck = False)]),
    # 25001000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 203000, rate = 2, luck = False)]),
    # 25001100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0)]),
    # 25001200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 1200000, rate = 2, luck = False)]),
    25002000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    # 25002100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 1200000, rate = 2, luck = False)]),
    # 25002200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 203000, rate = 2, luck = False)]),
    # 25002300: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0)]),
    # 25002400: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 1200000, rate = 2, luck = False)]),
    # 25002500: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 203000, rate = 2, luck = False)]),
    # 25003000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 203000, rate = 2, luck = False)]),
    # 25003100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0)]),
    # 25003200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 203000, rate = 2, luck = False)]),
    25004000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    25100000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    25100100: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 500000)], flag=51010960
    ),
    25200000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 103000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1404000, rate=1, luck=False),
        ],
        follow_items=[25200001, 25200002, 25200003],
    ),
    25200001: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 500000, rate=1, luck=False),
        ],
    ),
    25200002: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 501000, rate=1, luck=False),
        ],
    ),
    25200003: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 503000, rate=1, luck=False),
        ],
    ),
    25300200: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.ITEM, 271, rate=70),
            ItemLotEntry(ITEM_TYPE.ITEM, 271, count=2, rate=30, luck=False),
        ],
        follow_items=[25300201],
    ),
    25300201: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=90),
            ItemLotEntry(ITEM_TYPE.ITEM, 272, rate=10, luck=False),
        ],
    ),
    25400000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 200000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1406000, rate=1, luck=False),
        ],
        follow_items=[25400001, 25400002, 25400003],
    ),
    25400001: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 520000, rate=1, luck=False),
        ],
    ),
    25400002: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 521000, rate=1, luck=False),
        ],
    ),
    25400003: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 523000, rate=1, luck=False),
        ],
    ),
    25400100: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 701000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1406000, rate=1, luck=False),
        ],
        follow_items=[25400101, 25400102, 25400103],
    ),
    25400101: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 520000, rate=1, luck=False),
        ],
    ),
    25400102: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 521000, rate=1, luck=False),
        ],
    ),
    25400103: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 523000, rate=1, luck=False),
        ],
    ),
    25400200: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=88),
            ItemLotEntry(ITEM_TYPE.ITEM, 292, rate=10, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 292, count=2, rate=2, luck=False),
        ],
        follow_items=[25400201, 25400202, 25400203],
    ),
    25400201: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 520000, rate=1, luck=False),
        ],
    ),
    25400202: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 521000, rate=1, luck=False),
        ],
    ),
    25400203: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 523000, rate=1, luck=False),
        ],
    ),
    # 25401000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 200000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1406000, rate = 1, luck = False)], follow_items = [25401001, 25401002, 25401003]),
    # 25401001: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 520000, rate = 1, luck = False)]),
    # 25401002: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 521000, rate = 1, luck = False)]),
    # 25401003: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 523000, rate = 1, luck = False)]),
    # 25401100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 701000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1406000, rate = 1, luck = False)], follow_items = [25401101, 25401102, 25401103]),
    # 25401101: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 520000, rate = 1, luck = False)]),
    # 25401102: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 521000, rate = 1, luck = False)]),
    # 25401103: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 523000, rate = 1, luck = False)]),
    # 25401200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 88), ItemLotEntry(ITEM_TYPE.ITEM, 292, rate = 10, luck = False), ItemLotEntry(ITEM_TYPE.ITEM, 292, count = 2, rate = 2, luck = False)], follow_items = [25401201, 25401202, 25401203]),
    # 25401201: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 520000, rate = 1, luck = False)]),
    # 25401202: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 521000, rate = 1, luck = False)]),
    # 25401203: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 523000, rate = 1, luck = False)]),
    # 25402000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 200000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1406000, rate = 1, luck = False)], follow_items = [25402001, 25402002, 25402003]),
    # 25402001: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 520000, rate = 1, luck = False)]),
    # 25402002: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 521000, rate = 1, luck = False)]),
    # 25402003: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 523000, rate = 1, luck = False)]),
    # 25402100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 701000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1406000, rate = 1, luck = False)], follow_items = [25402101, 25402102, 25402103]),
    # 25402101: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 520000, rate = 1, luck = False)]),
    # 25402102: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 521000, rate = 1, luck = False)]),
    # 25402103: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 523000, rate = 1, luck = False)]),
    # 25402200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 88), ItemLotEntry(ITEM_TYPE.ITEM, 292, rate = 10, luck = False), ItemLotEntry(ITEM_TYPE.ITEM, 292, count = 2, rate = 2, luck = False)], follow_items = [25402201, 25402202, 25402203]),
    # 25402201: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 520000, rate = 1, luck = False)]),
    # 25402202: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 521000, rate = 1, luck = False)]),
    # 25402203: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 523000, rate = 1, luck = False)]),
    25500000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1000000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1454000, rate=1, luck=False),
        ],
        follow_items=[25500001, 25500002, 25500003, 25500004],
    ),
    25500001: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 480000, rate=1, luck=False),
        ],
    ),
    25500002: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 481000, rate=1, luck=False),
        ],
    ),
    25500003: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 483000, rate=1, luck=False),
        ],
    ),
    25500004: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=984),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate=16, luck=False),
        ],
    ),
    25500100: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 201000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1454000, rate=1, luck=False),
        ],
        follow_items=[25500101, 25500102, 25500103, 25500104],
    ),
    25500101: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 480000, rate=1, luck=False),
        ],
    ),
    25500102: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 481000, rate=1, luck=False),
        ],
    ),
    25500103: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 483000, rate=1, luck=False),
        ],
    ),
    25500104: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=984),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate=16, luck=False),
        ],
    ),
    25500200: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1250000, rate=2, luck=False),
        ],
        follow_items=[25500201, 25500202, 25500203, 25500204],
    ),
    25500201: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 480000, rate=1, luck=False),
        ],
    ),
    25500202: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 481000, rate=1, luck=False),
        ],
    ),
    25500203: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 483000, rate=1, luck=False),
        ],
    ),
    25500204: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=984),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate=16, luck=False),
        ],
    ),
    # 25501000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 201000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1454000, rate = 1, luck = False)], follow_items = [25501001, 25501002, 25501003, 25501004]),
    # 25501001: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 480000, rate = 1, luck = False)]),
    # 25501002: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 481000, rate = 1, luck = False)]),
    # 25501003: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 483000, rate = 1, luck = False)]),
    # 25501004: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 984), ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate = 16, luck = False)]),
    # 25502000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 1000000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1454000, rate = 1, luck = False)], follow_items = [25502001, 25502002, 25502003, 25502004]),
    # 25502001: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 480000, rate = 1, luck = False)]),
    # 25502002: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 481000, rate = 1, luck = False)]),
    # 25502003: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 483000, rate = 1, luck = False)]),
    # 25502004: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 984), ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate = 16, luck = False)]),
    # 25502100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 201000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1454000, rate = 1, luck = False)], follow_items = [25502101, 25502102, 25502103, 25502104]),
    # 25502101: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 480000, rate = 1, luck = False)]),
    # 25502102: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 481000, rate = 1, luck = False)]),
    # 25502103: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 483000, rate = 1, luck = False)]),
    # 25502104: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 984), ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate = 16, luck = False)]),
    # 25502200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 1250000, rate = 2, luck = False)], follow_items = [25502201, 25502202, 25502203, 25502204]),
    # 25502201: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 480000, rate = 1, luck = False)]),
    # 25502202: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 481000, rate = 1, luck = False)]),
    # 25502203: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 483000, rate = 1, luck = False)]),
    # 25502204: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 984), ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate = 16, luck = False)]),
    25503000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 201000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1454000, rate=1, luck=False),
        ],
        follow_items=[25503001, 25503002, 25503003, 25503004],
    ),
    25503001: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 480000, rate=1, luck=False),
        ],
    ),
    25503002: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 481000, rate=1, luck=False),
        ],
    ),
    25503003: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 483000, rate=1, luck=False),
        ],
    ),
    25503004: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=996),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate=4, luck=False),
        ],
    ),
    # 25503100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 201000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1454000, rate = 1, luck = False)], follow_items = [25503101, 25503102, 25503103, 25503104]),
    # 25503101: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 480000, rate = 1, luck = False)]),
    # 25503102: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 481000, rate = 1, luck = False)]),
    # 25503103: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 483000, rate = 1, luck = False)]),
    # 25503104: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 984), ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate = 16, luck = False)]),
    # 25503200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 201000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1454000, rate = 1, luck = False)], follow_items = [25503201, 25503202, 25503203, 25503204]),
    # 25503201: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 480000, rate = 1, luck = False)]),
    # 25503202: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 481000, rate = 1, luck = False)]),
    # 25503203: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 483000, rate = 1, luck = False)]),
    # 25503204: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 984), ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate = 16, luck = False)]),
    25600000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 204000, rate=1, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1455000, rate=1, luck=False),
        ],
        follow_items=[25600001, 25600002, 25600003, 25600004, 25600005],
    ),
    25600001: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 510000, rate=1, luck=False),
        ],
    ),
    25600002: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 511000, rate=1, luck=False),
        ],
    ),
    25600003: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 512000, rate=1, luck=False),
        ],
    ),
    25600004: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 513000, rate=1, luck=False),
        ],
    ),
    25600005: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=92),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate=8, luck=False),
        ],
    ),
    25600100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1250000, rate=2, luck=False),
        ],
        follow_items=[25600101, 25600102, 25600103, 25600104, 25600105],
    ),
    25600101: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 510000, rate=1, luck=False),
        ],
    ),
    25600102: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 511000, rate=1, luck=False),
        ],
    ),
    25600103: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 512000, rate=1, luck=False),
        ],
    ),
    25600104: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 513000, rate=1, luck=False),
        ],
    ),
    25600105: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=92),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate=8, luck=False),
        ],
    ),
    25600200: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 601000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1405000, rate=1, luck=False),
        ],
        follow_items=[25600201, 25600202, 25600203, 25600204, 25600205],
    ),
    25600201: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 510000, rate=1, luck=False),
        ],
    ),
    25600202: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 511000, rate=1, luck=False),
        ],
    ),
    25600203: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 512000, rate=1, luck=False),
        ],
    ),
    25600204: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 513000, rate=1, luck=False),
        ],
    ),
    25600205: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=92),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate=8, luck=False),
        ],
    ),
    # 25600300: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 204000, rate = 1, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1455000, rate = 1, luck = False)], follow_items = [25600301, 25600302, 25600303, 25600304, 25600305]),
    # 25600301: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 510000, rate = 1, luck = False)]),
    # 25600302: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 511000, rate = 1, luck = False)]),
    # 25600303: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 512000, rate = 1, luck = False)]),
    # 25600304: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 513000, rate = 1, luck = False)]),
    # 25600305: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 92), ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate = 8, luck = False)]),
    # 25600400: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 601000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1405000, rate = 1, luck = False)], follow_items = [25600401, 25600402, 25600403, 25600404, 25600405]),
    # 25600401: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 510000, rate = 1, luck = False)]),
    # 25600402: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 511000, rate = 1, luck = False)]),
    # 25600403: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 512000, rate = 1, luck = False)]),
    # 25600404: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 513000, rate = 1, luck = False)]),
    # 25600405: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 92), ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate = 8, luck = False)]),
    25601000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 204000, rate=1, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1455000, rate=1, luck=False),
        ],
        follow_items=[25601001, 25601002, 25601003, 25601004, 25601005, 25601006],
    ),
    25601001: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 510000, rate=1, luck=False),
        ],
    ),
    25601002: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 511000, rate=1, luck=False),
        ],
    ),
    25601003: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 512000, rate=1, luck=False),
        ],
    ),
    25601004: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 513000, rate=1, luck=False),
        ],
    ),
    25601005: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=85),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate=24, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, count=2, rate=1, luck=False),
        ],
    ),
    25601006: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate=2, luck=False),
        ],
    ),
    25601100: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1250000, rate=2, luck=False),
        ],
        follow_items=[25601101, 25601102, 25601103, 25601104, 25601105, 25601106],
    ),
    25601101: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 510000, rate=1, luck=False),
        ],
    ),
    25601102: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 511000, rate=1, luck=False),
        ],
    ),
    25601103: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 512000, rate=1, luck=False),
        ],
    ),
    25601104: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 513000, rate=1, luck=False),
        ],
    ),
    25601105: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=85),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate=24, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, count=2, rate=1, luck=False),
        ],
    ),
    25601106: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate=2, luck=False),
        ],
    ),
    25601200: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 601000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1405000, rate=1, luck=False),
        ],
        follow_items=[25601201, 25601202, 25601203, 25601204, 25601205, 25601206],
    ),
    25601201: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 510000, rate=1, luck=False),
        ],
    ),
    25601202: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 511000, rate=1, luck=False),
        ],
    ),
    25601203: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 512000, rate=1, luck=False),
        ],
    ),
    25601204: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 513000, rate=1, luck=False),
        ],
    ),
    25601205: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=85),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate=24, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, count=2, rate=1, luck=False),
        ],
    ),
    25601206: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate=2, luck=False),
        ],
    ),
    # 25601300: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 204000, rate = 1, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1455000, rate = 1, luck = False)], follow_items = [25601301, 25601302, 25601303, 25601304, 25601305, 25601306]),
    # 25601301: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 510000, rate = 1, luck = False)]),
    # 25601302: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 511000, rate = 1, luck = False)]),
    # 25601303: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 512000, rate = 1, luck = False)]),
    # 25601304: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 513000, rate = 1, luck = False)]),
    # 25601305: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 85), ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate = 24, luck = False), ItemLotEntry(ITEM_TYPE.ITEM, 1000, count = 2, rate = 1, luck = False)]),
    # 25601306: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate = 2, luck = False)]),
    # 25601400: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 601000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1405000, rate = 1, luck = False)], follow_items = [25601401, 25601402, 25601403, 25601404, 25601405, 25601406]),
    # 25601401: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 510000, rate = 1, luck = False)]),
    # 25601402: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 511000, rate = 1, luck = False)]),
    # 25601403: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 512000, rate = 1, luck = False)]),
    # 25601404: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 513000, rate = 1, luck = False)]),
    # 25601405: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 85), ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate = 24, luck = False), ItemLotEntry(ITEM_TYPE.ITEM, 1000, count = 2, rate = 1, luck = False)]),
    # 25601406: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate = 2, luck = False)]),
    25700000: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.WEAPON, 351000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 750000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1501000, rate=2, luck=False),
        ],
        follow_items=[25700001, 25700002, 25700003, 25700004, 25700005],
    ),
    25700001: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 490000, rate=1, luck=False),
        ],
    ),
    25700002: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 491000, rate=1, luck=False),
        ],
    ),
    25700003: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 492000, rate=1, luck=False),
        ],
    ),
    25700004: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 493000, rate=1, luck=False),
        ],
    ),
    25700005: ItemLotPart(ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1000)]),
    25700100: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1000)]),
    25700101: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.WEAPON, 351000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 750000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1501000, rate=2, luck=False),
        ],
        follow_items=[25700102, 25700103, 25700104, 25700105],
    ),
    25700102: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 490000, rate=1, luck=False),
        ],
    ),
    25700103: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 491000, rate=1, luck=False),
        ],
    ),
    25700104: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 492000, rate=1, luck=False),
        ],
    ),
    25700105: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 493000, rate=1, luck=False),
        ],
    ),
    25700200: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=294),
            ItemLotEntry(ITEM_TYPE.WEAPON, 351000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 750000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1501000, rate=2, luck=False),
        ],
        follow_items=[25700201, 25700202, 25700203, 25700204, 25700205],
    ),
    25700201: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=299),
            ItemLotEntry(ITEM_TYPE.ARMOR, 490000, rate=1, luck=False),
        ],
    ),
    25700202: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=299),
            ItemLotEntry(ITEM_TYPE.ARMOR, 491000, rate=1, luck=False),
        ],
    ),
    25700203: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=299),
            ItemLotEntry(ITEM_TYPE.ARMOR, 492000, rate=1, luck=False),
        ],
    ),
    25700204: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=299),
            ItemLotEntry(ITEM_TYPE.ARMOR, 493000, rate=1, luck=False),
        ],
    ),
    25700205: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=85),
            ItemLotEntry(ITEM_TYPE.ITEM, 1000, rate=15, luck=False),
        ],
    ),
    25701000: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.WEAPON, 351000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 750000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1501000, rate=2, luck=False),
        ],
        follow_items=[25701001, 25701002, 25701003, 25701004, 25701005],
    ),
    25701001: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 490000, rate=1, luck=False),
        ],
    ),
    25701002: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 491000, rate=1, luck=False),
        ],
    ),
    25701003: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 492000, rate=1, luck=False),
        ],
    ),
    25701004: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 493000, rate=1, luck=False),
        ],
    ),
    25701005: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=75),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate=25, luck=False),
        ],
    ),
    25701100: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.WEAPON, 351000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 750000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1501000, rate=2, luck=False),
        ],
        follow_items=[25701101, 25701102, 25701103, 25701104, 25701105],
    ),
    25701101: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 490000, rate=1, luck=False),
        ],
    ),
    25701102: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 491000, rate=1, luck=False),
        ],
    ),
    25701103: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 492000, rate=1, luck=False),
        ],
    ),
    25701104: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 493000, rate=1, luck=False),
        ],
    ),
    25701105: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=75),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate=25, luck=False),
        ],
    ),
    # 25701200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 94), ItemLotEntry(ITEM_TYPE.WEAPON, 351000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 750000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1501000, rate = 2, luck = False)]),
    # 25701201: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 490000, rate = 1, luck = False)]),
    # 25701202: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 491000, rate = 1, luck = False)]),
    # 25701203: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 492000, rate = 1, luck = False)]),
    # 25701204: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 493000, rate = 1, luck = False)]),
    # 25701205: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 75), ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate = 25, luck = False)]),
    25702000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.WEAPON, 351000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 750000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1501000, rate=2, luck=False),
        ],
        follow_items=[25702001, 25702002, 25702003, 25702004, 25702005],
    ),
    25702001: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 490000, rate=1, luck=False),
        ],
    ),
    25702002: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 491000, rate=1, luck=False),
        ],
    ),
    25702003: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 492000, rate=1, luck=False),
        ],
    ),
    25702004: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 493000, rate=1, luck=False),
        ],
    ),
    25702005: ItemLotPart(ITEM_DIF.NPC_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1010)]),
    25702100: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.WEAPON, 351000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 750000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1501000, rate=2, luck=False),
        ],
        follow_items=[25702101, 25702102, 25702103, 25702104, 25702105],
    ),
    25702101: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 490000, rate=1, luck=False),
        ],
    ),
    25702102: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 491000, rate=1, luck=False),
        ],
    ),
    25702103: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 492000, rate=1, luck=False),
        ],
    ),
    25702104: ItemLotPart(
        ITEM_DIF.IGNORE,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ARMOR, 493000, rate=1, luck=False),
        ],
    ),
    25702105: ItemLotPart(ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1010)]),
    # 25702200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 94), ItemLotEntry(ITEM_TYPE.WEAPON, 351000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 750000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1501000, rate = 2, luck = False)], follow_items = [25702201, 25702202, 25702203, 25702204, 25702205]),
    # 25702201: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 490000, rate = 1, luck = False)]),
    # 25702202: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 491000, rate = 1, luck = False)]),
    # 25702203: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 492000, rate = 1, luck = False)]),
    # 25702204: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.ARMOR, 493000, rate = 1, luck = False)]),
    # 25702205: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1010)]),
    26400000: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 810000)], flag=51010990
    ),
    26500000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1396000)]
    ),
    26600000: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 560000)]),
    26700000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.WEAPON, 403000, rate=1, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 312, count=2, rate=5, luck=False),
        ],
    ),
    26800000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.WEAPON, 102000, rate=1, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 312, count=2, rate=5, luck=False),
        ],
    ),
    26900000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 302000, rate=2, luck=False),
        ],
    ),
    26900100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2004)], flag=51700990
    ),
    # 26900200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 302000, rate = 2, luck = False)]),
    # 26900300: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 302000, rate = 2, luck = False)]),
    27000000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 303000, rate=2, luck=False),
        ],
    ),
    # 27000100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 303000, rate = 2, luck = False)]),
    27100000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=92),
            ItemLotEntry(ITEM_TYPE.ITEM, 1040, rate=8, luck=False),
        ],
    ),
    27100100: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=96),
            ItemLotEntry(ITEM_TYPE.ITEM, 1040, rate=4, luck=False),
        ],
    ),
    27100200: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2520)],
        flag=51700930,
        needs_flag=True,
        key_name="broken_pendant",
    ),
    27110000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    27110100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    27300000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    27310000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 104000)], flag=51100990
    ),
    27800000: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 570000)], flag=51500990
    ),
    27800001: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1000200)], flag=51501000
    ),  # FLAG MOD: 51500991 -> 51501000
    # 27801000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 570000)]),
    27801001: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 800700)], flag=51510980
    ),
    # 27801010: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 570000)]),
    27801011: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1100100)], flag=51510970
    ),
    # 27801020: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 570000)]),
    27801021: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 382, count=5)], flag=51510960
    ),
    # 27801030: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 570000)]),
    27801031: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 383)], flag=51510950
    ),
    # 27802000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 570000)]),
    27802001: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 401500)], flag=51700950
    ),
    # 27802010: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 570000)]),
    27802011: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1451100)], flag=51700940
    ),
    # 27803000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 570000)]),
    27803001: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2022)],
        flag=51210980,
        needs_flag=True,
        key_name="crest_key",
    ),
    # 27803100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 570000)]),
    27803101: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 512)],
        flag=51210920,
        needs_flag=True,
    ),
    # Remove Black Knight Items from RNG Pool and move them to the Item Pool.
    # 27900000: ItemLotPart(ITEM_DIF.NPC_HARD, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 75), ItemLotEntry(ITEM_TYPE.WEAPON, 310000, rate = 20, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1474000, rate = 5, luck = False)], follow_items = [27900001]),
    # 27900100: ItemLotPart(ITEM_DIF.NPC_HARD, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 75), ItemLotEntry(ITEM_TYPE.WEAPON, 355000, rate = 20, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1474000, rate = 5, luck = False)], follow_items = [27900101]),
    # 27901000: ItemLotPart(ITEM_DIF.NPC_HARD, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 75), ItemLotEntry(ITEM_TYPE.WEAPON, 1105000, rate = 20, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1474000, rate = 5, luck = False)], follow_items = [27901001]),
    # 27902000: ItemLotPart(ITEM_DIF.NPC_HARD, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 75), ItemLotEntry(ITEM_TYPE.WEAPON, 753000, rate = 20, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1474000, rate = 5, luck = False)], follow_items = [27902001]),
    # 27903000: ItemLotPart(ITEM_DIF.NPC_HARD, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 75), ItemLotEntry(ITEM_TYPE.WEAPON, 1105000, rate = 20, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1474000, rate = 5, luck = False)], follow_items = [27903001]),
    27900000: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 310000)]),
    27900100: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 355000)]),
    27901000: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1105000)]),
    27902000: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 753000)]),
    27903000: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1474000)]),
    27900001: ItemLotPart(ITEM_DIF.NPC_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1030)]),
    27900101: ItemLotPart(ITEM_DIF.NPC_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1030)]),
    27901001: ItemLotPart(ITEM_DIF.NPC_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1040)]),
    27902001: ItemLotPart(ITEM_DIF.NPC_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1050)]),
    27903001: ItemLotPart(ITEM_DIF.NPC_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1050)]),
    # 27905000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 75), ItemLotEntry(ITEM_TYPE.WEAPON, 310000, rate = 20, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1474000, rate = 5, luck = False)], follow_items = [27905001]),
    # 27905001: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1030)]),
    # 27905100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 75), ItemLotEntry(ITEM_TYPE.WEAPON, 355000, rate = 20, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1474000, rate = 5, luck = False)], follow_items = [27905101]),
    # 27905101: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1060)]),
    # 27905200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 75), ItemLotEntry(ITEM_TYPE.WEAPON, 753000, rate = 20, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1474000, rate = 5, luck = False)], follow_items = [27905201]),
    # 27905201: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1050)]),
    # 27905300: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 75), ItemLotEntry(ITEM_TYPE.WEAPON, 1105000, rate = 20, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1474000, rate = 5, luck = False)], follow_items = [27905301]),
    # 27905301: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1040)]),
    27907000: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    27907001: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=75),
            ItemLotEntry(ITEM_TYPE.WEAPON, 310000, rate=20, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1474000, rate=5, luck=False),
        ],
    ),
    # 27907001: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1060)]),
    27910000: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    28000000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=95),
            ItemLotEntry(ITEM_TYPE.WEAPON, 205000, rate=3, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1477000, rate=2, luck=False),
        ],
    ),
    28000100: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1201000, rate=2, luck=False),
        ],
    ),
    28100000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 855000, rate=2, luck=False),
        ],
        follow_items=[28100001],
    ),
    28100001: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=50),
            ItemLotEntry(ITEM_TYPE.ITEM, 293, rate=50, luck=False),
        ],
    ),
    28110000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=95),
            ItemLotEntry(ITEM_TYPE.WEAPON, 804000, rate=5, luck=False),
        ],
        follow_items=[28110001],
    ),
    28110001: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=50),
            ItemLotEntry(ITEM_TYPE.ITEM, 293, rate=50, luck=False),
        ],
    ),
    28200000: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    28301000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1000000, rate=1, luck=False),
        ],
        follow_items=[28301001],
    ),
    28301001: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1402000, rate=1, luck=False),
        ],
    ),
    28400000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    28400100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    28400200: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4050)], flag=51100980
    ),
    28600000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1030)]
    ),
    28600100: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 811000)], flag=51510940
    ),
    28600200: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, rate=1, luck=False),
        ],
    ),
    28700000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1101000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1502000, rate=1, luck=False),
        ],
        follow_items=[28700001],
    ),
    28700001: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=92),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, rate=8, luck=False),
        ],
    ),
    28701000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1101000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1502000, rate=1, luck=False),
        ],
    ),
    29000000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 400000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1476000, rate=1, luck=False),
        ],
    ),
    29000100: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1200000, rate=2, luck=False),
        ],
    ),
    29000200: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=97),
            ItemLotEntry(ITEM_TYPE.WEAPON, 401000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1476000, rate=1, luck=False),
        ],
    ),
    # 29001000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 400000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1476000, rate = 1, luck = False)]),
    # 29001100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 1200000, rate = 2, luck = False)]),
    # 29001200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 401000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1476000, rate = 1, luck = False)]),
    # 29002000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 400000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1476000, rate = 1, luck = False)]),
    # 29002100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 1200000, rate = 2, luck = False)]),
    # 29002200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 401000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1476000, rate = 1, luck = False)]),
    # 29003000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 400000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1476000, rate = 1, luck = False)]),
    # 29003100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 1200000, rate = 2, luck = False)]),
    # 29003200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 97), ItemLotEntry(ITEM_TYPE.WEAPON, 401000, rate = 2, luck = False), ItemLotEntry(ITEM_TYPE.WEAPON, 1476000, rate = 1, luck = False)]),
    29100000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.WEAPON, 451000, rate=1, luck=False),
        ],
    ),
    29100100: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1201000, rate=2, luck=False),
        ],
    ),
    # 29100200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.WEAPON, 451000, rate = 1, luck = False)]),
    # 29101000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 1201000, rate = 2, luck = False)]),
    # 29101100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.WEAPON, 451000, rate = 1, luck = False)]),
    29101200: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    # 29101300: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 98), ItemLotEntry(ITEM_TYPE.WEAPON, 1201000, rate = 2, luck = False)]),
    29101400: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 451000, rate=2, luck=False),
        ],
    ),
    29200000: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.WEAPON, 812000)],
        flag=51300990,
        follow_items=[29200001],
    ),
    29200001: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 580000)], flag=51301000
    ),  # FLAG MOD: 51300991 -> 51301000
    29200200: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    29300000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=99),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1506000, rate=1, luck=False),
        ],
    ),
    # 29300100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 99), ItemLotEntry(ITEM_TYPE.WEAPON, 1506000, rate = 1, luck = False)]),
    29400000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.ITEM, 500, rate=2, luck=False),
        ],
    ),
    29500000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    29600000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=95),
            ItemLotEntry(ITEM_TYPE.ITEM, 1050, rate=5, luck=False),
        ],
    ),
    30900000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    32000000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=96),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, rate=2, luck=False),
        ],
    ),
    32100000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=95),
            ItemLotEntry(ITEM_TYPE.ITEM, 275, rate=5, luck=False),
        ],
    ),
    32100100: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 275, count=2)], flag=51400980
    ),
    32200000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    32300000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    32300100: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=895),
            ItemLotEntry(ITEM_TYPE.ITEM, 1040, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1040, count=2, rate=3, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1080, rate=2, luck=False),
        ],
    ),
    32400000: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=895),
            ItemLotEntry(ITEM_TYPE.ITEM, 1060, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1050, count=2, rate=3, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1100, rate=2, luck=False),
        ],
    ),
    32500000: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=80),
            ItemLotEntry(ITEM_TYPE.ITEM, 1130, rate=20, luck=False),
        ],
        follow_items=[32500001],
    ),
    32500001: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=90),
            ItemLotEntry(ITEM_TYPE.ITEM, 274, rate=10, luck=False),
        ],
    ),
    # 32500100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 70), ItemLotEntry(ITEM_TYPE.ITEM, 1130, rate = 30, luck = False)], follow_items = [32500101]),
    # 32500101: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 90), ItemLotEntry(ITEM_TYPE.ITEM, 274, rate = 10, luck = False)]),
    32700000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.ITEM, 109, rate=6, luck=False),
        ],
    ),
    # 32700100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 94), ItemLotEntry(ITEM_TYPE.ITEM, 109, rate = 6, luck = False)]),
    33000000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1130, count=2)]
    ),
    33000001: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        3,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=10),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, count=2, rate=20, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2, rate=20, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, rate=10, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1040, rate=10, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1050, rate=10, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1060, rate=10, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1070, rate=10, luck=False),
        ],
    ),
    33001000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1130, count=2)]
    ),
    33001001: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        3,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=30),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2, rate=30, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1040, rate=50),
            ItemLotEntry(ITEM_TYPE.ITEM, 1040, count=2, rate=10, luck=False),
        ],
    ),
    33002000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1130, count=2)]
    ),
    33002001: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        3,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=30),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2, rate=30, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1060, rate=50),
            ItemLotEntry(ITEM_TYPE.ITEM, 1060, count=2, rate=10, luck=False),
        ],
    ),
    33003000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1130, count=2)]
    ),
    33003001: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        3,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=30),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2, rate=30, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1050, rate=50),
            ItemLotEntry(ITEM_TYPE.ITEM, 1050, count=2, rate=10, luck=False),
        ],
    ),
    33004000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1130, count=2)]
    ),
    33004001: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        3,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=30),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, count=2, rate=30, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, rate=50),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, count=2, rate=10, luck=False),
        ],
    ),
    33005000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1130, count=2)]
    ),
    33005001: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        3,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=30),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2, rate=30, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1050, rate=50),
            ItemLotEntry(ITEM_TYPE.ITEM, 1050, count=2, rate=10, luck=False),
        ],
    ),
    33006000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1130, count=2)]
    ),
    33006001: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        3,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=30),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, count=2, rate=30, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, rate=50),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, count=2, rate=10, luck=False),
        ],
    ),
    33007000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1130, count=2)]
    ),
    33007001: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        3,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=30),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, count=2, rate=30, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, rate=50),
            ItemLotEntry(ITEM_TYPE.ITEM, 1030, count=2, rate=10, luck=False),
        ],
    ),
    33007100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1130, count=2)]
    ),
    33007101: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        3,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=30),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2, rate=30, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1040, rate=50),
            ItemLotEntry(ITEM_TYPE.ITEM, 1040, count=2, rate=10, luck=False),
        ],
    ),
    33007200: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1130, count=2)]
    ),
    33007201: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        3,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=30),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2, rate=30, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1060, rate=50),
            ItemLotEntry(ITEM_TYPE.ITEM, 1060, count=2, rate=10, luck=False),
        ],
    ),
    33007300: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 3, [ItemLotEntry(ITEM_TYPE.ITEM, 1130, count=2)]
    ),
    33007301: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        3,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=30),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2, rate=30, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1050, rate=50),
            ItemLotEntry(ITEM_TYPE.ITEM, 1050, count=2, rate=10, luck=False),
        ],
    ),
    # Modify Pinwheel's Mask drop into three separate drops, so that they can be treated as 100% drops,
    #  since it is not clear how this type of drop works in other locations.
    33200000: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 590000)]),
    33200001: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 600000)]),
    33200002: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 610000)]),
    33200100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    33200200: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.ARMOR, 590000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.ARMOR, 600000, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.ARMOR, 610000, rate=2, luck=False),
        ],
        follow_items=[33200201],
    ),
    33200201: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=895),
            ItemLotEntry(ITEM_TYPE.ITEM, 1050, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1050, count=2, rate=3, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1090, rate=2, luck=False),
        ],
    ),
    33300000: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=96),
            ItemLotEntry(ITEM_TYPE.ITEM, 500, rate=4, luck=False),
        ],
    ),
    33300100: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5030)], flag=51700980
    ),
    33300200: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5050)], flag=51700970
    ),
    33400000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    # 33400100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0)]),
    # 33400200: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0)]),
    33410000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    33500000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    33700000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=90),
            ItemLotEntry(ITEM_TYPE.ITEM, 275, rate=10, luck=False),
        ],
    ),
    33800000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=90),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate=5, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=5, rate=2, luck=False),
        ],
    ),
    33900000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=75),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, rate=25, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2, rate=5, luck=False),
        ],
        follow_items=[33900001],
    ),
    33900001: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=95),
            ItemLotEntry(ITEM_TYPE.ITEM, 1060, rate=5, luck=False),
        ],
    ),
    34000000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34100000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=60),
            ItemLotEntry(ITEM_TYPE.ITEM, 260, rate=25, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 260, count=2, rate=15, luck=False),
        ],
    ),
    # 34100100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 60), ItemLotEntry(ITEM_TYPE.ITEM, 260, rate = 25, luck = False), ItemLotEntry(ITEM_TYPE.ITEM, 260, count = 2, rate = 15, luck = False)]),
    34200000: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1110)]),
    34200200: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1110)]),
    34210100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34220000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34300000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34310000: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 211000)], flag=51010980
    ),
    34500000: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34510000: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 354000)], flag=51320990
    ),
    34600000: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 620000)]),
    # 34610000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 620000)]),
    34710000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34720000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9019000)], flag=51210950
    ),
    34720010: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9019000)], flag=51210940
    ),
    34720020: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9019000)], flag=51210930
    ),
    34800000: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=965),
            ItemLotEntry(ITEM_TYPE.ITEM, 1060, rate=5, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 375, rate=30, luck=False),
        ],
    ),
    34800100: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 190000)], flag=51410990
    ),
    34900000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34900100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34900200: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34900300: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34900400: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34900500: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34900600: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34900700: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34900800: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34900900: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34901000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34901100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34901200: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34901300: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34901400: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    34910000: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34910100: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34910200: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34910300: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34910400: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34910500: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34910600: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34910700: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34910800: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34910900: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34911000: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34911100: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34911200: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34911300: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34911400: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)]),
    34920000: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34920100: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34920200: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34920300: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34920400: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34920500: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34920600: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34920700: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34920800: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34920900: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34921000: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34921100: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34921200: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34921300: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    34921400: ItemLotPart(ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)]),
    35000000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    35010000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    # 35010100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0)]),
    35100000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    35200200: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=95),
            ItemLotEntry(ITEM_TYPE.ITEM, 1110, rate=5, luck=False),
        ],
    ),
    # 35200500: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0, rate = 95), ItemLotEntry(ITEM_TYPE.ITEM, 1110, rate = 5, luck = False)]),
    35300000: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1110, count=2)]
    ),
    35300100: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 1110)],
        follow_items=[35300101],
    ),
    35300101: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 116)]),
    35310000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    # 35310100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count = 0)]),
    40900000: ItemLotPart(
        ITEM_DIF.MEDIUM,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 700000)],
        flag=51210990,
        follow_items=[40900001, 40900002, 40900003],
    ),
    40900001: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 701000)], flag=51210990
    ),
    40900002: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 702000)], flag=51210990
    ),
    40900003: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 703000)], flag=51210990
    ),
    40901000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    41000000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    41100000: ItemLotPart(
        ITEM_DIF.EASY,
        2,
        [ItemLotEntry(ITEM_TYPE.ARMOR, 680000)],
        flag=50000510,
        follow_items=[41100001, 41100002, 41100003],
    ),
    41100001: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 681000)], flag=50000510
    ),
    41100002: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 682000)], flag=50000510
    ),
    41100003: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 683000)], flag=50000510
    ),
    # 41100004: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9021000)], flag = 50000540), # FLAG MOD!
    41200000: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=98),
            ItemLotEntry(ITEM_TYPE.WEAPON, 9015000, rate=2, luck=False),
        ],
        follow_items=[41200001],
    ),
    41200001: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=80),
            ItemLotEntry(ITEM_TYPE.ITEM, 1130, rate=20, luck=False),
        ],
    ),
    41300000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=81),
            ItemLotEntry(ITEM_TYPE.ITEM, 270, rate=8, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 271, rate=8, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 272, rate=2, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 9016000, rate=1, luck=False),
        ],
    ),
    41301000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=82),
            ItemLotEntry(ITEM_TYPE.ITEM, 270, rate=8, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 271, rate=8, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 272, rate=2, luck=False),
        ],
    ),
    # 41400000: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 230, count = 3)], flag = 50000520),
    41500000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=995),
            ItemLotEntry(ITEM_TYPE.ARMOR, 710000, rate=5, luck=False),
        ],
        follow_items=[41500001],
    ),
    41500001: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, rate=5, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1010, count=2, rate=1, luck=False),
        ],
    ),
    41600000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=985),
            ItemLotEntry(ITEM_TYPE.ARMOR, 720000, rate=10, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 9018000, rate=5, luck=False),
        ],
        follow_items=[41600001],
    ),
    41600001: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=94),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, rate=5, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 1020, count=2, rate=1, luck=False),
        ],
    ),
    41601000: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 513)],
        flag=51210960,
        needs_flag=True,
    ),
    41700000: ItemLotPart(
        ITEM_DIF.NPC_HARD,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=95),
            ItemLotEntry(ITEM_TYPE.ITEM, 500, rate=10, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 501, rate=5, luck=False),
        ],
    ),
    41710000: ItemLotPart(
        ITEM_DIF.NPC_MEDIUM,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=90),
            ItemLotEntry(ITEM_TYPE.ITEM, 500, rate=8, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 501, rate=2, luck=False),
        ],
    ),
    41720000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=85),
            ItemLotEntry(ITEM_TYPE.ITEM, 500, rate=4, luck=False),
            ItemLotEntry(ITEM_TYPE.ITEM, 501, rate=1, luck=False),
        ],
    ),
    41800000: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=80),
            ItemLotEntry(ITEM_TYPE.ARMOR, 170000, rate=20, luck=False),
        ],
        follow_items=[41800001, 41800002, 41800003],
    ),
    41800001: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=80),
            ItemLotEntry(ITEM_TYPE.ARMOR, 171000, rate=20, luck=False),
        ],
    ),
    41800002: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=80),
            ItemLotEntry(ITEM_TYPE.ARMOR, 172000, rate=20, luck=False),
        ],
    ),
    41800003: ItemLotPart(
        ITEM_DIF.NPC_EASY,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=80),
            ItemLotEntry(ITEM_TYPE.ARMOR, 173000, rate=20, luck=False),
        ],
    ),
    41900000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    45000000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    45100000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    45110000: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9020000)], flag=51210970
    ),
    45200000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 9014000)], flag=51210910
    ),
    52000000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    52010000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    52020000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    52100000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    52200000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    52300000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    52400000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    52500000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    52600000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    52610000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 752000)], flag=51000990
    ),
    52710000: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 144)]),
    52800000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    52900000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    52900100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    52910000: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 309000)], flag=51700960
    ),
    53100000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    53300000: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    53300100: ItemLotPart(
        ITEM_DIF.IGNORE, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    53400000: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 392)], flag=51400990
    ),
    53500000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1103000)]
    ),
    53500001: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1478000)]
    ),
    53500002: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 630000)]),
    # 53500100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1103000)]),
    # 53500101: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 630000)]),
    53510000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [
            ItemLotEntry(ITEM_TYPE.NONE, 0, count=0, rate=91),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1103000, rate=3, luck=False),
            ItemLotEntry(ITEM_TYPE.WEAPON, 1478000, rate=3, luck=False),
            ItemLotEntry(ITEM_TYPE.ARMOR, 630000, rate=3, luck=False),
        ],
    ),
    53520000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 705000)], flag=51010970
    ),
    53530000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 705000)], flag=51510990
    ),
    53600000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    53610000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    53900000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    53900100: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    54000000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    54010000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.NONE, 0, count=0)]
    ),
    # Shop items:
    60000001: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 240, count=-1)]
    ),
    # 60001100: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 106)], flag = 11017020, needs_flag = True),
    60001101: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 280)]
    ),
    60001102: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 290)]
    ),
    60001103: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 292)]
    ),
    60001104: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 296)]
    ),
    # 60001105: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2021)], flag = 11017030, needs_flag = True),
    # 60001106: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2602)] flag = 11017040, needs_flag = True),
    60001107: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 100000)]),
    60001108: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 200000)]),
    60001110: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 400000)]),
    60001111: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 601000)]),
    60001112: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 700000)]),
    60001113: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 800000)]),
    60001114: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 809000)]),
    60001115: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1000000)]),
    60001116: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1200000)]),
    60001117: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1400000)]),
    60001118: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1403000)]),
    60001119: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1405000)]
    ),
    60001120: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1408000)]),
    60001121: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1450000)]),
    60001122: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1460000)]),
    60001123: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2000000)]
    ),
    60001124: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2001000)]
    ),
    60001125: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2006000)]
    ),
    60001126: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2100000)]
    ),
    60001127: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2101000)]
    ),
    60001128: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2103000)]
    ),
    60001129: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 170000)]),
    60001130: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 171000)]),
    60001131: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 172000)]),
    60001132: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 173000)]),
    60001133: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2608)],
        flag=11007010,
        needs_flag=True,
    ),
    60001200: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 270)]
    ),
    60001201: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 271)]
    ),
    60001202: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 272)]
    ),
    60001203: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 291)]
    ),
    60001204: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 293)]
    ),
    60001205: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 294)]
    ),
    60001206: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 310)]
    ),
    60001207: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 312, count=4)], flag=11017190
    ),
    60001208: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 313)]
    ),
    60001209: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 330)]
    ),
    60001210: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 370)]
    ),
    60001211: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500)], flag=11027020
    ),
    60001212: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2003000)]
    ),
    60001213: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2004000)]
    ),
    60001214: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 274)]
    ),
    60001215: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2000000)]
    ),
    60001216: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2001000)]
    ),
    60001217: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2006000)]
    ),
    60001218: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2100000)]
    ),
    60001219: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2101000)]
    ),
    60001220: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2103000)]
    ),
    60005300: ItemLotPart(
        ITEM_DIF.SALABLE_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 260)]
    ),
    60005301: ItemLotPart(
        ITEM_DIF.SALABLE_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 297)]
    ),
    60005302: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1000)]
    ),
    60005303: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1010)]
    ),
    60005304: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1020)]
    ),
    60005306: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.RING, 106)], flag=11507030
    ),
    60005307: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.RING, 107)], flag=11507040
    ),
    60005308: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 351000)]),
    60005309: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 750000)]),
    60005310: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1455000)]),
    60005311: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1501000)]),
    60005312: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2000000)]
    ),
    60005313: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2001000)]
    ),
    60005314: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2002000)]
    ),
    60005315: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2100000)]
    ),
    60005316: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2101000)]
    ),
    60005317: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2102000)]
    ),
    60005318: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 10000)]),
    60005319: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 11000)]),
    60005320: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 12000)]),
    60005321: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 13000)]),
    60005322: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 490000)]),
    60005323: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 491000)]),
    60005324: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 492000)]),
    60005325: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 493000)]),
    60005326: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 510000)]),
    60005327: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 511000)]),
    60005328: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 512000)]),
    60005329: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 513000)]),
    60001400: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1000)]
    ),
    # 60001401: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2002)], flag = 11017140),
    60001402: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2600)],
        flag=11017150,
        needs_flag=True,
    ),
    60001403: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2601)],
        flag=11017160,
        needs_flag=True,
    ),
    60001404: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2602)],
        flag=11017170,
        needs_flag=True,
    ),
    60001405: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 201000)]),
    60001406: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 202000)]),
    60001407: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 300000)]),
    60001408: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 701000)]),
    60001409: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 803000)]),
    60001410: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 901000)]),
    60001411: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1050000)]
    ),
    60001412: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1402000)]),
    60001413: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1452000)]
    ),
    60001414: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1477000)]
    ),
    60001415: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2000000)]
    ),
    60001416: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2001000)]
    ),
    60001417: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2006000)]
    ),
    60001418: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2100000)]
    ),
    60001419: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2101000)]
    ),
    60001420: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2103000)]
    ),
    60001500: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 311, count=3)], flag=11007000
    ),
    # 60001501: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2608, flag = 11007010, needs_flag = True)]),
    60001502: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 205000)]),
    60001503: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 304000)]),
    60001504: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1471000)]),
    60001505: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 110000)]),
    60001506: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 111000)]),
    60001507: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 112000)]),
    60001508: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 113000)]),
    60001509: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2000000)]
    ),
    60001510: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2001000)]
    ),
    60001511: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2006000)]
    ),
    60001512: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2100000)]
    ),
    60001513: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2101000)]
    ),
    60001514: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2103000)]
    ),
    60001550: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 470000)]),
    60001551: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 471000)]),
    60001552: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 472000)]),
    60001553: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 473000)]),
    60001554: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 80000)]),
    60001555: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 81000)]),
    60001556: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 82000)]),
    60001557: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 83000)]),
    60001558: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 270000)]),
    60001559: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 271000)]),
    60001560: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 272000)]),
    60001561: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 273000)]),
    60001562: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 540000)]),
    60001563: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 541000)]),
    60001564: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 542000)]),
    60001565: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 543000)]),
    60001566: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 550000)]),
    60001567: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 551000)]),
    60001568: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 552000)]),
    60001569: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 553000)]),
    60001580: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 2100)],
        flag=11007020,
        needs_flag=True,
    ),
    60001581: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 660000)]),
    60001582: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 661000)]),
    60001583: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 662000)]),
    60001584: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 663000)]),
    60001600: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 109, count=3)], flag=11307000
    ),
    60001601: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 240)], flag=11027040
    ),
    60001602: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 370)]
    ),
    60001603: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=3)], flag=11027050
    ),
    60001604: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 501)], flag=11307010
    ),
    60001605: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5000)], flag=11027090
    ),
    60001606: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5020)], flag=11027100
    ),
    60001607: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 702000)], flag=11307020
    ),
    60001608: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 801000)]),
    60001609: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1361000)]
    ),
    60001610: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1362000)]
    ),
    60001611: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 590000)]),
    60001612: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 600000)]),
    60001613: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 610000)]),
    60001614: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 180000)]),
    60001615: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 181000)]),
    60001616: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 182000)]),
    60001617: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 183000)]),
    60001700: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 145)], flag=11407000
    ),
    60001701: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 303000)]),
    60001702: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 306000)]),
    60001703: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 352000)]),
    60001704: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 402000)]),
    60001705: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 500000)]),
    60001706: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 501000)]),
    60001707: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 751000)]),
    60001708: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 902000)]),
    60001709: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1003000)]
    ),
    60002000: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3000)]),
    60002001: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3010)]),
    60002002: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3020)]),
    60002003: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3030)]),
    60002004: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3100)]),
    60002005: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3300)]),
    60002006: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3520)]),
    60002007: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3540)]),
    60002008: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 115)]),
    60002009: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 141)]),
    60002010: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1300000)]),
    60002020: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3040)]),
    60002021: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3060)]),
    60002100: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3000)], flag=11607120
    ),
    60002101: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3020)], flag=11607130
    ),
    # Leave the Sorcerer's Catalyst that Rickert sells alone, so that it can be always
    #  sold in case the player needs the key item Cast Light and has no other catalysts.
    60002102: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1300000, count=-1)]
    ),
    60002200: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3400)], flag=11207000
    ),
    60002201: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3410)], flag=11207010
    ),
    60002202: ItemLotPart(
        ITEM_DIF.KEY,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 3500)],
        flag=11207020,
        key_name="cast_light",
    ),
    60002203: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3530)], flag=11207030
    ),
    60002204: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3550)], flag=11207040
    ),
    60002205: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1305000)]),
    60002400: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3600)]),
    60002401: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 312)]
    ),
    60003000: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4000)], flag=11407030
    ),
    60003001: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4010)], flag=11407040
    ),
    60003002: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4100)], flag=11407050
    ),
    60003003: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4300)], flag=11407060
    ),
    60003004: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4310)], flag=11407070
    ),
    60003200: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 112)],
        flag=11407080,
        needs_flag=True,
    ),
    60003210: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 275)]
    ),
    60003211: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4200)], flag=11407090
    ),
    60003212: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4210)], flag=11407100
    ),
    60003400: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4000)]),
    60003401: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4010)]),
    60003402: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4020)]),
    60003403: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4030)]),
    60003404: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4060)]),
    60003405: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4100)]),
    60003406: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4110)]),
    60003407: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 4360)]),
    60004000: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5000)], flag=11027260
    ),
    60004001: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5020)], flag=11027270
    ),
    60004002: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5210)], flag=11027280
    ),
    60004003: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5300)], flag=11027290
    ),
    60004004: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5400)], flag=11017180
    ),
    60004005: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1360000)]
    ),
    60004006: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1362000)]
    ),
    60004200: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 240)]),
    60004201: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5000)]),
    60004205: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5010)]),
    60004202: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5020)]),
    60004203: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5210)]),
    60004204: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5300)]),
    60004206: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5310)]),
    60004207: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5400)]),
    60004208: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5600)]),
    60004209: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1360000)]),
    60004400: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 108)],
        flag=11607020,
        needs_flag=True,
    ),
    60004401: ItemLotPart(
        ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 274, count=5)], flag=11607110
    ),
    60004402: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 373)]),
    60004403: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 5700)]),
    60004404: ItemLotPart(
        ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1367000)]
    ),
    60004405: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 109)]),
    60004406: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.RING, 110)]),
    60004407: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.RING, 126, count=10)]
    ),
    60004408: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 330)]
    ),
    60005000: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3000)]),
    60005001: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3010)]),
    60005002: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3020)]),
    60005003: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3030)]),
    60005004: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3040)]),
    60005005: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3060)]),
    60005006: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3100)]),
    60005007: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3300)]),
    60005020: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3050)]),
    60005021: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3070)]),
    60005022: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3120)]),
    60006100: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 111)]
    ),
    60006200: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1101000)]),
    60006201: ItemLotPart(ITEM_DIF.EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1502000)]),
    60006202: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2005000)]
    ),
    60006203: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2007000)]
    ),
    60006204: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2000000)]
    ),
    60006205: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2001000)]
    ),
    60006206: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2002000)]
    ),
    60006207: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2104000)]
    ),
    60006208: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2100000)]
    ),
    60006209: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2101000)]
    ),
    60006210: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2102000)]
    ),
    60006211: ItemLotPart(ITEM_DIF.MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 530000)]),
    60006212: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 531000)]),
    60006213: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 532000)]),
    60006214: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ARMOR, 533000)]),
    # 60006215: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2600)], flag = 11017150, needs_flag = True),
    # 60006216: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2601)], flag = 11017160, needs_flag = True),
    # 60006217: ItemLotPart(ITEM_DIF.DUPLCIATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2602)], flag = 11017170, needs_flag = True),
    60006218: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1000)]
    ),
    60006219: ItemLotPart(
        ITEM_DIF.SALABLE_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1010)]
    ),
    60006220: ItemLotPart(
        ITEM_DIF.SALABLE_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1020)]
    ),
    60006221: ItemLotPart(
        ITEM_DIF.SALABLE_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1130)]
    ),
    60006300: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 330)]
    ),
    60006301: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1000)]
    ),
    # 60006302: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2600)], flag = 11017150),
    # 60006303: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2601)], flag = 11017160),
    # 60006304: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 2602)], flag = 11017170),
    60006305: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2000000)]
    ),
    60006306: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2001000)]
    ),
    60006307: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2006000)]
    ),
    60006308: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2100000)]
    ),
    60006309: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2101000)]
    ),
    60006310: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2103000)]
    ),
    60006410: ItemLotPart(
        ITEM_DIF.SALABLE_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 260)]
    ),
    60006411: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 270)]
    ),
    60006412: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 271)]
    ),
    60006413: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 272)]
    ),
    60006414: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 290)]
    ),
    60006415: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 292)]
    ),
    60006416: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 294)]
    ),
    60006417: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 296)]
    ),
    60006418: ItemLotPart(
        ITEM_DIF.SALABLE_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 297)]
    ),
    60006419: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 330)]
    ),
    60006420: ItemLotPart(
        ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 500, count=13)], flag=11217100
    ),
    60006421: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2000000)]
    ),
    60006422: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2001000)]
    ),
    60006423: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2002000)]
    ),
    60006424: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2100000)]
    ),
    60006425: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2101000)]
    ),
    60006426: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2102000)]
    ),
    60006500: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 280)]
    ),
    60006501: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 311, count=6)],
        flag=11217000,
        needs_flag=True,
    ),
    # 60006502: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3400, flag = 11207000)]),
    # 60006503: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3410, flag = 11207010)]),
    # 60006504: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3500, flag = 11207020)]),
    # 60006505: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3530, flag = 11207030)]),
    # 60006506: ItemLotPart(ITEM_DIF.DUPLICATE, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 3550, flag = 11207040)]),
    60006507: ItemLotPart(ITEM_DIF.HARD, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 1305000)]),
    60006600: ItemLotPart(
        ITEM_DIF.SALABLE_HARD, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 293)]
    ),
    60006601: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 330)]
    ),
    60006602: ItemLotPart(
        ITEM_DIF.SALABLE_EASY, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 370)]
    ),
    60006603: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 510)],
        flag=11217010,
        needs_flag=True,
    ),
    60006604: ItemLotPart(
        ITEM_DIF.HARD,
        2,
        [ItemLotEntry(ITEM_TYPE.ITEM, 511)],
        flag=11217020,
        needs_flag=True,
    ),
    60006608: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1000)]
    ),
    60006609: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1010)]
    ),
    60006610: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.ITEM, 1020)]
    ),
    60006611: ItemLotPart(
        ITEM_DIF.SALABLE_MEDIUM, 2, [ItemLotEntry(ITEM_TYPE.WEAPON, 2008000)]
    ),
    60010000: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3000, count=-1)]
    ),
    60010001: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3010, count=-1)]
    ),
    60010002: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3020, count=-1)]
    ),
    60010003: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3030, count=-1)]
    ),
    60010004: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3040, count=-1)]
    ),
    60010005: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3050, count=-1)]
    ),
    60010008: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3060, count=-1)]
    ),
    60010009: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3070, count=-1)]
    ),
    60010010: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3100, count=-1)]
    ),
    60010011: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3110, count=-1)]
    ),
    60010012: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3120, count=-1)]
    ),
    60010013: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3300, count=-1)]
    ),
    60010014: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3310, count=-1)]
    ),
    60010015: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3400, count=-1)]
    ),
    60010016: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3410, count=-1)]
    ),
    60010017: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3500, count=-1)]
    ),
    60010018: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3510, count=-1)]
    ),
    60010019: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3520, count=-1)]
    ),
    60010020: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3530, count=-1)]
    ),
    60010021: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3540, count=-1)]
    ),
    60010022: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3550, count=-1)]
    ),
    60010023: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3600, count=-1)]
    ),
    60010024: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3610, count=-1)]
    ),
    60010025: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3700, count=-1)]
    ),
    60010026: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4000, count=-1)]
    ),
    60010027: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4010, count=-1)]
    ),
    60010028: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4020, count=-1)]
    ),
    60010029: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4030, count=-1)]
    ),
    60010030: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4040, count=-1)]
    ),
    60010031: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4050, count=-1)]
    ),
    60010034: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4060, count=-1)]
    ),
    60010035: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4100, count=-1)]
    ),
    60010036: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4110, count=-1)]
    ),
    60010037: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4200, count=-1)]
    ),
    60010038: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4210, count=-1)]
    ),
    60010039: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4220, count=-1)]
    ),
    60010040: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4300, count=-1)]
    ),
    60010041: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4310, count=-1)]
    ),
    60010042: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4360, count=-1)]
    ),
    60010043: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4400, count=-1)]
    ),
    60010044: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4500, count=-1)]
    ),
    60010045: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4510, count=-1)]
    ),
    60010046: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4520, count=-1)]
    ),
    60010047: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5000, count=-1)]
    ),
    60010048: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5010, count=-1)]
    ),
    60010049: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5020, count=-1)]
    ),
    60010050: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5030, count=-1)]
    ),
    60010051: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5040, count=-1)]
    ),
    60010052: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5050, count=-1)]
    ),
    60010053: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5100, count=-1)]
    ),
    60010054: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5110, count=-1)]
    ),
    60010055: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5200, count=-1)]
    ),
    60010056: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5210, count=-1)]
    ),
    60010057: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5300, count=-1)]
    ),
    60010058: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5310, count=-1)]
    ),
    60010059: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5320, count=-1)]
    ),
    60010060: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5400, count=-1)]
    ),
    60010061: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5500, count=-1)]
    ),
    60010062: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5510, count=-1)]
    ),
    60010063: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5520, count=-1)]
    ),
    60010064: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5600, count=-1)]
    ),
    60010065: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5610, count=-1)]
    ),
    60010066: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5700, count=-1)]
    ),
    60010068: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5800, count=-1)]
    ),
    60010069: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5810, count=-1)]
    ),
    60010070: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5900, count=-1)]
    ),
    60010071: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 5910, count=-1)]
    ),
    60010072: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3710, count=-1)]
    ),
    60010073: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3720, count=-1)]
    ),
    60010074: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3730, count=-1)]
    ),
    60010075: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 3740, count=-1)]
    ),
    60010076: ItemLotPart(
        ITEM_DIF.NOT_IN_POOL, 2, [ItemLotEntry(ITEM_TYPE.SHOP_SPELL, 4530, count=-1)]
    ),
}


UPGRADES = [
    (1030, 2),
    (1040, 2),
    (1050, 2),
    (1060, 2),
    (1110, 1),
    (1120, 1),
    (1130, 1),
]  # Will have 100% drop chance.
RANDOM_UPGRADE_COMMON = [(1000, 3), (1010, 2), (1020, 2)]  # Will have 30% drop chance.
RANDOM_UPGRADE_UNCOMMON = [
    (1030, 1),
    (1040, 1),
    (1050, 1),
    (1060, 1),
]  # Will have 25% drop chance.
RANDOM_UPGRADE_RARE = [
    (1030, 2),
    (1040, 2),
    (1050, 2),
    (1060, 2),
    (1110, 1),
    (1120, 1),
    (1130, 1),
]  # Will have 20% drop chance.
RANDOM_UPGRADE_ULTRARARE = [
    (1070, 1),
    (1080, 1),
    (1090, 1),
    (1100, 1),
    (1110, 2),
    (1120, 2),
    (1130, 2),
]  # Will have 15% drop chance.

# (consumable_type, consumable_id, min_amount, max_amount)
RANDOM_CONSUMABLES = [
    (ITEM_TYPE.ITEM, 230, 1, 1),  # Elizabeth's Mushroom
    (ITEM_TYPE.ITEM, 240, 1, 1),  # Divine Blessing
    (ITEM_TYPE.ITEM, 260, 1, 2),  # Green Blossom
    (ITEM_TYPE.ITEM, 270, 2, 4),  # Bloodred Moss Clump
    (ITEM_TYPE.ITEM, 271, 2, 4),  # Purple Moss Clump
    (ITEM_TYPE.ITEM, 272, 1, 2),  # Blooming Purple Moss Clump
    (ITEM_TYPE.ITEM, 274, 1, 2),  # Purging Stone
    (ITEM_TYPE.ITEM, 275, 1, 1),  # Egg Vermifuge
    (ITEM_TYPE.ITEM, 280, 1, 3),  # Repair Powder
    (ITEM_TYPE.ITEM, 290, 5, 10),  # Throwing Knife
    (ITEM_TYPE.ITEM, 291, 5, 10),  # Poison Throwing Knife
    (ITEM_TYPE.ITEM, 293, 1, 1),  # Dung Pie
    (ITEM_TYPE.ITEM, 294, 3, 5),  # Alluring Skull
    (ITEM_TYPE.ITEM, 296, 1, 4),  # Lloyd's Talisman
    (ITEM_TYPE.ITEM, 297, 5, 10),  # Black Firebomb
    (ITEM_TYPE.ITEM, 310, 1, 3),  # Charcoal Pine Resin
    (ITEM_TYPE.ITEM, 311, 1, 3),  # Gold Pine Resin
    (ITEM_TYPE.ITEM, 312, 2, 4),  # Transient Curse
    (ITEM_TYPE.ITEM, 313, 1, 3),  # Rotten Pine Resin
    (ITEM_TYPE.ITEM, 330, 1, 4),  # Homeward Bone
    (ITEM_TYPE.ITEM, 370, 1, 10),  # Prism Stone
    (ITEM_TYPE.ITEM, 376, 1, 1),  # Pendant
    (ITEM_TYPE.ITEM, 380, 1, 1),  # Rubbish
    (ITEM_TYPE.ITEM, 381, 1, 3),  # Copper Coin
    (ITEM_TYPE.ITEM, 382, 1, 3),  # Silver Coin
    (ITEM_TYPE.ITEM, 383, 1, 3),  # Gold Coin
    (ITEM_TYPE.ITEM, 408, 1, 1),  # Soul of a Hero
    (ITEM_TYPE.ITEM, 409, 1, 1),  # Soul of a Great Hero
    (ITEM_TYPE.ITEM, 500, 1, 4),  # Humanity
    (ITEM_TYPE.ITEM, 501, 1, 2),  # Twin Humanities
    (ITEM_TYPE.ITEM, 1000, 1, 5),  # Titanite Shard
    (ITEM_TYPE.ITEM, 1000, 1, 5),  # Titanite Shard (Duplicate)
    (ITEM_TYPE.ITEM, 1010, 1, 5),  # Large Titanite Shard
    (ITEM_TYPE.ITEM, 1010, 1, 5),  # Large Titanite Shard (Duplicate)
    (ITEM_TYPE.ITEM, 1020, 1, 5),  # Green Titanite Shard
    (ITEM_TYPE.ITEM, 1020, 1, 5),  # Green Titanite Shard (Duplicate)
    (ITEM_TYPE.ITEM, 1130, 1, 1),  # Twinkling Titanite
    (ITEM_TYPE.WEAPON, 2000000, 10, 50),  # Standard Arrow
    (ITEM_TYPE.WEAPON, 2001000, 10, 50),  # Large Arrow
    (ITEM_TYPE.WEAPON, 2002000, 10, 50),  # Feather Arrow
    (ITEM_TYPE.WEAPON, 2003000, 10, 50),  # Fire Arrow
    (ITEM_TYPE.WEAPON, 2004000, 10, 50),  # Poison Arrow
    (ITEM_TYPE.WEAPON, 2005000, 10, 50),  # Moonlight Arrow
    (ITEM_TYPE.WEAPON, 2006000, 10, 50),  # Wooden Arrow
    (ITEM_TYPE.WEAPON, 2007000, 5, 25),  # Dragonslayer Arrow
    (ITEM_TYPE.WEAPON, 2008000, 5, 25),  # Gough's Great Arrow
    (ITEM_TYPE.WEAPON, 2100000, 10, 50),  # Standard Bolt
    (ITEM_TYPE.WEAPON, 2101000, 10, 50),  # Heavy Bolt
    (ITEM_TYPE.WEAPON, 2102000, 10, 50),  # Sniper Bolt
    (ITEM_TYPE.WEAPON, 2103000, 10, 50),  # Wood Bolt
    (ITEM_TYPE.WEAPON, 2104000, 10, 50),  # Lightning Bolt
]


def boss_weapon_list_helper(min_index, max_index):
    return [(ITEM_TYPE.WEAPON, i) for i in range(min_index, max_index + 1, 100)]


BOSS_SOUL_ITEMS = {
    700: [
        boss_weapon_list_helper(406000, 406500),
        boss_weapon_list_helper(503000, 503200),
    ],
    701: [
        boss_weapon_list_helper(1507000, 1510600),
        boss_weapon_list_helper(311000, 312700),
        boss_weapon_list_helper(307000, 307100),
    ],
    702: [boss_weapon_list_helper(314000, 315700), [(ITEM_TYPE.ITEM, 5520)]],
    703: [
        boss_weapon_list_helper(704000, 704600),
        boss_weapon_list_helper(903000, 903100),
    ],
    704: [boss_weapon_list_helper(1051000, 1051900) + [(ITEM_TYPE.WEAPON, 1054000)]],
    705: [
        boss_weapon_list_helper(1052000, 1053000),
        boss_weapon_list_helper(1411000, 1414600),
    ],
    706: [boss_weapon_list_helper(856000, 857100)],
    707: [boss_weapon_list_helper(1151000, 1151800)],
    708: [
        boss_weapon_list_helper(1205000, 1205300),
        boss_weapon_list_helper(1304000, 1304500),
    ],
    709: [[(ITEM_TYPE.ITEM, 709)]],  # Sanctuary Guardian has no boss item.
    710: [
        boss_weapon_list_helper(9012000, 9012800)
        + boss_weapon_list_helper(9013000, 9013700)
    ],
    711: [boss_weapon_list_helper(9017000, 9017500)],
}
