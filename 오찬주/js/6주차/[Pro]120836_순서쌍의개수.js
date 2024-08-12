/*

[순서쌍의 개수]

<문제 설명>
순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 
자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 
return하도록 solution 함수를 완성해주세요.

<제한사항>
1 ≤ n ≤ 1,000,000

*/

//문제 풀이
//자연수 n으로 n까지 계속 나누어서 (반복문) 만약 나머지가 0이라면 answer에 값을 하나씩 추가하도록 한다.

function solution(n) {
  var answer = 0;
  for (var i = 0; i <= n; i++) {
    if (n % i == 0) {
      answer++;
    }
  }
  return answer;
}

//다른 풀이 방법

function solution(n) {
  let ans = 0;
  //반복문을 통해 제곱근까지의 수를 순회
  for (let i = 1; i < Math.sqrt(n); i++) if (n % i === 0) ans += 2;

  return Number.isInteger(Math.sqrt(n)) ? ans + 1 : ans;
}
