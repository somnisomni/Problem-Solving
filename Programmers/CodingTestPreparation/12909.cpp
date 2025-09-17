#include <string>
#include <stack>
#include <iostream>
using namespace std;

bool solution(string s) {
    stack<bool> stk;

    for(char c : s) {
        if(c == '(') stk.push(true);
        else if(stk.empty() && c == ')') return false;
        else stk.pop();
    }

    return stk.empty();
}

// == //

int main() {
  string s;
  cin >> s;

  cout << solution(s);

  return 0;
}
