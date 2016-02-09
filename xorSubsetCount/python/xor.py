#################################################################################################################
#Number of subsets of a set of numbers having a particular XOR value
#Recursive Implementation
#Time Complexity: O (2^N)
#URI: http://www.geeksforgeeks.org/count-number-of-subsets-having-a-particular-xor-value/
#################################################################################################################

def xorSubsetCount (array, target, xorValue, size):
	localResult = 0;

	if (size < 1):
		return (0);
	if (xorValue ^ array [size-1] == target):
		localResult = 1;

	return (
		localResult + 
		xorSubsetCount (array, target, xorValue ^ array [size-1], size - 1) + 
		xorSubsetCount (array, target, xorValue, size - 1)
	);

if (__name__ == '__main__'):
	array = [int (i) for i in input ().split ()];
	target = int (input ());
	print (xorSubsetCount (array, target, 0, len (array)));