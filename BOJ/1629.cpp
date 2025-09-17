// Reference: https://velog.io/@junttang/BOJ-1629-%EA%B3%B1%EC%85%88-%ED%95%B4%EA%B2%B0-%EC%A0%84%EB%9E%B5-C
//
// a ^ b = a ^ (b / 2) * a ^ (b / 2)로 왜 나뉘어질 수 있는가? 하면 지수법칙을 생각해보면 된다.
//       = a ^ ((b / 2) + (b / 2))
//       = a ^ (2b / 2)
//       = a ^ b
// Divide & Conquer를 위해 일부러 계산식을 나누는 것
//
// 홀수인 경우에는 정수의 나눗셈 과정에서 소수점 아래는 버려지기 때문에 a ^ 1를 곱한 만큼이 부족해지기에 보정 필요
//       = a ^ (b / 2) * a ^ (b / 2 + 1)
//       = a ^ (b / 2) * a ^ (b / 2) * a ^ 1
//
// 나머지 연산은 "시도때도 없이" 하면 된다.

#include <iostream>
using namespace std;

long long powDNQ(const long long base, const long long power, const long long mod) {
  // n ^ 0의 값은 언제나 1
  if(power == 0) return 1;

  // n ^ 1의 값은 언제나 n
  if(power == 1) return base % mod;

  // n ^ 2 이상부터 위에서 나눈 계산식에 따라 분할 정복
  // 재귀를 줄이기 위해 분할된 문제의 결과값을 재사용
  long long dnqValue = powDNQ(base, power / 2, mod) % mod;
  if(power % 2 == 0) return dnqValue * dnqValue % mod;
  return ((dnqValue * dnqValue % mod) * (base % mod)) % mod;
}

int main() {
  long long a, b, c;
  cin >> a >> b >> c;

  cout << powDNQ(a, b, c) << endl;

  return 0;
}
