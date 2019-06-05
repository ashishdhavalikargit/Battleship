from collections import defaultdict

class BattleShip(object):
	"""docstring for BattleShip"""
	def __init__(self):
		self.grid_start_header = 65
		self.grid = defaultdict(list)
		self.ship_type = { "cargo ship" : 3, "boat" : 2}

	def create_grid(self, grid_width=5, grid_length=5):
		self.grid_width = grid_width
		self.grid_length = grid_length
		for row in range(self.grid_start_header, (self.grid_start_header + grid_width)):
			for column in range(1,grid_length + 1):
				self.grid[chr(row)].append(False)

	def create_ship(self, ship_type, start, direction):
		ship_value = self.ship_type[ship_type]
		ship_header, ship_index = start.split(":") # value must separated in colons ex-> A:3
		ship_index = int(ship_index)
		
		if direction.lower() == "right":
			for i in range(ship_index - 1, (ship_index + ship_value - 1)):
				self.grid[ship_header.upper()][i] = True
		
		if direction.lower() == "left":
			for i in range((ship_index - ship_value), ship_index):
				self.grid[ship_header.upper()][i] = True

	def show_ships(self):
		count = 0
		print("     " + "    ".join([str(i) for i in range(1, self.grid_length + 1)]))
		for i in self.grid:
			print("\n")
			count += 1
			print(i + "    " + "    ".join([chr(36) if j else chr(34) for j in self.grid[i]]))

###  for testing purpose  ###
'''	
test = BattleShip()
test.create_grid()
test.show_ships()
print("\n" * 3)
test.create_ship("cargo ship", "a:5", "left")
test.create_ship("boat", "a:3", "right")
test.show_ships()
'''
