from item_randomizer.locations_setup import LOCATIONS

def convert_locations_to_list():
    """
    This converted the original locations dict into a new LOCATIONS_LIST list
    """


    location_list = [item.better_repr for item in LOCATIONS.values()]
    print("[")
    for item in location_list:
        print(f"    {item},")
    print("]")
