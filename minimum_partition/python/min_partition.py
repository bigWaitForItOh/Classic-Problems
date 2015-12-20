###########################################################################################################
#Recursive Implementation of Minimum Partition Problem
#http://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
#Time Complexity: O (2^m)
#m = size of set1
###########################################################################################################

def partition_aux (set1, sum1, sum2, size):
	if (size == 0):
		return (abs (sum1 - sum2));

	x = abs (sum1 - sum2);
	y = partition_aux (set1, sum1 - set1 [size - 1], sum2 + set1 [size - 1], size - 1);
	z = partition_aux (set1, sum1, sum2, size - 1);
	return (min (x, y, z));

def partition (set1):
	return (partition_aux (set1, sum (set1), 0, len (set1)));

if (__name__ == '__main__'):
	set1 = [int (i) for i in input ().split ()];
	print (partition (set1));