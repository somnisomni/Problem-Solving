// 프로그래머스 "정수 삼각형" (43105) 문제와 동일

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
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

int main() {
  int n;
  cin >> n;
  cin.ignore();

  vector<vector<int>> triangle;

  // 파이썬이 그리운 string split 코드
  // triangle[i] = list(map(int, input().split(" ")))
  for(int i = 0; i < n; i++) {
    string line;
    getline(cin, line);

    triangle.push_back(vector<int>());

    istringstream lineStream(line);
    string buf;
    while(getline(lineStream, buf, ' ')) {
      triangle[i].push_back(stoi(buf));
    }
  }

  cout << solution(triangle) << endl;

  return 0;
}
