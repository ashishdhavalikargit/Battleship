from arsenal import BattleShip
from platform import python_version
from sound_effects import playMP3

take_input = input if int(python_version()[0]) == 3 else raw_input

class Player(BattleShip):
	pass
		

def main():
	print("\n==================      welcome to battleship      ==================\n")
	# include aound
	playMP3("mp3tracks/ship_built.mp3")
	status = True
	while (status):
		value = int(take_input("\nPlease enter ocean size (3 or more):  "))
		status = value < 3
		if status:
			print("\nOCEAN IS TOO SMALL EVEN FOR FISH TO SWIM \nPLEASE DREAM BIGGER ...")

	ships = value - 2
	player1 = Player()
	cpu = Player()
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
	sound_effects.playMP3("D:/Battleship/Latest_built_06_06_2019/Battleship/mp3tracks/ship_built.mp3")	
	playMP3("mp3tracks/ship_built.mp3")

main()