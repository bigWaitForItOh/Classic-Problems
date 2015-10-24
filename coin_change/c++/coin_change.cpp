#include <bits/stdc++.h>
using namespace std;

int coin_change (int amount, vector< int >& coins) {
	if (amount == 0) { return (1); }
	else if (amount < 0 || coins.size () == 0) { return (0); }

	vector< int > replica (coins.begin (), coins.end () - 1);
	return (coin_change (amount - coins [coins.size () - 1], coins) + coin_change (amount, replica));
}
int main () {
	int size, amount;

	cout << "Enter size: ";
	cin >> size;
	cout << "Enter amount: ";
	cin >> amount;
	vector< int > coins (size);

	for (int i = 0; i < size; i++) {
		cin >> coins [i];
	}
	cout << coin_change (amount, coins) << endl;
	return (0);
}
