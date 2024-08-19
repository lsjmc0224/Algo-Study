//[몫 구하기]

//문제 설명
// 정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.

// 제한사항
// 0 < num1 ≤ 100
// 0 < num2 ≤ 100

//문제 링크
//https://school.programmers.co.kr/learn/courses/30/lessons/120805?language=javascript

function solution(num1, num2) {
  var answer = parseInt(num1 / num2);
  return answer;
}

//다른 방식
//Math.floor 활용하기

function solution(num1, num2) {
  var answer = Math.floor(num1 / num2);
  return answer;
}

//Math.floor와 화살표 함수 활용
const solution = (num1, num2) => Math.floor(num1 / num2);

//Math.floor()함수: 주어진 숫자와 같거나 작은 정수 중에서 가장 큰 수를 반환
