#include <iostream>
#include <vector>
using namespace std;

vector<int> dfs;

int maxNum = 0, lineLimit = 0;

void process(int num = 1) {
  dfs.push_back(num);

  if(dfs.size() >= lineLimit) {
    for(int v : dfs) {
      cout << v << " ";
    }
    cout << endl;

    dfs.pop_back();
    return;
  }

  for(int i = num; i <= maxNum; i++) {
    process(i);
  }

  dfs.pop_back();
}

int main() {
  cin >> maxNum >> lineLimit;

  for(int i = 1; i <= maxNum; i++) {
    process(i);
  }

  return 0;
}
