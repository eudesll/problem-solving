/* 
   CodeChef
   Problem Name: FCTRL2
*/

#include <iostream>
using namespace std;

int main() {

	int t;

    cin >> t;
    while (t--) {

        int a[200], i = 0, n, m = 0, flag;

        cin >> n;
        flag = n; 

        while(flag != 0)  {
            a[i] = flag % 10;
            flag = flag / 10;
            i++;
            m++;
        } 

		int temp, x = 0, index = 0;
		for (i = 2; i < n; i++)  {
			temp = 0;

			for (index = 0; index < m; index++) {
				x = a[index] * i + temp;
				a[index] = x % 10;
				temp = x / 10;
			}

			while (temp != 0) {
				a[index] = temp % 10;
				temp = temp / 10;
				index++;
				m++;
			}
        }

        for(i = m - 1; i >= 0; i--) {
        	cout << a[i];
        }

        cout << endl;
    }

    return 0;
}