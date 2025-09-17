#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> nums;
vector<int> dfs;

int maxNum = 0, lineLimit = 0;

void process(int index = 0) {
  dfs.push_back(index);

  if(dfs.size() >= lineLimit) {
    for(int idx : dfs) {
      cout << nums[idx] << " ";
    }
    cout << "\n";

    dfs.pop_back();
    return;
  }

  for(int i = 0; i < maxNum; i++) {
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

  for(int i = 0; i < maxNum; i++) {
    process(i);
  }

  return 0;
}
