#include <iostream>
#include <vector>
using namespace std;

inline const int max(const int a, const int b) { return a > b ? a : b; }

int solution(vector<vector<int>> triangle) {
  int ySize = triangle.size();

  for(int y = ySize - 2; y >= 0; y--) {
    for(int x = 0; x < triangle[y].size(); x++) {
      int value = triangle[y][x];

      triangle[y][x] = max(
        triangle[y + 1][x] + value,
        triangle[y + 1][x + 1] + value
      );
    }
  }

  return triangle[0][0];
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
