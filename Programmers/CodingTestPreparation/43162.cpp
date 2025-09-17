#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <map>
using namespace std;

map<int, bool> visited;
stack<int> dfs;

bool networkDfs(vector<vector<int>> computers, int current) {
  if(visited[current]) return false;

  dfs.push(current);

  while(!dfs.empty()) {
    int dfsIndex = dfs.top();
    dfs.pop();

    if(visited[dfsIndex]) continue;
    visited[dfsIndex] = true;

    vector<int> nodeNetwork = computers[dfsIndex];
    for(int index = 0; index < nodeNetwork.size(); index++) {
      if(nodeNetwork[index] == 1) dfs.push(index);
    }
  }

  return true;
}

int solution(int n, vector<vector<int>> computers) {
  int answer = 0;

  for(int index = 0; index < computers.size(); index++) {
    if(networkDfs(computers, index)) answer++;
  }

  return answer;
}

// == //

int main() {
  vector<vector<int>> testcase = {
    { 1, 1, 0 },
    { 1, 1, 0 },
    { 0, 0, 1 }
  };

  cout << solution(3, testcase) << endl;

  return 0;
}
