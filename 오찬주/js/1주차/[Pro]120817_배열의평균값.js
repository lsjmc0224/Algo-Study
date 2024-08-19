/*

[배열의 평균값]

문제 설명
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

제한사항
0 ≤ numbers의 원소 ≤ 1,000
1 ≤ numbers의 길이 ≤ 100
정답의 소수 부분이 .0 또는 .5인 경우만 입력으로 주어집니다.

*/

//문제 풀이
//배열 []
//필요한 것: 배열 속 숫자의 합들(sum), 배열 크기(.length)

function solution(numbers) {
  var answers = 0;
  var sum = 0;

  for (i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }

  var answers = sum / numbers.length;
  return answers;
}
