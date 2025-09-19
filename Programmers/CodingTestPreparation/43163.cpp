#include <iostream>

#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <queue>
using namespace std;

int solution(string begin, string target, vector<string> words) {
  if(find(words.begin(), words.end(), target) == words.end()) {
    return 0;
  }

  if(find(words.begin(), words.end(), begin) == words.end()) {
    words.push_back(begin);
  }

  // == link map building
  unordered_map<string, vector<string>> linkMap;
  for(string targetWord : words) {
    for(string wordSearch : words) {
      if(targetWord == wordSearch) continue;

      int diff = 0;

      for(int index = 0; index < targetWord.length(); index++) {
        if(targetWord[index] != wordSearch[index]) {
          diff++;
        }
      }

      if(diff == 1) {
        linkMap[targetWord].push_back(wordSearch);
      }
    }
  }
  // ==

  // == bfs
  queue<pair<string, int>> bfs;
  unordered_map<string, bool> visited;
  int minStep = 2147483647;
  bool found = false;

  bfs.push(make_pair(begin, 0));
  while(!bfs.empty()) {
    string currentWord = bfs.front().first;
    int currentDepth = bfs.front().second;
    bfs.pop();

    if(visited[currentWord] == true) {
      visited.erase(currentWord);
      continue;
    }

    if(currentWord == target) {
      found = true;

      if(minStep > currentDepth) {
        minStep = currentDepth;
      }

      break;
    }

    visited[currentWord] = true;

    for(string linkedWords : linkMap[currentWord]) {
      bfs.push(make_pair(linkedWords, currentDepth + 1));
    }
  }
  // ==

  return found ? minStep : 0;
}

// == //

int main() {
  string begin = "hit";
  string target = "cog";
  vector<string> words = { "hot", "dot", "dog", "lot", "log", "cog" };

  // string begin = "abc";
  // string target = "cde";
  // vector<string> words = { "adc", "ade", "cde", "bbc", "bdc" };

  cout << solution(begin, target, words) << endl;

  return 0;
}
