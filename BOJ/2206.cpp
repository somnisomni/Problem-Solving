#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
using namespace std;

#define INT32_MAX 2147483647

struct SearchData {
  pair<int, int> coord;
  int depth;
  bool hasBrokeWall;
};

vector<pair<int, int>> deltaMap = {
  make_pair(-1, 0),
  make_pair(0, -1),
  make_pair(1, 0),
  make_pair(0, 1)
};

int findWay(vector<vector<int>> maze) {
  pair<int, int> destination = make_pair(maze.size() - 1, maze[maze.size() - 1].size() - 1);

  queue<SearchData> bfs;
  map<pair<int, int>, bool> visited;
  map<pair<int, int>, bool> visitedWhileBrokeWall;
  int bestDepth = INT32_MAX;

  SearchData initial;
  initial.coord = make_pair(0, 0);
  initial.depth = 1;
  initial.hasBrokeWall = false;

  bfs.push(initial);

  while(!bfs.empty()) {
    SearchData data = bfs.front();
    bfs.pop();

    if(data.hasBrokeWall == false && visited[data.coord] == true) continue;
    if(data.hasBrokeWall == true && visitedWhileBrokeWall[data.coord] == true) continue;

    if(data.hasBrokeWall == true) {
      visitedWhileBrokeWall[data.coord] = true;
    } else {
      visited[data.coord] = true;
    }

    if(data.coord == destination) {
      bestDepth = bestDepth > data.depth ? data.depth : bestDepth;

      break;
    }

    for(pair<int, int> delta : deltaMap) {
      int newY = data.coord.first + delta.first;
      int newX = data.coord.second + delta.second;

      if(newY < 0 || newY >= maze.size() || newX < 0 || newX >= maze[newY].size()) continue;

      int nextValue = maze[newY][newX];

      if(nextValue == 1 && data.hasBrokeWall == true) continue;

      SearchData next;
      next.coord = make_pair(newY, newX);
      next.depth = data.depth + 1;
      next.hasBrokeWall = data.hasBrokeWall || nextValue == 1;

      bfs.push(next);
    }
  }

  return bestDepth >= INT32_MAX ? -1 : bestDepth;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int n, m;
  cin >> n >> m;

  vector<vector<int>> maze(n, vector<int>(m));
  for(int y = 0; y < n; y++) {
    string line;
    cin >> line;

    for(int x = 0; x < m; x++) {
      maze[y][x] = line[x] - '0';
    }
  }

  cout << findWay(maze) << endl;

  return 0;
}
