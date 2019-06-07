from arsenal import BattleShip
from platform import python_version
from sound_effects import playMP3

take_input = input if int(python_version()[0]) == 3 else raw_input

class Player(BattleShip):
	def __init__(self):
		super(Player, self).__init__()
		self.attaks_history = {}
		self.name = "player"
		self.opponent = None
		self.status = "start"

	def get_attack_history(self):
		return self.attaks_history

	def do_attack(self):
		location =  str(take_input("\nEnter attack point Ex.[B:2] :  "))
		try:
			position, value = location.strip().upper().split(':')
			if (position not in self.opponent.grid) or (int(value) not in range(1, (self.opponent.grid_width + 1))):
				raise ValueError
			self.status, value = self.opponent.attack(location)
			self.attaks_history.update({location: self.status})
		except Exception as e:
			self.status = "on hold"
			print("\nPlease Enter a valid input ...")
    	
		
player1 = Player()
cpu = Player()
player1.opponent = cpu
cpu.name = "computer"

def main():
	print("\n==================      welcome to battleship      ==================\n")
	playMP3("mp3tracks/ship_built.mp3")
	name = str(take_input("\nENTER YOUR NAME :  "))
	player1.name = name
	status = True
	while (status):
		value = int(take_input("\nPlease enter ocean size (3 or more):  "))
		status = value < 3
		if status:
			print("\nOCEAN IS TOO SMALL EVEN FOR FISH TO SWIM \nPLEASE DREAM BIGGER ...")

	ships = value - 2
	player1.create_grid(value,value)
	cpu.create_grid(value,value)
	status = True
	count = ships
	print("\n ~ ~ ~ ~ Here is your wonderful ocean ~ ~ ~ ~ \n")
	player1.show_ships()
	while count:
		ship_type = str(take_input("\nEnter ship type cargo-ship/submarine :  "))
		start =  str(take_input("\nEnter ship initial point Ex.[A:3] :  "))
		direction = str(take_input("\nEnter direction  right/left/up/down:  "))
		status, msg = player1.create_ship(ship_type, start, direction)
		if status:
			count -= 1
		print(msg)
	player1.show_ships()
	cpu.create_random_ships(ships)
	playMP3("mp3tracks/ship_built.mp3")	


def start():
	computer_attacks = list()
	status = "start"
	value = False
	player  = player1
	while status != "GAME OVER":
		if player == player1:
			player1.do_attack()
			status = player1.status
			print("\n======= your attaks history =======\n")
			print(player1.attaks_history)
			player1.show_ships()
		else:
			status, value = player1.hit_random()
			computer_attacks.append(value)
			print("computer attacked on : ", computer_attacks)
		print("\nCURRENT STATUS of {}  ==== > ".format(player.name) + status)
		if status == "miss":
			value = (not value)
			player = (player1, cpu)[value]


main()
start()
