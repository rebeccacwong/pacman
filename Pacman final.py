import pygame, time
import random
pygame.init()

def create_grid(rows, columns):
	"creates a grid that contains data for the board (ex: where the fruit, ghosts, pacman maze are)"
	index = 0
	index2 = 0
	board = []
	while not index == rows:
		row = []
		while not index2 == columns:
			row.append("")
			index2 += 1
		board.append(row)
		index2 = 0
		index += 1
	return board

# global variables!
SCORE = 0
BOARD = create_grid(31, 28)
PACMAN_POSITION = [17, 14]
	# [17, 14] is the starting point
PACMAN_PREVIOUS = [17, 14]
PACMAN_DIRECTION = 'right'
	# starts out right and then should change
GHOST1 = [[12, 13], 'up', [12, 13]] 
GHOST2 = [[12, 14], 'up', [12, 14]]
GHOST3 = [[14, 13], 'up', [14, 13]]
GHOST4 = [[14, 14], 'up', [14, 14]]
# ghost = [ghost current position, ghost direction, ghost previous position]
GHOSTS = [GHOST1, GHOST2, GHOST3, GHOST4]


# KEY
# P = pacman
# o = fruit
# X = wall
# G = ghost
# Go = ghost, but there is a pellet behind it (this is so we can replace the pellet after ghost leaves)

