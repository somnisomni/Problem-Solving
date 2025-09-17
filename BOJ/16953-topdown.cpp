// 그리디, 탑다운 구현

#include <iostream>
using namespace std;

#define max(a, b) a > b ? a : b;

int maxDepth = 0;

bool dig(int target, long long currentValue, int depth = 1) {
  // cout << currentValue << " ";
  if(currentValue == target) {
    maxDepth = max(maxDepth, depth);
    // cout << "O (maxdepth: " << maxDepth << ") ";

    return true;
  } else if(currentValue > target) {
    // cout << "X" << " ";
    return false;
  }

  bool doubling = dig(target, currentValue * 2, depth + 1);
  bool appending = dig(target, currentValue * 10 + 1, depth + 1);

  return doubling || appending;
}

int main() {
  int start, target;
  cin >> start >> target;

  if(dig(target, start)) {
    cout << maxDepth << endl;
  } else {
    cout << -1 << endl;
  }

  return 0;
}
