#include <vector>
#include <string>
using namespace std;

string solution(string s) {
  int max = -2147483647;
  int min = 2147483647;

  string sNew = s + " ";
  string seg;
  for(char c : sNew) {
    if(c == ' ') {
      int val = stoi(seg);
      seg = "";

      if(val > max) max = val;
      if(val < min) min = val;

      continue;
    }

    seg += c;
  }

  return to_string(min) + " " + to_string(max);
}
