/*

문제 설명
한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

제한사항
3 ≤ num_str ≤ 100

*/
//문제 풀이

function solution(num_str) {
  var answer = 0;
  for (var i = 0; i < num_str.length; i++) {
    answer += Number(num_str[i]);
  }
  return answer;
}

//다른 풀이

function solution(num_str) {
  return [...num_str].reduce((a, c) => a + +c, 0);
}

//다른 풀이2
function solution(num_str) {
  var answer = 0;

  num_str.split("").map((a) => (answer += Number(a)));

  return answer;
}
