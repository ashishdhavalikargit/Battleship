from collections import defaultdict,OrderedDict


class BattleShip(object):
    """docstring for BattleShip"""

    def __init__(self):
        self.grid_start_header = 65
        self.grid = defaultdict(list)
        self.ship_type = {"cargo ship": 3, "boat": 2}

    def create_grid(self, grid_width=5, grid_length=5):
        self.grid_width = grid_width
        self.grid_length = grid_length
        for row in range(self.grid_start_header, (self.grid_start_header + grid_width)):
            for column in range(1, grid_length + 1):
                self.grid[chr(row)].append(False)
        self.grid = OrderedDict(sorted(self.grid.items()))

    def create_ship(self, ship_type, start, direction):
        ship_value = self.ship_type[ship_type]
        ship_header, ship_index = start.split(":")  # value must separated in colons ex-> A:3
        ship_index = int(ship_index)

        if direction.lower() == "right":
            ocean_value = range(ship_index - 1, (ship_index + ship_value - 1))
            if self.__collaps(ocean_value, horizental=ship_header.upper()):
                return False, "Ships are colliding"
            for i in ocean_value:
                self.grid[ship_header.upper()][i] = True

        if direction.lower() == "left":
            ocean_value = range((ship_index - ship_value), ship_index)
            if self.__collaps(ocean_value, horizental=ship_header.upper()):
                return False, "Ships are colliding"
            for i in ocean_value:
                self.grid[ship_header.upper()][i] = True

        if direction.lower() == "up":
            ship_header = ship_header.upper()
            ocean_value = range(ord(ship_header), (ord(ship_header) - ship_value), -1)
            if self.__collaps(ocean_value, vertical=(ship_index - 1)):
                return False, "Ships are colliding"
            for i in ocean_value:
                self.grid[chr(i)][ship_index - 1] = True

        if direction.lower() == "down":
            ship_header = ship_header.upper()
            ocean_value = range(ord(ship_header), (ord(ship_header) + ship_value))
            if self.__collaps(ocean_value, vertical=(ship_index - 1)):
                return False, "Ships are colliding"
            for i in ocean_value:
                self.grid[chr(i)][ship_index - 1] = True
        return True, "Ships are ready for battle"

    def show_ships(self):
        count = 0
        print("     " + "    ".join([str(i) for i in range(1, self.grid_length + 1)]))
        for i in self.grid:
            print("\n")
            count += 1
            print(i + "    " + "    ".join([chr(36) if j else chr(34) for j in self.grid[i]]))

    def __collaps(self, ocean_value, horizental="empty", vertical="empty"):
        if horizental != "empty":
            result = any([self.grid[horizental][i] for i in ocean_value])
        if vertical != "empty":
            result = any([self.grid[chr(i)][vertical] for i in ocean_value])
        return result




###  for testing purpose  ###
"""
test = BattleShip()
test.create_grid()
print("\n" * 3)
print(test.create_ship("cargo ship", "a:3", "left"))
test.create_ship("boat", "c:4", "down")
test.create_ship("boat", "e:1", "up")
print(test.create_ship("boat", "e:2", "right"))
test.show_ships()
"""

