from arsenal import BattleShip
from platform import python_version
from sound_effects import playMP3
from re import findall

take_input = input if int(python_version()[0]) == 3 else raw_input

class Player(BattleShip):
	def __init__(self):
		super(Player, self).__init__()
		self.attaks_history = {}
		self.name = "player"
		self.opponent = None
		self.status = "start"
		self.varify_regex = "[a-z|A-Z|:\\d+]"
	
	def get_attack_history(self):
		return self.attaks_history

	def do_attack(self):
		location =  str(take_input("\nEnter attack point Ex.[B:2] :  "))
		try:
			position, value = location.strip().upper().split(':')
			if (position not in self.opponent.grid) or (int(value) not in range(self.opponent.grid_width)):
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
	playMP3("mp3tracks/Intro.mp3")
	rules = str(take_input("DO WANT TO KNOW THE RULES OF THE GAME PLEASE ENTER (YES/NO): "))
	if rules.upper() == "YES":
		with open("Rulebook.txt") as rules:
			print(rules.read())
	name = str(take_input("\nENTER YOUR NAME :  "))
	player1.name = name
	status = True
	while (status):
		value = str(take_input("\nPlease enter ocean size (3 or more):  "))
		if not value.isdigit():
			print("PLAESE ENTER A VALID NUMBER ...")
			continue
		value = int(value)
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
		if ship_type.strip().lower() not in player1.ship_type:
			print("ENTER CORRECT SHIP ....")
			continue
		start =  str(take_input("\nEnter ship initial point Ex.[A:3] :  "))
		if len(findall(player1.varify_regex, start)) != 3:
			print("PLAESE ENTER IN PROPER FORMAT ...")
			continue
		direction = str(take_input("\nEnter direction  right/left/up/down:  "))
		if direction.strip().lower() not in player1.direction:
			print("ENTER DIRECTIONS PROPERLY ...")
			continue
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
			playMP3("mp3tracks/miss.mp3")
		else:
			playMP3("mp3tracks/Hit.mp3")
	print("Congratulations " + player.name + " You Won ...!!!")
	playMP3("mp3tracks/gameover.mp3")


main()
start()
