##################################################################################################################
#Greedy Implementation of Job Sequencing Problem
#Time Complexity: O (N.log (N))
##################################################################################################################

from heapq import heapify, heappush, heappop;
def job_sequence (jobs):
	p_queue = [ (-jobs [i] [0], jobs [i] [1], i) for i in jobs ];
	heapify (p_queue);

	top = heappop (p_queue);
	sequence, subtraction_count, profit = [top [2]], -1, -top [0];

	while (p_queue):
		datum = heappop (p_queue);
		if (datum [1] + subtraction_count > 0):
			sequence.append (datum [2]);
			profit -= datum [0];
			subtraction_count -= 1;

	return (sequence, profit);
		

#Sample Argument : A Dictionary where Key => Job Name / ID, Value => a 2-tuple (profit, deadline)
jobs = {
	'A' : (20, 4),
	'B' : (10, 1),
	'C' : (40, 1),
	'D' : (30, 1)
};

#sample call to job_sequence () : Returns a 2-Tuple (sequence of jobs to be executed, total profit obtained)
sequence, net_profit = job_sequence (jobs);
print (sequence, net_profit);
