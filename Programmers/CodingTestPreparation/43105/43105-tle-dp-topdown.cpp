#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

map<pair<int, int>, int> dp;

inline const int max(const int a, const int b) { return a > b ? a : b; }

int solution(vector<vector<int>> triangle) {
  int maxValue = triangle[0][0];

  dp[make_pair(0, 0)] = triangle[0][0];

  for(int y = 1; y < triangle.size(); y++) {
    for(int x = 0; x < triangle[y].size(); x++) {
      pair<int, int> coord = make_pair(y, x);
      int value = triangle[y][x];

      int ancestMax = -1;
      if(x - 1 >= 0) ancestMax = max(ancestMax, dp[make_pair(y - 1, x - 1)]);
      ancestMax = max(ancestMax, dp[make_pair(y - 1, x)]);

      dp[coord] = ancestMax + value;
      maxValue = max(maxValue, dp[coord]);
    }
  }

  return maxValue;
}

/* == */

int main() {
  vector<vector<int>> testcase = {
    { 7 },
    { 3, 8 },
    { 8, 1, 0 },
    { 2, 7, 4, 4 },
    { 4, 5, 2, 6, 5 }
  };

  cout << solution(testcase) << endl;

  return 0;
}
