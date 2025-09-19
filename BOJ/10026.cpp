#include <iostream>
#include <vector>
#include <queue>
#include <map>
using namespace std;

vector<pair<int, int>> deltas = {
  make_pair(-1, 0),
  make_pair(0, -1),
  make_pair(1, 0),
  make_pair(0, 1)
};

int findAreas(vector<vector<char>> areaMap) {
  queue<pair<int, int>> bfs;
  map<pair<int, int>, bool> visited;

  int areas = 0;

  for(int y = 0; y < areaMap.size(); y++) {
    for(int x = 0; x < areaMap[y].size(); x++) {
      pair<int, int> coord = make_pair(y, x);
      char currentChar = areaMap[coord.first][coord.second];

      if(visited[coord] == true) continue;

      bfs.push(coord);

      while(!bfs.empty()) {
        pair<int, int> bfsCoord = bfs.front();
        bfs.pop();

        if(visited[bfsCoord] == true) continue;
        visited[bfsCoord] = true;

        for(pair<int, int> delta : deltas) {
          int newY = bfsCoord.first + delta.first;
          int newX = bfsCoord.second + delta.second;

          if(newY < 0 || newY >= areaMap.size() || newX < 0 || newX >= areaMap[newY].size()) continue;

          char nextChar = areaMap[newY][newX];

          if(currentChar == nextChar) {
            bfs.push(make_pair(newY, newX));
          }
        }
      }

      areas++;
    }
  }

  return areas;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int n;
  cin >> n;

  vector<vector<char>> areaMap(n, vector<char>(n));
  vector<vector<char>> areaMapColorBlindness(n, vector<char>(n));

  for(int y = 0; y < n; y++) {
    string line;
    cin >> line;

    for(int x = 0; x < n; x++) {
      areaMap[y][x] = line[x];
      areaMapColorBlindness[y][x] = line[x];

      if(line[x] == 'G') areaMapColorBlindness[y][x] = 'R';
    }
  }

  cout << findAreas(areaMap) << " " << findAreas(areaMapColorBlindness) << endl;

  return 0;
}
