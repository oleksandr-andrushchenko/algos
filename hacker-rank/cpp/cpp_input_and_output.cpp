// Read  numbers from stdin and print their sum to stdout.

#include <iostream>
using namespace std;

int main() {
    int num, sum = 0;
    while (cin >> num) {
        sum += num;
    }
    cout << sum << endl;
    return 0;
}