maps = {
    (1, 1): 20,
    (3, 2): 40,
    (5,5): 10
}

def get_treasure(maps, coords):
    if coords in maps:
        return maps[coords]
    return 0

def add_treasure(maps, coords, amount):
    maps[coords] = amount

print(get_treasure(maps, (1,1)))
add_treasure(maps, (1,1), 200)
print(get_treasure(maps, (1,1)))