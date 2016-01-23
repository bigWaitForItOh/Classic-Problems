############################################################################################################################
#Recursive Implementation of the Apple Table Problem
#
#A table composed of N x M cells, each having a certain quantity of apples, is given. You start from the upper-left corner. 
#At each step you can go down or right one cell. Find the maximum number of apples you can collect.
#
#https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/
#Under 'Intermediate'
#Time Complexity: O (2^N)
############################################################################################################################

def maxApples (table, row, col):
	if ( (row == len (table) - 1) and (col == len (table [0]) - 1) ):
		return (table [row] [col]);
	if (row == len (table) - 1):
		return (table [row] [col] + maxApples (table, row, col+1));
	if (col == len (table [0]) - 1):
		return (table [row] [col] + maxApples (table, row+1, col));

	return (table [row] [col] + max (
		maxApples (table, row+1, col),
		maxApples (table, row, col+1)
	));

if (__name__ == '__main__'):
	rows, cols = [int (i) for i in input ().split ()];
	table = [ [int (i) for i in input ().split ()] for j in range (rows) ];

	print (maxApples (table, 0, 0));
