from arsenal import BattleShip

class Player(BattleShip):
	pass
		

def main():
	print("\n==================      welcome to battleship      ==================\n")
	# include aound
	status = True
	while (status):
		value = int(input("\nPlease enter ocean size (3 or more):  "))
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
		ship_type = str(input("\nEnter ship type cargo-ship/submarine :  "))
		start =  str(input("\nEnter ship initial point Ex.[A:3] :  "))
		direction = str(input("\nEnter direction  right/left/up/down:  "))
		status, msg = player1.create_ship(ship_type, start, direction)
		if status:
			count -= 1
		print(msg)
	player1.show_ships()
	cpu.create_random_ships(ships)
	# include sound

main()