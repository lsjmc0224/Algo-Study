/*

[문제 설명]

실수 flo가 매개 변수로 주어질 때, flo의 정수 부분을 return하도록 solution 함수를 완성해주세요.

*/

function solution(flo) {
  return Math.floor(flo);
}

//다른 풀이
function solution(flo) {
  return parseInt(flo);
}

//다른 풀이2

const solution = Math.trunc;
