#include <iostream>
using namespace std;

int dp[1025][1025];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int n, m;
  cin >> n >> m;

  int cell = 0;
  for(int x = 1; x <= n; x++) {
    for(int y = 1; y <= n; y++) {
      cin >> cell;

      dp[x][y] = dp[x][y - 1] + dp[x - 1][y] - dp[x - 1][y - 1] + cell;
    }
  }

  int x1, y1, x2, y2;
  for(; m > 0; m--) {
    cin >> x1 >> y1 >> x2 >> y2;

    cout << dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1] << "\n";
  }

  return 0;
}
