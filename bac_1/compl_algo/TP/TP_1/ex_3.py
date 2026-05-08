maps = {
    (1, 1): 20,
    (3, 2): 40,
    (5,5): 10
}
maps2 = {
    (100, 1): 20,
    (3, 2): 40,
    (5,5): 10
}


def get_treasure(maps, coords):
    if coords in maps:
        return maps[coords]
    return 0

def add_treasure(maps, coords, amount):
    maps[coords] = amount
    
def set_treasure(maps, coords, amount):
    if amount == 0:
        del maps[coords]
    else:
        add_treasure(maps, coords, amount)

def add_map(map1, map2):
    return map1 | map2

print(get_treasure(maps, (1,1)))
set_treasure(maps, (1,1), 0)
print(add_map(maps, maps2))
print(get_treasure(maps, (1,1)))