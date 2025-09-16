#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  // numerator / denominator
  int numerator = 1;
  int denominator = 1;

  // true: num++ denom--, false: num-- denom++
  bool direction = false;

  int step = 0;
  cin >> step;

  while(step > 1) {
    if(direction) {
      numerator++;
      denominator--;
    } else {
      numerator--;
      denominator++;
    }

    if(numerator <= 0) {
      numerator = 1;
      direction = !direction;
    } else if(denominator <= 0) {
      denominator = 1;
      direction = !direction;
    }

    step--;
  }

  cout << numerator << "/" << denominator;

  return 0;
}
