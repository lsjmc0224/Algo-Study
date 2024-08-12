// [짝수의 합]

/*
문제 설명
정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

제한 사항
0 < n ≤ 1000

*/

// 문제 풀이

function solution(n) {
  var sum = 0;

  for (i = 0; i <= n; i++) {
    if (n % 2 == 0) {
      sum += i;
    }
  }
  return sum;
}

/*
다른 문제 풀이: 수열 공식 활용하기 (Math.floor)
*/

function solution(n) {
  var half = Math.floor(n / 2);
  return half * (half + 1);
}
