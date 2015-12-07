##################################################################################################################
#Fractional Knapsack Greedy Algorithm
#Time Complexity: O(nlog(n))
#Yields the optimal value that can be retrieved, needs to be modified to include weight-item information
##################################################################################################################

from heapq import heapify, heappush, heappop;

#items is a list of 2-tuples of the form (weight_of_item, value_of_item)
def fractional_knap (items, knap_size):
	reward, p_queue = 0, [ (-(i [1] / i [0]), i [0], i [1]) for i in items ];
	heapify (p_queue);

	while (knap_size):
		vpw, weight, value = heappop (p_queue);
		if (knap_size >= weight):
			knap_size -= weight;
			reward += value;
		else:
			reward += (knap_size / weight) * value;
			knap_size = 0;
	return (reward);

if (__name__ == '__main__'):
	size = int (input ('Enter knapsack Size: '));
	num = int (input ('Number of items: '));
	print ('Enter items below in format (1 item on each line: <weight> <value> <ENTER>');
	items = [ [int (i) for i in input ().split ()] for j in range (num) ];
	print (fractional_knap (items, size));
