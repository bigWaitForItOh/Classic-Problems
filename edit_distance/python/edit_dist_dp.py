###########################################################################################################################
#Dynamic Programming implementation of Edit Distance Algorithm
#Complexity:
#	Time: O (mn)
#	Space: O (mn)
#m = length of string1, n = length of string2
###########################################################################################################################

def init_matrix (x, y):
	matrix = [ [None for i in range (len (x) + 1)] for j in range (len (y) + 1)];
	for i in range (len (matrix [0])):
		matrix [0] [i] = i;
		try:
			matrix [i] [0] = i;
		except:
			pass;

	return (matrix);

def edit_dist (x, y):
	matrix = init_matrix (x, y);
	for i in range (1, len (x)+1):
		for j in range (1, len (y)+1):
			if (x [i-1] == y [j-1]):
				matrix [j] [i] = matrix [j - 1] [i - 1];
			else:
				matrix [j] [i] = min (matrix [j - 1] [i], matrix [j] [i - 1], matrix [j - 1] [i - 1]) + 1;

	return (matrix [-1] [-1]);

distance = edit_dist (input (), input ());
print (distance);
