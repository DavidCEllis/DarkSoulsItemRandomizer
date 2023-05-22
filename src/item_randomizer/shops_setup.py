from . import items_setup as item_s
from . import locations_setup as loc_s

# qwc_id should match the count of the shop item (including -1 for items
#  that can be infinitely purchased), so it is not included here.
class ShopData:
    def __init__(self, shop_id, cost = -1, shop_type = 0, mtrl_id = -1):
        self.shop_id = shop_id
        self.cost = cost
        self.shop_type = shop_type
        self.mtrl_id = mtrl_id

DEFAULT_SHOP_DATA = {
 60000001: ShopData(1, cost = 100),
 60001100: ShopData(1100, cost = 100),
 60001101: ShopData(1101, cost = 500),
 60001102: ShopData(1102, cost = 10),
 60001103: ShopData(1103, cost = 50),
 60001104: ShopData(1104, cost = 500),
 60001105: ShopData(1105, cost = 1000),
 60001106: ShopData(1106, cost = 3000),
 60001107: ShopData(1107, cost = 300),
 60001108: ShopData(1108, cost = 600),
 60001110: ShopData(1110, cost = 600),
 60001111: ShopData(1111, cost = 600),
 60001112: ShopData(1112, cost = 450),
 60001113: ShopData(1113, cost = 150),
 60001114: ShopData(1114, cost = 350),
 60001115: ShopData(1115, cost = 600),
 60001116: ShopData(1116, cost = 1000),
 60001117: ShopData(1117, cost = 400),
 60001118: ShopData(1118, cost = 600),
 60001119: ShopData(1119, cost = 800),
 60001120: ShopData(1120, cost = 800),
 60001121: ShopData(1121, cost = 1000),
 60001122: ShopData(1122, cost = 800),
 60001123: ShopData(1123, cost = 10),
 60001124: ShopData(1124, cost = 50),
 60001125: ShopData(1125, cost = 3),
 60001126: ShopData(1126, cost = 30),
 60001127: ShopData(1127, cost = 100),
 60001128: ShopData(1128, cost = 10),
 60001129: ShopData(1129, cost = 500),
 60001130: ShopData(1130, cost = 800),
 60001131: ShopData(1131, cost = 500),
 60001132: ShopData(1132, cost = 500),
 60001133: ShopData(1133, cost = 1000),
 60001134: ShopData(1134, cost = 2000),
 60001200: ShopData(1200, cost = 300),
 60001201: ShopData(1201, cost = 500),
 60001202: ShopData(1202, cost = 1000),
 60001203: ShopData(1203, cost = 100),
 60001204: ShopData(1204, cost = 200),
 60001205: ShopData(1205, cost = 500),
 60001206: ShopData(1206, cost = 500),
 60001207: ShopData(1207, cost = 4000),
 60001208: ShopData(1208, cost = 1000),
 60001209: ShopData(1209, cost = 500),
 60001210: ShopData(1210, cost = 10),
 60001211: ShopData(1211, cost = 5000),
 60001212: ShopData(1212, cost = 100),
 60001213: ShopData(1213, cost = 100),
 60001214: ShopData(1214, cost = 6000),
 60001215: ShopData(1215, cost = 10),
 60001216: ShopData(1216, cost = 50),
 60001217: ShopData(1217, cost = 3),
 60001218: ShopData(1218, cost = 30),
 60001219: ShopData(1219, cost = 100),
 60001220: ShopData(1220, cost = 10),
 60005300: ShopData(5300, cost = 1000),
 60005301: ShopData(5301, cost = 500),
 60005302: ShopData(5302, cost = 1000),
 60005303: ShopData(5303, cost = 4000),
 60005304: ShopData(5304, cost = 5000),
 60005306: ShopData(5306, cost = 15000),
 60005307: ShopData(5307, cost = 15000),
 60005308: ShopData(5308, cost = 8000),
 60005309: ShopData(5309, cost = 8000),
 60005310: ShopData(5310, cost = 4000),
 60005311: ShopData(5311, cost = 8000),
 60005312: ShopData(5312, cost = 10),
 60005313: ShopData(5313, cost = 50),
 60005314: ShopData(5314, cost = 100),
 60005315: ShopData(5315, cost = 30),
 60005316: ShopData(5316, cost = 100),
 60005317: ShopData(5317, cost = 250),
 60005318: ShopData(5318, cost = 10000),
 60005319: ShopData(5319, cost = 10000),
 60005320: ShopData(5320, cost = 7000),
 60005321: ShopData(5321, cost = 7000),
 60005322: ShopData(5322, cost = 5000),
 60005323: ShopData(5323, cost = 8000),
 60005324: ShopData(5324, cost = 5000),
 60005325: ShopData(5325, cost = 5000),
 60005326: ShopData(5326, cost = 5000),
 60005327: ShopData(5327, cost = 8000),
 60005328: ShopData(5328, cost = 5000),
 60005329: ShopData(5329, cost = 5000),
 60001400: ShopData(1400, cost = 800),
 60001401: ShopData(1401, cost = 20000),
 60001402: ShopData(1402, cost = 2000),
 60001403: ShopData(1403, cost = 2000),
 60001404: ShopData(1404, cost = 2000),
 60001405: ShopData(1405, cost = 1000),
 60001406: ShopData(1406, cost = 1000),
 60001407: ShopData(1407, cost = 3000),
 60001408: ShopData(1408, cost = 1000),
 60001409: ShopData(1409, cost = 800),
 60001410: ShopData(1410, cost = 200),
 60001411: ShopData(1411, cost = 2000),
 60001412: ShopData(1412, cost = 800),
 60001413: ShopData(1413, cost = 1000),
 60001414: ShopData(1414, cost = 1000),
 60001415: ShopData(1415, cost = 10),
 60001416: ShopData(1416, cost = 50),
 60001417: ShopData(1417, cost = 3),
 60001418: ShopData(1418, cost = 30),
 60001419: ShopData(1419, cost = 100),
 60001420: ShopData(1420, cost = 10),
 60001500: ShopData(1500, cost = 1000),
 60001501: ShopData(1501, cost = 1000),
 60001502: ShopData(1502, cost = 4000),
 60001503: ShopData(1503, cost = 6000),
 60001504: ShopData(1504, cost = 4000),
 60001505: ShopData(1505, cost = 12000),
 60001506: ShopData(1506, cost = 15000),
 60001507: ShopData(1507, cost = 10000),
 60001508: ShopData(1508, cost = 10000),
 60001509: ShopData(1509, cost = 10),
 60001510: ShopData(1510, cost = 50),
 60001511: ShopData(1511, cost = 3),
 60001512: ShopData(1512, cost = 30),
 60001513: ShopData(1513, cost = 100),
 60001514: ShopData(1514, cost = 10),
 60001550: ShopData(1550, cost = 5000),
 60001551: ShopData(1551, cost = 7000),
 60001552: ShopData(1552, cost = 5000),
 60001553: ShopData(1553, cost = 5000),
 60001554: ShopData(1554, cost = 6000),
 60001555: ShopData(1555, cost = 7000),
 60001556: ShopData(1556, cost = 5000),
 60001557: ShopData(1557, cost = 5000),
 60001558: ShopData(1558, cost = 7000),
 60001559: ShopData(1559, cost = 8000),
 60001560: ShopData(1560, cost = 6000),
 60001561: ShopData(1561, cost = 6000),
 60001562: ShopData(1562, cost = 10000),
 60001563: ShopData(1563, cost = 10000),
 60001564: ShopData(1564, cost = 10000),
 60001565: ShopData(1565, cost = 10000),
 60001566: ShopData(1566, cost = 20000),
 60001567: ShopData(1567, cost = 20000),
 60001568: ShopData(1568, cost = 20000),
 60001569: ShopData(1569, cost = 20000),
 60001580: ShopData(1580, cost = 5000),
 60001581: ShopData(1581, cost = 20000),
 60001582: ShopData(1582, cost = 20000),
 60001583: ShopData(1583, cost = 20000),
 60001584: ShopData(1584, cost = 20000),
 60001600: ShopData(1600, cost = 3000),
 60001601: ShopData(1601, cost = 20000),
 60001602: ShopData(1602, cost = 10),
 60001603: ShopData(1603, cost = 10000),
 60001604: ShopData(1604, cost = 20000),
 60001605: ShopData(1605, cost = 5000),
 60001606: ShopData(1606, cost = 10000),
 60001607: ShopData(1607, cost = 10000),
 60001608: ShopData(1608, cost = 3000),
 60001609: ShopData(1609, cost = 1000),
 60001610: ShopData(1610, cost = 5000),
 60001611: ShopData(1611, cost = 8000),
 60001612: ShopData(1612, cost = 8000),
 60001613: ShopData(1613, cost = 8000),
 60001614: ShopData(1614, cost = 5000),
 60001615: ShopData(1615, cost = 7000),
 60001616: ShopData(1616, cost = 5000),
 60001617: ShopData(1617, cost = 5000),
 60001700: ShopData(1700, cost = 10000),
 60001701: ShopData(1701, cost = 10000),
 60001702: ShopData(1702, cost = 15000),
 60001703: ShopData(1703, cost = 10000),
 60001704: ShopData(1704, cost = 10000),
 60001705: ShopData(1705, cost = 5000),
 60001706: ShopData(1706, cost = 20000),
 60001707: ShopData(1707, cost = 10000),
 60001708: ShopData(1708, cost = 5000),
 60001709: ShopData(1709, cost = 15000),
 60002000: ShopData(2000, cost = 1000),
 60002001: ShopData(2001, cost = 6000),
 60002002: ShopData(2002, cost = 2000),
 60002003: ShopData(2003, cost = 8000),
 60002004: ShopData(2004, cost = 3000),
 60002005: ShopData(2005, cost = 3000),
 60002006: ShopData(2006, cost = 1000),
 60002007: ShopData(2007, cost = 1500),
 60002008: ShopData(2008, cost = 20000),
 60002009: ShopData(2009, cost = 20000),
 60002010: ShopData(2010, cost = 500),
 60002020: ShopData(2020, cost = 20000),
 60002021: ShopData(2021, cost = 40000),
 60002100: ShopData(2100, cost = 2000),
 60002101: ShopData(2101, cost = 4000),
 
 # Modify the Sorcerer's Catalyst that Rickert sells to have a
 #  high price, so that it is a last resort.
 60002102: ShopData(2102, cost = 500000),
 
 60002200: ShopData(2200, cost = 2000),
 60002201: ShopData(2201, cost = 2000),
 60002202: ShopData(2202, cost = 1000),
 60002203: ShopData(2203, cost = 10000),
 60002204: ShopData(2204, cost = 3000),
 60002205: ShopData(2205, cost = 1000),
 60002400: ShopData(2400, cost = 5000),
 60002401: ShopData(2401, cost = 1000),
 60003000: ShopData(3000, cost = 800),
 60003001: ShopData(3001, cost = 8000),
 60003002: ShopData(3002, cost = 500),
 60003003: ShopData(3003, cost = 2000),
 60003004: ShopData(3004, cost = 2000),
 60003200: ShopData(3200, cost = 500),
 60003210: ShopData(3210, cost = 1000),
 60003211: ShopData(3211, cost = 10000),
 60003212: ShopData(3212, cost = 25000),
 60003400: ShopData(3400, cost = 800),
 60003401: ShopData(3401, cost = 8000),
 60003402: ShopData(3402, cost = 20000),
 60003403: ShopData(3403, cost = 30000),
 60003404: ShopData(3404, cost = 10000),
 60003405: ShopData(3405, cost = 500),
 60003406: ShopData(3406, cost = 5000),
 60003407: ShopData(3407, cost = 10000),
 60004000: ShopData(4000, cost = 4000),
 60004001: ShopData(4001, cost = 10000),
 60004002: ShopData(4002, cost = 8000),
 60004003: ShopData(4003, cost = 4000),
 60004004: ShopData(4004, cost = 2000),
 60004005: ShopData(4005, cost = 1000),
 60004006: ShopData(4006, cost = 5000),
 60004200: ShopData(4200, cost = 1000),
 60004201: ShopData(4201, cost = 1000),
 60004205: ShopData(4205, cost = 10000),
 60004202: ShopData(4202, cost = 2000),
 60004203: ShopData(4203, cost = 1000),
 60004204: ShopData(4204, cost = 1000),
 60004206: ShopData(4206, cost = 10000),
 60004207: ShopData(4207, cost = 500),
 60004208: ShopData(4208, cost = 6000),
 60004209: ShopData(4209, cost = 200),
 60004400: ShopData(4400, cost = 1000),
 60004401: ShopData(4401, cost = 3000),
 60004402: ShopData(4402, cost = 200),
 60004403: ShopData(4403, cost = 40000),
 60004404: ShopData(4404, cost = 5000),
 60004405: ShopData(4405, cost = 10000),
 60004406: ShopData(4406, cost = 15000),
 60004407: ShopData(4407, cost = 5000),
 60004408: ShopData(4408, cost = 500),
 60005000: ShopData(5000, cost = 1000),
 60005001: ShopData(5001, cost = 6000),
 60005002: ShopData(5002, cost = 2000),
 60005003: ShopData(5003, cost = 8000),
 60005004: ShopData(5004, cost = 20000),
 60005005: ShopData(5005, cost = 40000),
 60005006: ShopData(5006, cost = 3000),
 60005007: ShopData(5007, cost = 3000),
 60005020: ShopData(5020, cost = 30000),
 60005021: ShopData(5021, cost = 50000),
 60005022: ShopData(5022, cost = 20000),
 60006100: ShopData(6100, cost = 3000),
 60006200: ShopData(6200, cost = 5000),
 60006201: ShopData(6201, cost = 10000),
 60006202: ShopData(6202, cost = 500),
 60006203: ShopData(6203, cost = 500),
 60006204: ShopData(6204, cost = 10),
 60006205: ShopData(6205, cost = 50),
 60006206: ShopData(6206, cost = 100),
 60006207: ShopData(6207, cost = 700),
 60006208: ShopData(6208, cost = 30),
 60006209: ShopData(6209, cost = 100),
 60006210: ShopData(6210, cost = 250),
 60006211: ShopData(6211, cost = 6000),
 60006212: ShopData(6212, cost = 8000),
 60006213: ShopData(6213, cost = 6000),
 60006214: ShopData(6214, cost = 6000),
 60006215: ShopData(6215, cost = 2000),
 60006216: ShopData(6216, cost = 2000),
 60006217: ShopData(6217, cost = 2000),
 60006218: ShopData(6218, cost = 800),
 60006219: ShopData(6219, cost = 3800),
 60006220: ShopData(6220, cost = 4800),
 60006221: ShopData(6221, cost = 8000),
 60006300: ShopData(6300, cost = 500),
 60006301: ShopData(6301, cost = 800),
 60006302: ShopData(6302, cost = 2000),
 60006303: ShopData(6303, cost = 2000),
 60006304: ShopData(6304, cost = 2000),
 60006305: ShopData(6305, cost = 10),
 60006306: ShopData(6306, cost = 50),
 60006307: ShopData(6307, cost = 3),
 60006308: ShopData(6308, cost = 30),
 60006309: ShopData(6309, cost = 100),
 60006310: ShopData(6310, cost = 10),
 60006410: ShopData(6410, cost = 1200),
 60006411: ShopData(6411, cost = 400),
 60006412: ShopData(6412, cost = 600),
 60006413: ShopData(6413, cost = 1500),
 60006414: ShopData(6414, cost = 30),
 60006415: ShopData(6415, cost = 100),
 60006416: ShopData(6416, cost = 800),
 60006417: ShopData(6417, cost = 800),
 60006418: ShopData(6418, cost = 800),
 60006419: ShopData(6419, cost = 600),
 60006420: ShopData(6420, cost = 10000),
 60006421: ShopData(6421, cost = 20),
 60006422: ShopData(6422, cost = 100),
 60006423: ShopData(6423, cost = 200),
 60006424: ShopData(6424, cost = 50),
 60006425: ShopData(6425, cost = 150),
 60006426: ShopData(6426, cost = 400),
 60006500: ShopData(6500, cost = 300),
 60006501: ShopData(6501, cost = 1000),
 60006502: ShopData(6502, cost = 2000),
 60006503: ShopData(6503, cost = 2000),
 60006504: ShopData(6504, cost = 1000),
 60006505: ShopData(6505, cost = 10000),
 60006506: ShopData(6506, cost = 3000),
 60006507: ShopData(6507, cost = 1000),
 60006600: ShopData(6600, cost = 200),
 60006601: ShopData(6601, cost = 300),
 60006602: ShopData(6602, cost = 10),
 60006603: ShopData(6603, cost = 5),
 60006604: ShopData(6604, cost = 5),
 60006608: ShopData(6608, cost = 800),
 60006609: ShopData(6609, cost = 3800),
 60006610: ShopData(6610, cost = 4800),
 60006611: ShopData(6611, cost = 650),
 60010000: ShopData(10000, shop_type = 2, cost = 0, mtrl_id = 3000),
 60010001: ShopData(10001, shop_type = 2, cost = 0, mtrl_id = 3010),
 60010002: ShopData(10002, shop_type = 2, cost = 0, mtrl_id = 3020),
 60010003: ShopData(10003, shop_type = 2, cost = 0, mtrl_id = 3030),
 60010004: ShopData(10004, shop_type = 2, cost = 0, mtrl_id = 3040),
 60010005: ShopData(10005, shop_type = 2, cost = 0, mtrl_id = 3050),
 60010008: ShopData(10008, shop_type = 2, cost = 0, mtrl_id = 3060),
 60010009: ShopData(10009, shop_type = 2, cost = 0, mtrl_id = 3070),
 60010010: ShopData(10010, shop_type = 2, cost = 0, mtrl_id = 3100),
 60010011: ShopData(10011, shop_type = 2, cost = 0, mtrl_id = 3110),
 60010012: ShopData(10012, shop_type = 2, cost = 0, mtrl_id = 3120),
 60010013: ShopData(10013, shop_type = 2, cost = 0, mtrl_id = 3300),
 60010014: ShopData(10014, shop_type = 2, cost = 0, mtrl_id = 3310),
 60010015: ShopData(10015, shop_type = 2, cost = 0, mtrl_id = 3400),
 60010016: ShopData(10016, shop_type = 2, cost = 0, mtrl_id = 3410),
 60010017: ShopData(10017, shop_type = 2, cost = 0, mtrl_id = 3500),
 60010018: ShopData(10018, shop_type = 2, cost = 0, mtrl_id = 3510),
 60010019: ShopData(10019, shop_type = 2, cost = 0, mtrl_id = 3520),
 60010020: ShopData(10020, shop_type = 2, cost = 0, mtrl_id = 3530),
 60010021: ShopData(10021, shop_type = 2, cost = 0, mtrl_id = 3540),
 60010022: ShopData(10022, shop_type = 2, cost = 0, mtrl_id = 3550),
 60010023: ShopData(10023, shop_type = 2, cost = 0, mtrl_id = 3600),
 60010024: ShopData(10024, shop_type = 2, cost = 0, mtrl_id = 3610),
 60010025: ShopData(10025, shop_type = 2, cost = 0, mtrl_id = 3700),
 60010026: ShopData(10026, shop_type = 2, cost = 0, mtrl_id = 4000),
 60010027: ShopData(10027, shop_type = 2, cost = 0, mtrl_id = 4010),
 60010028: ShopData(10028, shop_type = 2, cost = 0, mtrl_id = 4020),
 60010029: ShopData(10029, shop_type = 2, cost = 0, mtrl_id = 4030),
 60010030: ShopData(10030, shop_type = 2, cost = 0, mtrl_id = 4040),
 60010031: ShopData(10031, shop_type = 2, cost = 0, mtrl_id = 4050),
 60010034: ShopData(10034, shop_type = 2, cost = 0, mtrl_id = 4060),
 60010035: ShopData(10035, shop_type = 2, cost = 0, mtrl_id = 4100),
 60010036: ShopData(10036, shop_type = 2, cost = 0, mtrl_id = 4110),
 60010037: ShopData(10037, shop_type = 2, cost = 0, mtrl_id = 4200),
 60010038: ShopData(10038, shop_type = 2, cost = 0, mtrl_id = 4210),
 60010039: ShopData(10039, shop_type = 2, cost = 0, mtrl_id = 4220),
 60010040: ShopData(10040, shop_type = 2, cost = 0, mtrl_id = 4300),
 60010041: ShopData(10041, shop_type = 2, cost = 0, mtrl_id = 4310),
 60010042: ShopData(10042, shop_type = 2, cost = 0, mtrl_id = 4360),
 60010043: ShopData(10043, shop_type = 2, cost = 0, mtrl_id = 4400),
 60010044: ShopData(10044, shop_type = 2, cost = 0, mtrl_id = 4500),
 60010045: ShopData(10045, shop_type = 2, cost = 0, mtrl_id = 4510),
 60010046: ShopData(10046, shop_type = 2, cost = 0, mtrl_id = 4520),
 60010047: ShopData(10047, shop_type = 2, cost = 0, mtrl_id = 5000),
 60010048: ShopData(10048, shop_type = 2, cost = 0, mtrl_id = 5010),
 60010049: ShopData(10049, shop_type = 2, cost = 0, mtrl_id = 5020),
 60010050: ShopData(10050, shop_type = 2, cost = 0, mtrl_id = 5030),
 60010051: ShopData(10051, shop_type = 2, cost = 0, mtrl_id = 5040),
 60010052: ShopData(10052, shop_type = 2, cost = 0, mtrl_id = 5050),
 60010053: ShopData(10053, shop_type = 2, cost = 0, mtrl_id = 5100),
 60010054: ShopData(10054, shop_type = 2, cost = 0, mtrl_id = 5110),
 60010055: ShopData(10055, shop_type = 2, cost = 0, mtrl_id = 5200),
 60010056: ShopData(10056, shop_type = 2, cost = 0, mtrl_id = 5210),
 60010057: ShopData(10057, shop_type = 2, cost = 0, mtrl_id = 5300),
 60010058: ShopData(10058, shop_type = 2, cost = 0, mtrl_id = 5310),
 60010059: ShopData(10059, shop_type = 2, cost = 0, mtrl_id = 5320),
 60010060: ShopData(10060, shop_type = 2, cost = 0, mtrl_id = 5400),
 60010061: ShopData(10061, shop_type = 2, cost = 0, mtrl_id = 5500),
 60010062: ShopData(10062, shop_type = 2, cost = 0, mtrl_id = 5510),
 60010063: ShopData(10063, shop_type = 2, cost = 0, mtrl_id = 5520),
 60010064: ShopData(10064, shop_type = 2, cost = 0, mtrl_id = 5600),
 60010065: ShopData(10065, shop_type = 2, cost = 0, mtrl_id = 5610),
 60010066: ShopData(10066, shop_type = 2, cost = 0, mtrl_id = 5700),
 60010068: ShopData(10068, shop_type = 2, cost = 0, mtrl_id = 5800),
 60010069: ShopData(10069, shop_type = 2, cost = 0, mtrl_id = 5810),
 60010070: ShopData(10070, shop_type = 2, cost = 0, mtrl_id = 5900),
 60010071: ShopData(10071, shop_type = 2, cost = 0, mtrl_id = 5910),
 60010072: ShopData(10072, shop_type = 2, cost = 0, mtrl_id = 3710),
 60010073: ShopData(10073, shop_type = 2, cost = 0, mtrl_id = 3720),
 60010074: ShopData(10074, shop_type = 2, cost = 0, mtrl_id = 3730),
 60010075: ShopData(10075, shop_type = 2, cost = 0, mtrl_id = 3740),
 60010076: ShopData(10076, shop_type = 2, cost = 0, mtrl_id = 4530)
}

