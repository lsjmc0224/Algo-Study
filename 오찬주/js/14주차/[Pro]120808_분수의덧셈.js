/*

[분수의 덧셈]

<문제 설명>
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

<제한사항>
0 <numer1, denom1, numer2, denom2 < 1,000
*/

function solution(numer1, denom1, numer2, denom2) {
  var answer = [];

  //분모 구하기
  let denom = denom1 * denom2;

  //분자 구하기
  let numer = denom1 * numer2 + denom2 * numer1;

  //최대 공약수구하기
  //최대 공약수: 두 수의 공통된 약수 중에서 가장 큰 정수
  //구하는 방법: 유클리드 호제법

  let getGCD = (a, b) => (b > 0 ? getGCD(b, a % b) : a);
  let gcd = getGCD(numer, denom);

  //최대 공약수를 분자, 분모에 나누고 배열에 넣기
  answer[0] = numer / gcd;
  answer[1] = denom / gcd;

  return answer;
}
