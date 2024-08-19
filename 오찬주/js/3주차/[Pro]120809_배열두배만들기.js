/*

[배열 두 배 만들기]

문제 설명
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

제한사항
-10,000 ≤ numbers의 원소 ≤ 10,000
1 ≤ numbers의 길이 ≤ 1,000


*/

//풀이
//배열의 수에 2를 곱한 후 answer에 Push 해야겠다!!

function solution(numbers) {
  answer = [];
  for (var i = 0; i < numbers.length; i++) {
    answer.push(numbers[i] * 2);
  }
  return answer;
}

//다른 풀이
/*
reduce 메소드
:  배열의 각 요소를 반복하고 결과를 누적함

*/

function solution(numbers) {
  //reduce 메서드의 첫 번째 인수인 콜백 함수 - (a, b) => [...a, b * 2]
  //현재 누적된 값(a)과 현재 처리 중인 요소(b)
  //각 요소를 처리할 때마다 누적된 배열 a에 현재 요소 b의 두 배를 추가

  //[]: reduce 메서드의 두 번째 인수는 누적 변수의 초기 값
  //배열의 첫 번째 요소부터 시작하여 각 요소를 두 배로 만든 새로운 배열이 만들어짐
  return numbers.reduce((a, b) => [...a, b * 2], []);
}

//map 메소드

const solution = (numbers) => numbers.map((numbers) => numbers * 2);
