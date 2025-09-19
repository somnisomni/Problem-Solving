#include <iostream>
#include <vector>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  string input;
  cin >> input;
  input += "-";  // for문에서 마지막 숫자 세그먼트 처리를 위함

  vector<int> nums;
  string segment;
  bool minus = false;
  for(char c : input) {
    if(c == '-' || c == '+') {
      int segmentValue = stoi(segment);

      nums.push_back(minus ? -segmentValue : segmentValue);

      segment = "";
      if(c == '-') minus = true;
    } else {
      segment += c;
    }
  }

  int value = 0;
  for(int num : nums) value += num;

  cout << value << endl;

  return 0;
}
