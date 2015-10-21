#maximum subarray Problem: Kadane's Algorithm
def max_subarray (array):
	#bsf: best so far
	bsf = current = pos_current = 0;

	while (pos_current < len (array)):
		current += array [pos_current];

		if (current < 0):
			current = 0;
		if (bsf < current):
			bsf = current;

		pos_current += 1;

	return (bsf);

#SAMPLE CALL
print (max_subarray ([int (i) for i in input ().split ()]));
