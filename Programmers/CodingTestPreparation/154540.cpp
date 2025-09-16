#include <string>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;

#define ctoi(c) c - '0';

map<pair<int, int>, bool> visited;
queue<pair<int, int>> bfs;

int islandBfs(vector<string> maps, int x, int y) {
    char coordChar = maps[y][x];
    pair<int, int> coord = make_pair(y, x);
    const int xLength = maps[0].length();
    const int yLength = maps.size();
    int result = 0;

    bfs.push(coord);

    while(!bfs.empty()) {
        pair<int, int> bfsCoord = bfs.front();
        bfs.pop();

        if(visited[bfsCoord]) continue;
        visited[bfsCoord] = true;

        char bfsChar = maps[bfsCoord.first][bfsCoord.second];
        if(bfsChar == 'X') continue;

        result += ctoi(bfsChar);

        if(bfsCoord.first + 1 < yLength) bfs.push(make_pair(bfsCoord.first + 1, bfsCoord.second));
        if(bfsCoord.first - 1 >= 0) bfs.push(make_pair(bfsCoord.first - 1, bfsCoord.second));
        if(bfsCoord.second + 1 < xLength) bfs.push(make_pair(bfsCoord.first, bfsCoord.second + 1));
        if(bfsCoord.second - 1 >= 0) bfs.push(make_pair(bfsCoord.first, bfsCoord.second - 1));
    }

    return result;
}

vector<int> solution(vector<string> maps) {
    vector<int> result;

    for(int y = 0; y < maps.size(); y++) {
        string yLine = maps[y];

        for(int x = 0; x < yLine.length(); x++) {
            int bfsResult = islandBfs(maps, x, y);

            if(bfsResult > 0) result.push_back(bfsResult);
        }
    }

    if(result.size() <= 0) result.push_back(-1);

    sort(result.begin(), result.end());

    return result;
}

int main() {
  vector<string> testcase = {
    "X591X",
    "X1X5X",
    "X231X",
    "1XXX1"
  };

  vector<int> result = solution(testcase);
  for(int x : result) cout << x << " ";

  return 0;
}
