// C++ 형변환 개싫다

#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int n;
  int s, m, l, xl, xxl, xxxl;
  int t, p;

  cin >> n;
  cin >> s >> m >> l >> xl >> xxl >> xxxl;
  cin >> t >> p;

  // 티셔츠 = ceil(s / T) + ceil(m / T) + ceil(l / T) + ceil(xl / T) + ceil(xxl / T) + ceil(xxxl / T)
  // 펜 묶음 = floor(n / P), 한 자루씩 = n % P

  // string split하고 for문 돌려도 되지만 C++에선 그거 작성하기 넘 귀찮

  cout << (long long)(ceill((long double)s / t) + ceill((long double)m / t) + ceill((long double)l / t) + ceill((long double)xl / t) + ceill((long double)xxl / t) + ceill((long double)xxxl / t)) << endl;
  cout << (long long)floor((long double)n / p) << " " << n % p << endl;

  // cmath의 ceil(float)을 사용하면 정확도 이슈 발생
  //   -> ceil(long double) 또는 ceill(long double) 또는 ((a + b - 1) / b) 사용
  //   && 형변환에 int/float 쓰면 WA, 큰 자료형으로 변환해야함

  // 테스트케이스
  // 1000000000
  // 166666667 166666667 166666667 166666667 166666667 166666665
  // 2 2
  //
  // 정상 출력
  // 500000003
  // 500000000 0
  //
  // 비정상 출력
  // 500000032
  // 500000000 0

  return 0;
}
