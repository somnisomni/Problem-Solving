#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
using namespace std;

vector<int> nums;
vector<int> dfs;
set<string> output;  // 너무 얌체같은 방법 (어차피 WA)

int maxNum = 0, lineLimit = 0;

void process(int index = 0) {
  dfs.push_back(index);

  if(dfs.size() >= lineLimit) {
    string s;

    for(int idx : dfs) {
      s += to_string(nums[idx]) + " ";
    }
    s += "\n";

    output.insert(s);
    dfs.pop_back();
    return;
  }

  for(int i = 0; i < nums.size(); i++) {
    if(find(dfs.begin(), dfs.end(), i) != dfs.end()) continue;

    process(i);
  }

  dfs.pop_back();
}

int main() {
  ios_base::sync_with_stdio(false);
  cout.tie(nullptr);

  cin >> maxNum >> lineLimit;

  for(int i = 0; i < maxNum; i++) {
    int input;
    cin >> input;

    nums.push_back(input);
  }

  sort(nums.begin(), nums.end());

  for(int i = 0; i < nums.size(); i++) {
    process(i);
  }

  for(string s : output) {
    cout << s;
  }

  return 0;
}