SALABLE_MIN_SELL_PRICE = {
 (item_s.ITEM_TYPE.ITEM, 111): 500,
 (item_s.ITEM_TYPE.ITEM, 260): 50,
 (item_s.ITEM_TYPE.ITEM, 270): 50,
 (item_s.ITEM_TYPE.ITEM, 271): 50,
 (item_s.ITEM_TYPE.ITEM, 272): 50,
 (item_s.ITEM_TYPE.ITEM, 274): 1000,
 (item_s.ITEM_TYPE.ITEM, 275): 200,
 (item_s.ITEM_TYPE.ITEM, 280): 50,
 (item_s.ITEM_TYPE.ITEM, 290): 10,
 (item_s.ITEM_TYPE.ITEM, 291): 50,
 (item_s.ITEM_TYPE.ITEM, 292): 50,
 (item_s.ITEM_TYPE.ITEM, 293): 200,
 (item_s.ITEM_TYPE.ITEM, 294): 50,
 (item_s.ITEM_TYPE.ITEM, 296): 50,
 (item_s.ITEM_TYPE.ITEM, 297): 50,
 (item_s.ITEM_TYPE.ITEM, 310): 50,
 (item_s.ITEM_TYPE.ITEM, 312): 50,
 (item_s.ITEM_TYPE.ITEM, 313): 50,
 (item_s.ITEM_TYPE.ITEM, 330): 50,
 (item_s.ITEM_TYPE.ITEM, 370): 10,
 (item_s.ITEM_TYPE.ITEM, 1000): 50,
 (item_s.ITEM_TYPE.ITEM, 1010): 50,
 (item_s.ITEM_TYPE.ITEM, 1020): 50,
 (item_s.ITEM_TYPE.ITEM, 1130): 100,
 (item_s.ITEM_TYPE.WEAPON, 2000000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2001000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2002000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2003000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2004000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2005000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2006000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2007000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2008000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2100000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2101000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2102000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2103000): 5,
 (item_s.ITEM_TYPE.WEAPON, 2104000): 5
}

