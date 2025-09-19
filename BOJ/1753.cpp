#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

// map<정점 인덱스, vector<pair<연결 정점 인덱스, 가중치>>>
unordered_map<int, vector<pair<int, int>>> graph;

int totalVertices, startVertex;

void dijkstra() {
  // 최소힙(오름차순), pq[?].first == 대상 정점까지의 비용 (1차 비교 기준), pq[?].second == 대상 정점 번호 (2차 비교 기준)
  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

  // 시작 정점(startVertex)로부터 각 정점까지의 거리를 저장하는 배열
  vector<int> distToVertices(totalVertices + 1, 2147483647);

  // 시작 정점의 거리를 0으로 설정
  distToVertices[startVertex] = 0;

  // 시작 정점을 큐에 등록
  pq.push(make_pair(0, startVertex));

  while(!pq.empty()) {
    // 현재 큐에서 비용이 가장 적은 정점 취득
    pair<int, int> pqTop = pq.top();
    int currentCost = pqTop.first;
    int currentVertex = pqTop.second;
    pq.pop();

    // 연결된 정점 순회
    for(pair<int, int> edge : graph[currentVertex]) {
      // 연결된 정점까지의 거리 계산
      int distToEdgeVertex = currentCost + edge.second;

      // 다익스트라에선 연결된 정점까지의 새로 계산된 거리가 이미 등록된 거리보다 더 길 경우 처리할 필요 없음
      // 이는 visited 배열을 따로 두는 것과 동일한 효과
      // 이 분기가 없으면 메모리 초과 (처리할 필요 없는 정점까지 PQ에 올려야 하므로)
      if(distToEdgeVertex >= distToVertices[edge.first]) continue;

      // 연결된 정점까지의 거리 갱신
      distToVertices[edge.first] = distToEdgeVertex;

      // 큐에 연결된 정점 등록
      pq.push(make_pair(distToVertices[edge.first], edge.first));
    }
  }

  // 정점마다 계산된 최소 거리 출력
  for(int i = 1; i < distToVertices.size(); i++) {
    cout << (distToVertices[i] >= 2147483647 ? "INF" : to_string(distToVertices[i])) << "\n";
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int edges;
  cin >> totalVertices >> edges >> startVertex;

  for(int i = 0; i < edges; i++) {
    int startV, connectV, weight;
    cin >> startV >> connectV >> weight;

    graph[startV].push_back(make_pair(connectV, weight));
  }

  dijkstra();

  return 0;
}
