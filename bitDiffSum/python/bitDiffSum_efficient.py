##########################################################################################
#http://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/
#An efficient solution for problem of sum of bit differences amongst all pairs
#Time Complexity: O (N)
##########################################################################################

def countForBit (array, bit):
	bitSetCount = 0;
	mask = 1 << bit;

	for number in array:
		if (number & mask):	bitSetCount += 1;
	return (bitSetCount * (len (array)-bitSetCount) * 2);

def bitDiff (array):
	count = 0;
	for bit in range (0, 32):
		count += countForBit (array, bit);
	return (count);

if (__name__ == '__main__'):
	array = [int (i) for i in input ().split ()];
	print (bitDiff (array));