#Implementation of the Coin Change Problem using Dynamic Programming
def get_count (amount, coins):
	size = len (coins);
	table = [ [0 for i in range (size)] for x in range (amount + 1) ];

	for i in range (size): table [0] [i] = 1;
	for i in range (1, amount + 1):
		for j in range (size):
			a = table [i - coins [j]] [j] if (i - coins [j]) >= 0 else 0;
			b = table [i] [j - 1] if j >= 1 else 0;
			table [i] [j] = a + b;
	return (table [amount] [size - 1]);
				

