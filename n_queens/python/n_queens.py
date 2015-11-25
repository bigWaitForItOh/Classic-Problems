###############################################################################################################################
#Solves the N Queens Problem using Backtracking & Recursion
#Input: Number N
#Output: a List of N Lists, representing an NxN grid. 0 represents no queen at that spot, 1 otherwise.
###############################################################################################################################

def make_board (n):
	return ([ [0]*n for j in range (n) ]);

def valid_state (board, row, col):
	if (1 in board [row]):
		return (False);

	positions = [];
	for r in range (len (board)):
		try:
			c = board [r].index (1);
			positions.append ( (r, c) );
		except Exception as e:
			pass;

	for pos in positions:
		if (abs (pos [0] - row) == abs (pos [1] - col)):
			return (False);
		
	return (True);

def n_queens (n, row, col, board):
	if (not n):
		return (True);

	for curr_row in range (len (board)):
		if (valid_state (board, curr_row, col)):
			board [curr_row] [col] = 1;
			if (n_queens (n - 1, row, col + 1, board)):
				return (True);
			else:
				board [curr_row] [col] = 0;
	return (False);

if (__name__ == '__main__'):
	n = int (input ());
	board = make_board (n);		#Create Grid to fill Queen Positions

	n_queens (n, 0, 0, board);	#Sample Call to n_queens (). NOTE: the 0, 0 is the position the algorithm starts at.
	for row in board: print (row);
