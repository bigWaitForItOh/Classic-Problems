#Implementation of the Coin Change Problem using Recursion
def get_count (amount, coins):
	size = len (coins);
	if (amount == 0):
		return (1);
	elif (amount < 0 or size == 0):
		return (0);
	else:
		return (get_count (amount, coins [ : -1]) + get_count (amount - coins [-1], coins));
