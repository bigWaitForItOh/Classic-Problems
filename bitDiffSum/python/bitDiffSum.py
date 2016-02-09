##########################################################################################
#http://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/
#A naive solution for problem of sum of bit differences amongst all pairs
#Time Complexity: O (N^2)
##########################################################################################

from itertools import combinations as comb;

def bitDiffCount (x, y):
	print (x, y);
	count, mask = 0, 1;
	for i in range (32):
		if (not ( (x & mask) == (y & mask))):
			count += 1;
		x = x >> 1;
		y = y >> 1;
	return (count*2);

def bitDiff (array):
	count = 0;
	for pair in comb (array, 2):
		count += bitDiffCount (pair [0], pair [1]);
	return (count);

if (__name__ == '__main__'):
	array = [int (i) for i in input ().split ()];
	print (bitDiff (array));