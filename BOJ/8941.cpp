#include <iostream>
#include <iomanip>
#include <map>
#include <vector>
#include <string>
using namespace std;

map<char, double> massMap = {
  { 'C', 12.01 },
  { 'H', 1.008 },
  { 'O', 16.00 },
  { 'N', 14.01 }
};

vector<pair<char, int>> parseFormula(string formula) {
  vector<pair<char, int>> parsed;

  char currentElement = '\0';
  string numStr;

  for(char seg : formula) {
    if(seg >= '0' && seg <= '9') {
      numStr += seg;
    } else {
      if(currentElement != '\0') {
        parsed.push_back(make_pair(currentElement, numStr.empty() ? 1 : stoi(numStr)));
      }

      currentElement = seg;
      numStr.clear();
    }
  }

  if(currentElement != '\0') {
    parsed.push_back(make_pair(currentElement, numStr.empty() ? 1 : stoi(numStr)));
  }

  return parsed;
}

int main() {
  int t;
  cin >> t;

  for(; t > 0; t--) {
    string input;
    cin >> input;

    double sum = 0.0;
    vector<pair<char, int>> parsed = parseFormula(input);
    for(pair<char, int> item : parsed) {
      sum += massMap[item.first] * item.second;
    }

    cout << fixed << setprecision(3) << sum << endl;
  }

  return 0;
}
