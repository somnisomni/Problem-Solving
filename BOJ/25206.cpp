#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <map>
using namespace std;

constexpr int INPUT_LINES = 20;

const map<string, float> SCORE_MAP = {
  { "A+", 4.5f },
  { "A0", 4.0f },
  { "B+", 3.5f },
  { "B0", 3.0f },
  { "C+", 2.5f },
  { "C0", 2.0f },
  { "D+", 1.5f },
  { "D0", 1.0f },
  { "F",  0.0f },
};

vector<string> split(string source, char delimiter = ' ') {
  istringstream stream(source);
  string buf;
  vector<string> result;

  while(getline(stream, buf, delimiter)) {
    result.push_back(buf);
  }

  return result;
}

int main() {
  float scoreSum = 0.0f;
  float hakSum = 0.0f;

  for(int i = 0; i < INPUT_LINES; i++) {
    string line;
    getline(cin, line);

    vector<string> elements = split(line);
    if(elements[2] == "P") continue;

    float hak = stof(elements[1]);
    hakSum += hak;
    scoreSum += hak * SCORE_MAP.at(elements[2]);
  }

  float avg = scoreSum / hakSum;
  cout << fixed << setprecision(6) << avg;

  return 0;
}