PRICE_DISTIBUTION = {
 loc_s.LOC_DIF.EASY: [1, 10000] * 1 + [10, 5000] * 4 + [50, 250] * 5 + [100, 200, 300, 750, 1000, 2000] * 10 + [500] * 20,
 loc_s.LOC_DIF.MEDIUM: [300, 50000, 500000, 1000000] * 1 + [500, 20000] * 3 + [750, 17000] * 5 + [1000, 2000, 3000, 7500, 10000, 15000] * 10 + [5000] * 20,
 loc_s.LOC_DIF.HARD: [1000, 1000000] * 1  + [2000, 100000] * 24 + [4000, 50000, 75000] * 50 + [5000, 7500, 10000, 15000, 30000, 40000] * 100 + [20000] * 200,
 loc_s.LOC_DIF.SHOP_EASY: [20] * 15 + [50] * 15 + [100] * 40 + [500] * 20 + [1000] * 10 + [2000] * 10,
 loc_s.LOC_DIF.SHOP_MEDIUM: [50] * 15 + [100] * 15 + [200] * 30 + [500] * 20 + [1000] * 10 + [2000] * 5 + [5000] * 5,
 loc_s.LOC_DIF.SHOP_HARD: [1000] * 10 + [2000] * 10 + [5000] * 20 + [7500] * 20 + [10000] * 20 + [20000] * 10 + [30000] * 5 + [40000] * 4 + [50000] * 1
}

for v in PRICE_DISTIBUTION:
    PRICE_DISTIBUTION[v].sort()
