############################################################################################################################
#Dynamic Programming Implementation of the Apple Table Problem
#
#A table composed of N x M cells, each having a certain quantity of apples, is given. You start from the upper-left corner. 
#At each step you can go down or right one cell. Find the maximum number of apples you can collect.
#
#https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/
#Under 'Intermediate'
#Time Complexity: O (NM)
############################################################################################################################

def maxApples (table):
	auxTable = [ [None for j in range (len (table [0]))] for i in range (len (table))];
	auxTable [0] [0] = table [0] [0];

	for i in range (1, len (table [0])):
		auxTable [0] [i] = auxTable [0] [i - 1] + table [0] [i];
	for i in range (1, len (table)):
		auxTable [i] [0] = auxTable [i - 1] [0] + table [i] [0];

	for i in range (1, len (table)):
		for j in range (1, len (table [0])):
			auxTable [i] [j] = table [i] [j] + max (auxTable [i - 1] [j], auxTable [i] [j - 1], auxTable [i - 1] [j - 1]);

	return (auxTable [-1] [-1]);

if (__name__ == '__main__'):
	rows, cols = [int (i) for i in input ().split ()];
	table = [ [int (i) for i in input ().split ()] for j in range (rows) ];

	print (maxApples (table));