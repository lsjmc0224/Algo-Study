/*

[짝수, 홀수 구하기]

문제 설명
정수가 담긴 리스트 num_list가 주어질 때, 
num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 
solution 함수를 완성해보세요.

제한사항
1 ≤ num_list의 길이 ≤ 100
0 ≤ num_list의 원소 ≤ 1,000

입출력 예
num_list	/ result
[1, 2, 3, 4, 5]	/ [2, 3]
[1, 3, 5, 7]	/ [0, 4]

*/

function solution(num_list) {
  var answer = [];
  var Even = 0;
  var Odd = 0;
  for (var i = 0; i < num_list.length; i++) {
    if (num_list[i] % 2 == 0) {
      Even++;
    }
  }
  var Odd = num_list.length - Even;
  answer.push(Even);
  answer.push(Odd);
  return answer;
}

//다른 문제 풀이
// for (let a of) 형태

function solution(num_list) {
  //결과 저장할 배열 0,0으로 초기화
  var answer = [0, 0];

  //주어진 배열의 각 요소에 대해 반복
  for (let a of num_list) {
    // 현재 요소가 짝수인지 홀수인지 확인하고,
    // 해당하는 인덱스의 개수를 1 증가
    answer[a % 2] += 1;
  }

  return answer;
}
