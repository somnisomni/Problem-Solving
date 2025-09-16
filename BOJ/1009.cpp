#include <iostream>
using namespace std;

int main() {
  // a ^ b의 결과에서 일의 자리 수만 구하면 되는 문제

  int line = 0;
  cin >> line;

  for(int i = 0; i < line; i++) {
    int a = 0, b = 0;
    cin >> a >> b;

    int rem = a % 10;
    for(; b > 1; b--) {
      rem = (rem * a) % 10;
    }

    // 0이 되는 경우 핸들링 -> 10이 되어야함
    if(rem == 0) rem = 10;

    cout << rem << endl;
  }

  return 0;
}
