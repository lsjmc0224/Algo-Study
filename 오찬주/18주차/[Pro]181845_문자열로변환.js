/*

[문자열로 변환]

<문제 설명>
정수 n이 주어질 때, n을 문자열로 변환하여 return하도록 solution 함수를 완성해주세요.

<제한사항>
1 ≤ n ≤ 10000

*/

//문제 풀이

function solution(n) {
  return n.toString();
}

// 위 풀이는 함수 선언식이고, 만약 함수 표현식으로 짠다면 이렇게 짜면 된다.

const solution = (n) => String(n);
