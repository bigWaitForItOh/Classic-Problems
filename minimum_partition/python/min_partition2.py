###########################################################################################################
#Recursive Implementation of Minimum Partition Problem
#http://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
#Time Complexity: O (2^m)
#m = size of set1
#This recursive implementation is a little different from that of min_partition.py
###########################################################################################################

def partition_aux (set1, total_sum, partial_sum, size):
	if (size == 0):
		return (abs ( (total_sum - partial_sum) - partial_sum ));
	return (min (
		partition_aux (set1, total_sum, partial_sum, size - 1),
		partition_aux (set1, total_sum, partial_sum + set1 [size - 1], size - 1)
	));

def partition (set1):
	return (partition_aux (set1, sum (set1), 0, len (set1)));

if (__name__ == '__main__'):
	set1 = [int (i) for i in input ().split ()];
	print (partition (set1));
