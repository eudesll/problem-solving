/**
 * URI
 * Problem Id : 1143
 * Problem Name: Quadrado e ao Cubo
 */

#include <iostream>
using namespace std;

int main () {

	int n;

	cin >> n;
	for (int i = 1; i <= n; i++) {
		cout << i << " ";
		cout << (i * i) << " ";
		cout << (i * i * i) << endl;
	}

	return 0;
}