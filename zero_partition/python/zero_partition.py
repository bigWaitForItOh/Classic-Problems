###########################################################################################################
#Recursive Implementation of Zero Partition Problem
#http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/
#Time Complexity: O (2^m)
#m = size of set1
###########################################################################################################

def partition (set1, size, total_sum, partial_sum):
	if (total_sum == partial_sum):
		return (True);
	if (size == 0):
		return (False);

	return (
		partition (set1, size - 1, total_sum, partial_sum) or 
		partition (set1, size - 1, total_sum - set1 [size - 1], partial_sum + set1 [size - 1])
	);

def zero_partition (set1):
	return (partition (set1, len (set1), sum (set1), 0));

if (__name__ == '__main__'):
	set1 = [int (i) for i in input ().split ()];
	print (zero_partition (set1));