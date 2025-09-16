#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
  string s;
  cin >> s;

  string srev = s;
  reverse(srev.begin(), srev.end());

  cout << (s == srev ? 1 : 0);

  return 0;
}
