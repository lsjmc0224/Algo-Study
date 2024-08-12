/*

[약수 구하기]

<문제 설명>
정수 n이 매개변수로 주어질 때,
n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

<제한사항>
1 ≤ n ≤ 10,000

*/

//문제 풀이

function solution(n) {
  let answer = [];

  for (let i = 1; i <= n; i++) {
    if (n % i === 0) {
      answer.push(i);
    }
  }

  return answer;
}

//다른 문제 풀이 1

function solution(n) {
  return Array(n)
    .fill(0)
    .map((v, index) => v + index + 1)
    .filter((v) => n % v === 0);
}
