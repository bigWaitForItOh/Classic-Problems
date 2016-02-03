################################################################################################
#Recursive Implementation of K Coin Path Problem
#URI: http://www.geeksforgeeks.org/number-of-paths-with-exactly-k-coins/
#Time Complexity: O (2^N)
#Space Complexity: 
################################################################################################

def kCoinPaths (size, N, matrix, i, j):
	size -= matrix [i] [j];
	if (size < 0):
		return (0);
	if (size == 0):
		return (i == N-1 and j == N-1);

	right = kCoinPaths (size, N, matrix, i, j+1) if j+1 < N else 0;
	down = kCoinPaths (size, N, matrix, i+1, j) if i+1 < N else 0;
	return (right + down);

if (__name__ == '__main__'):
	size = int (input ());
	N = int (input ());
	#matrix = [ [int (i) for i in input ().split ()] for j in range (N) ];
	matrix = [ [1,2,3],[4,6,5],[3,2,1] ];

	print (kCoinPaths (size, N, matrix, 0, 0));