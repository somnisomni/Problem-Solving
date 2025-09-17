#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

long long solution(int n, vector<int> works) {
  int worksSize = works.size();

  sort(works.begin(), works.end());

  while(n > 0) {
    int currentMax = works[worksSize - 1];

    for(int index = worksSize - 1; index >= 0; index--) {
      if(works[index] >= currentMax) {
        works[index]--;
        n--;
      }

      if(n <= 0) break;
    }
  }

  long long result = 0LL;
  for(int remainingWork : works) {
    int normalized = remainingWork < 0 ? 0 : remainingWork;

    result += normalized * normalized;
  }

  return result;
}

/* == */

int main() {
  vector<int> testcase = { 1, 1 };

  cout << solution(3, testcase) << endl;

  return 0;
}
