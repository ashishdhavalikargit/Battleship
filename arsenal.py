from collections import defaultdict,OrderedDict


class BattleShip(object):
    """docstring for BattleShip"""

    def __init__(self):
        self.grid_start_header = 65
        self.grid = defaultdict(list)
        self.ship_type = {"cargo ship": 3, "subsubmarine": 2}
        self.occupancy = []
        self.attack_history = {}

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
        new_occupancy = []

        if direction.lower() == "right":
            ocean_value = range(ship_index - 1, (ship_index + ship_value - 1))
            if self.__collaps(ocean_value, horizental=ship_header.upper()):
                return False, "Ships are colliding"
            for i in ocean_value:
                self.grid[ship_header.upper()][i] = True
                new_occupancy.append(ship_header.upper() + ":" + str(i+1))

        if direction.lower() == "left":
            ocean_value = range((ship_index - ship_value), ship_index)
            if self.__collaps(ocean_value, horizental=ship_header.upper()):
                return False, "Ships are colliding"
            for i in ocean_value:
                self.grid[ship_header.upper()][i] = True
                new_occupancy.append(ship_header.upper() + ":" + str(i+1))

        if direction.lower() == "up":
            ship_header = ship_header.upper()
            ocean_value = range(ord(ship_header), (ord(ship_header) - ship_value), -1)
            if self.__collaps(ocean_value, vertical=(ship_index - 1)):
                return False, "Ships are colliding"
            for i in ocean_value:
                self.grid[chr(i)][ship_index - 1] = True
                new_occupancy.append(chr(i) + ":" + str(ship_index))

        if direction.lower() == "down":
            ship_header = ship_header.upper()
            ocean_value = range(ord(ship_header), (ord(ship_header) + ship_value))
            if self.__collaps(ocean_value, vertical=(ship_index - 1)):
                return False, "Ships are colliding"
            for i in ocean_value:
                self.grid[chr(i)][ship_index - 1] = True
                new_occupancy.append(chr(i) + ":" + str(ship_index))
        self.occupancy.append(new_occupancy)
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

    def attack(self, position):
        status = "miss"
        position = position.strip().upper()
        if position in self.attack_history:
            return "already present", False
        ships = len(self.occupancy)
        for ship_occupancy in self.occupancy:
            if position in ship_occupancy:
                ship_occupancy.remove(position)
                status = "hit"
                ship_header, ship_index = position.split(":")
                ship_index = int(ship_index) - 1
                self.grid[ship_header][ship_index] = False
                break
        self.occupancy = [occupancy for occupancy in self.occupancy if occupancy]
        if len(self.occupancy) != ships:
            status += " and destroyed"
        if not self.occupancy:
            status = "GAME OVER"
        self.attack_history.update({position : status})
        return status, True 

