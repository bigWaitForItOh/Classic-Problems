#########################################################################################################################################
#Script to return the nim sum of a list of numbers. nim sum has application in the Nim Game and other Game Theory related algorithms.
#########################################################################################################################################

def nim_sum (array):
	max_len, base_2 = len (bin (max (array))) - 2, [bin (i) [2 : ] for i in array];
	result = '0' * max_len;

	for i in range (len (base_2)):
		if (len (base_2 [i]) < max_len): base_2 [i] = ('0' * (max_len - len (base_2 [i]))) + base_2 [i];
		for j in range (max_len):
			result = result [ : j] + str ( (int (result [j]) + int (base_2 [i] [j])) % 2 ) + result [j + 1 : ];
	return (int ('0b' + result, 2));
	

print (nim_sum ([int (i) for i in input ().split ()]));
