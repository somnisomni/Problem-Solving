#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
  string diff;

  sort(participant.begin(), participant.end());
  sort(completion.begin(), completion.end());

  for(int index = 0; index < participant.size(); index++) {
    // participant 배열의 마지막까지 체크하는 경우를 고려해야 함
    //   -> index 바운더리 체크 안하면 completion[index]에서 segfault 발생
    if(index == participant.size() - 1 || participant[index] != completion[index]) {
      diff = participant[index];
      break;
    }
  }

  return diff;
}
