/*

[중복된 숫자 개수]

문제 설명
정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, 
array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

제한사항
1 ≤ array의 길이 ≤ 100
0 ≤ array의 원소 ≤ 1,000
0 ≤ n ≤ 1,000

문제 풀이 도출 과정
//배열이기에 반복을 하면서 n과 같은 숫자 찾기.
//if문 활용해 만약 같다면 answer을 하나씩 증가시키기.
//처음에 answer을 0으로 선언해야 함

*/

function solution(array, n) {
  var answer = 0;
  for (var i = 0; i < array.length; i++) {
    if (array[i] == n) {
      answer++;
    }
  }
  return answer;
}

// var array = [3, 4, 5, 1, 32, 3];

// console.log(solution(array, 3));

//다른 풀이 방법
//filter를 활용

function solution(array, n) {
  var answer = 0;
  let Array = array.filter((item) => item === n);
  answer = Array.length;

  return answer;
}
