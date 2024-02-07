
def print_board(b):
	for r in b:
		for e in r:
			if e == 0:
				print('_', end=' ')
			elif e == 1:
				print('X', end=' ')
			elif e == 2:
				print('O', end=' ')
		print()

def has_player_won(b, player):
	return (b[0][0] == player and b[0][1] == player and b[0][2] == player) or (b[1][0] 
		== player and b[1][1] == player and b[1][2] == player) or (b[2][0] == 
		player and b[2][1] == player and b[2][2] == player) or (b[0][0] == 
		player and b[1][0] == player and b[2][0] == player) or (b[0][1] == 
		player and b[1][1] == player and b[2][1] == player) or (b[0][2] == 
		player and b[1][2] == player and b[2][2] == player) or (b[0][0] == 
		player and b[1][1] == player and b[2][2] == player) or (b[0][2] == 
		player and b[1][1] == player and b[2][0] == player)


		




the_board = [[0,2,2], [0,1,0], [0,1,0]]
print_board(the_board)
print(has_player_won(the_board, 2))
the_board = [[0,2,2], [0,1,0], [0,1,0]]