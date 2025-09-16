#include <string>
using namespace std;

int solution(int n) {
  int result = 0;
  string seq = to_string(n);

  for(char c : seq) {
    result += c - '0';
  }

  return result;
}