def add_maze():
	"adds maze and ghosts to the grid of data"
	BOARD[0] = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
	BOARD[1] = ['X', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'X', 'X', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'X']
	BOARD[2] = ['X', 'o', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'o', 'X']
	BOARD[3] = ['X', 'o', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'o', 'X']
	BOARD[4] = ['X', 'o', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'o', 'X']
	BOARD[5] = ['X', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'X']
	BOARD[6] = ['X', 'o', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'o', 'X']
	BOARD[7] = ['X', 'o', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'o', 'X']
	BOARD[8] = ['X', 'o', 'o', 'o', 'o', 'o', 'o', 'X', 'X', 'o', 'o', 'o', 'o', 'X', 'X', 'o', 'o', 'o', 'o', 'X', 'X', 'o', 'o', 'o', 'o', 'o', 'o', 'X']
	BOARD[9] = ['X', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'X']
	BOARD[10] = [' ' ,' ' ,' ' , ' ' ,' ' , 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', ' ' ,' ' ,' ' , ' ' ,' ' ]
	BOARD[11] = [' ' ,' ' ,' ' , ' ' ,' ' , 'X', 'o', 'X', 'X', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'X', 'X', 'o', 'X', ' ' ,' ' ,' ' , ' ' ,' ' ]
	BOARD[12] = [' ' ,' ' ,' ' , ' ' ,' ' , 'X', 'o', 'X', 'X', 'o', 'o', 'o', 'X', 'G', 'G', 'X', 'o', 'o', 'o', 'X', 'X', 'o', 'X', ' ' ,' ' ,' ' , ' ' ,' ' ]
	BOARD[13] = ['X', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'o', 'o', 'X', ' ', ' ', 'X', 'o', 'o', 'o', 'X', 'X', 'o', 'X', 'X' ,'X' ,'X' , 'X' ,'X' ]
	BOARD[14] = ['X', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'X', 'G', 'G', 'X', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'X']
	BOARD[15] = ['X', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'o', 'o', 'X', 'X', 'X' , 'X', 'o', 'o', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'X']
	BOARD[16] = [' ' ,' ' ,' ' , ' ' ,' ' , 'X', 'o', 'X', 'X', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'X', 'X', 'o', 'X', ' ' ,' ' ,' ' , ' ' , ' ']
	BOARD[17] = [' ' ,' ' ,' ' , ' ' ,' ' , 'X', 'o', 'X', 'X', 'o', 'o', 'o', 'o', 'o', 'P', 'o', 'o', 'o', 'o', 'X', 'X', 'o', 'X', ' ' ,' ' ,' ' , ' ' , ' ']
	BOARD[18] = [' ' ,' ' ,' ' , ' ' ,' ' , 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', ' ' ,' ' ,' ' , ' ' , ' ']
	BOARD[19] = ['X', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'X']
	BOARD[20] = ['X', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'X', 'X', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'X']
	BOARD[21] = ['X', 'o', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'o', 'X']
	BOARD[22] = ['X', 'o', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'o', 'X']
	BOARD[23] = ['X', 'o', 'o', 'o', 'X', 'X', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'X', 'X', 'o', 'o', 'o', 'X']
	BOARD[24] = ['X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X']
	BOARD[25] = ['X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X']
	BOARD[26] = ['X', 'o', 'o', 'o', 'o', 'o', 'o', 'X', 'X', 'o', 'o', 'o', 'o', 'X', 'X', 'o', 'o', 'o', 'o', 'X', 'X', 'o', 'o', 'o', 'o', 'o', 'o', 'X']
	BOARD[27] = ['X', 'o', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'o', 'X']
	BOARD[28] = ['X', 'o', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'o', 'X', 'X', 'o', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'o', 'X']
	BOARD[29] = ['X', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'X']
	BOARD[30] = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']

def new_new_ghost_position(ghost_row, ghost_column, ghost_number):
	"generates the coordinates of where the ghost should move to. will make the ghost continue moving in one direction until it hits a wall. when it hits a wall, it will choose a random direction to go in"
	global GHOST1
	global GHOST2
	global GHOST3
	global GHOST4
	if ghost_number == GHOST1:
		ghost_direction = GHOST1[1]
		ghost_index = 0
	if ghost_number == GHOST2:
		ghost_direction = GHOST2[1]
		ghost_index = 1
	if ghost_number == GHOST3:
		ghost_direction = GHOST3[1]
		ghost_index = 2
	if ghost_number == GHOST4:
		ghost_direction = GHOST4[1]
		ghost_index = 3
	ghost_directions = ['right', 'left', 'up', 'down']
	while True:
		if ghost_direction == 'down':
			if BOARD[ghost_row + 1][ghost_column] != 'X' and BOARD[ghost_row + 1][ghost_column] != 'G' and BOARD[ghost_row + 2][ghost_column] != 'G':
				return [ghost_row + 1, ghost_column]
			else:
				ghost_direction = ghost_directions[random.randint(0, 2)]
				GHOSTS[ghost_index][1] = ghost_direction
		if ghost_direction == 'left':
			if BOARD[ghost_row][ghost_column - 1] != 'X' and BOARD[ghost_row][ghost_column - 1] != 'G' and BOARD[ghost_row][ghost_column - 2] != 'G':
				return [ghost_row, ghost_column - 1]
			else:
				ghost_direction = ghost_directions[random.randint(0, 3)]
				GHOSTS[ghost_index][1] = ghost_direction
		if ghost_direction == 'right':
			if BOARD[ghost_row][ghost_column + 1] != 'X' and BOARD [ghost_row][ghost_column + 1] != 'G' and BOARD[ghost_row][ghost_column + 2] != 'G':
				return [ghost_row, ghost_column + 1]
			else: 
				ghost_direction = ghost_directions[random.randint(1, 3)]
				GHOSTS[ghost_index][1] = ghost_direction
		if ghost_direction == 'up':
			if BOARD[ghost_row - 1][ghost_column] != 'X' and BOARD[ghost_row - 1][ghost_column] != 'G' and BOARD[ghost_row - 2][ghost_column] != 'G':
				return [ghost_row - 1, ghost_column]
			else: 
				ghost_direction = ghost_directions[random.randint(0, 3)]
				GHOSTS[ghost_index][1] = ghost_direction
		if ghost_number == GHOST1:
			GHOST1[1] = ghost_direction
		if ghost_number == GHOST2:
			GHOST2[1] = ghost_direction
		if ghost_number == GHOST3:
			GHOST3[1] = ghost_direction
		if ghost_number == GHOST4:
			GHOST4[1] = ghost_direction

def ghost_movement(ghost_number):
	"takes in a global variable of the ghost's location (GHOST1, GHOST2, GHOST3, GHOST4) and modifies the board to move the ghost using the randomizer block new_ghost_position"
	# new_ghost_position(ghost_row, ghost_column) will report coordinates that the ghost should move to
	global GHOST1
	global GHOST2
	global GHOST3
	global GHOST4
	move_to = new_new_ghost_position(ghost_number[0][0], ghost_number[0][1], ghost_number)
	if BOARD[move_to[0]][move_to[1]] == 'o' or BOARD[move_to[0]][move_to[1]] == 'Go':
		BOARD[move_to[0]][move_to[1]] = 'Go'
		if BOARD[ghost_number[0][0]][ghost_number[0][1]] == 'Go':
			BOARD[ghost_number[0][0]][ghost_number[0][1]] = 'o'
		if BOARD[ghost_number[0][0]][ghost_number[0][1]] == 'G':
			BOARD[ghost_number[0][0]][ghost_number[0][1]] = ' '
	if BOARD[move_to[0]][move_to[1]] == ' ' or BOARD[move_to[0]][move_to[1]] == 'G':
		BOARD[move_to[0]][move_to[1]] = 'G'
		if BOARD[ghost_number[0][0]][ghost_number[0][1]] == 'Go':
			BOARD[ghost_number[0][0]][ghost_number[0][1]] = 'o'
		if BOARD[ghost_number[0][0]][ghost_number[0][1]] == 'G':
			BOARD[ghost_number[0][0]][ghost_number[0][1]] = ' '
	if ghost_number == GHOST1:
		GHOST1[2] = ghost_number[0][0], ghost_number[0][1]
		GHOST1[0] = [move_to[0],move_to[1]]
	if ghost_number == GHOST2:
		GHOST2[2] = ghost_number[0][0], ghost_number[0][1]
		GHOST2[0] = [move_to[0],move_to[1]]
	if ghost_number == GHOST3:
		GHOST3[2] = ghost_number[0][0], ghost_number[0][1]
		GHOST3[0] = [move_to[0],move_to[1]]
	if ghost_number == GHOST4:
		GHOST4[2] = ghost_number[0][0], ghost_number[0][1]
		GHOST4[0] = [move_to[0],move_to[1]]

def game_over():
	if PACMAN_POSITION == GHOST1[0] or PACMAN_POSITION == GHOST2[0] or PACMAN_POSITION == GHOST3[0] or PACMAN_POSITION == GHOST4[0]:
		return True
		# true means game over
	if PACMAN_PREVIOUS == GHOST1[0] or PACMAN_PREVIOUS == GHOST2[0] or PACMAN_PREVIOUS == GHOST3[0] or PACMAN_PREVIOUS == GHOST4[0]:
		# if pacman and ghost switch postions, game is over (they crossed each other)
		return True
	if GHOST1[2] == PACMAN_POSITION or GHOST2[2] == PACMAN_POSITION or GHOST3[2] == PACMAN_POSITION or GHOST4[2] == PACMAN_POSITION:
		return True
	return False

def pacman_movement(pacman_position):
	"keeps moving pacman forward depending on the direction he is facing in"
	global PACMAN_DIRECTION
	global SCORE
	global PACMAN_POSITION
	global PACMAN_PREVIOUS
	if PACMAN_DIRECTION == 'right':
		if BOARD[pacman_position[0]][pacman_position[1] + 1] != 'X':
			if BOARD[pacman_position[0]][pacman_position[1] + 1] == 'o':
				SCORE += 10
			BOARD[pacman_position[0]][pacman_position[1] + 1] = 'P'
			BOARD[pacman_position[0]][pacman_position[1]] = ' '
			PACMAN_POSITION = [pacman_position[0], pacman_position[1] + 1]
	if PACMAN_DIRECTION == 'left':
		if BOARD[pacman_position[0]][pacman_position[1] - 1] != 'X':
			if BOARD[pacman_position[0]][pacman_position[1] - 1] == 'o':
				SCORE += 10
			BOARD[pacman_position[0]][pacman_position[1] - 1] = 'P'
			BOARD[pacman_position[0]][pacman_position[1]] = ' '
			PACMAN_POSITION = [pacman_position[0], pacman_position[1] - 1]
	if PACMAN_DIRECTION == 'up':
		if BOARD [pacman_position[0] - 1][pacman_position[1]] != 'X':
			if BOARD[pacman_position[0] - 1][pacman_position[1]] == 'o':
				SCORE += 10
			BOARD[pacman_position[0] - 1][pacman_position[1]] = 'P'
			BOARD[pacman_position[0]][pacman_position[1]] = ' '
			PACMAN_POSITION = [pacman_position[0] - 1, pacman_position[1]]
	if PACMAN_DIRECTION == 'down':
		if BOARD [pacman_position[0] + 1][pacman_position[1]] != 'X':
			if BOARD[pacman_position[0] + 1][pacman_position[1]] == 'o':
				SCORE += 10
			BOARD[pacman_position[0] + 1][pacman_position[1]] = 'P'
			BOARD[pacman_position[0]][pacman_position[1]] = ' '
			PACMAN_POSITION = [pacman_position[0] + 1, pacman_position[1]]
	PACMAN_PREVIOUS = [pacman_position[0], pacman_position[1]]

def print_board():
	for row in range(0, 31):
		result = ''
		for column in range(0, 28):
			if BOARD[row][column] == 'Go':
				result = result + ' ' + 'G'
			else:
				result = result + ' ' + BOARD[row][column]
		print(result)


# GAME CODE
add_maze()
print_board()
	# keeps looping so pacman and the ghosts will be constantly moving
while not game_over():
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT and BOARD[PACMAN_POSITION[0]][PACMAN_POSITION[1] + 1] != 'X':
				# checks to make sure that the spot to the right isn't a wall, if it is, it will not change direction of pacman (keep going in the direction it was already set in)
				PACMAN_DIRECTION = 'right'
			if event.key == pygame.K_UP and BOARD[PACMAN_POSITION[0] - 1][PACMAN_POSITION[1]] != 'X':
				PACMAN_DIRECTION = 'up'
			if event.key == pygame.K_LEFT and BOARD[PACMAN_POSITION[0]][PACMAN_POSITION[1] - 1] != 'X':
				PACMAN_DIRECTION = 'left'
			if event.key == pygame.K_DOWN and BOARD [PACMAN_POSITION[0] + 1][PACMAN_POSITION[1]] != 'X':
				PACMAN_DIRECTION = 'down'
	pacman_movement(PACMAN_POSITION)
	ghost_movement(GHOST1)
	ghost_movement(GHOST2)
	ghost_movement(GHOST3)
	ghost_movement(GHOST4)
	time.sleep(.75)
	print('TOTAL SCORE = ' + str(SCORE))
	print_board()
	print(' ')
print('GAME OVER')
print('TOTAL SCORE = ' + str(SCORE))

pygame.quit()


