#######################################################################################################################
# Recursive Implementation of Optimal Game Strategy
# Game is described at: http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/
#######################################################################################################################

def max_benefit (coins):
	if (len (coins) == 1):
		return (coins [0]);
	if (len (coins) == 2):
		return (max (coins));

	return (max (
		coins [0] + min (max_benefit (coins [2 : ]), max_benefit (coins [ : -1])),
		coins [-1] + min (max_benefit (coins [1 : ]), max_benefit (coins [ : -2]))
	));

coins = [int (i) for i in input ().split ()];
print (max_benefit (coins));