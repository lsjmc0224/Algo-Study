/*

문제 설명
머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 
머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 
머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

제한사항
1 ≤ array의 길이 ≤ 100
1 ≤ height ≤ 200
1 ≤ array의 원소 ≤ 200

*/

//문제 풀이
// 1. array 배열 안 숫자들이 height보다 큰 지 비교하기.
// 2. 만약 크다면 count 숫자 하나씩 증가하기

function solution(array, height) {
  var count = 0;
  for (var i = 0; i < array.length; i++) {
    if (array[i] > height) {
      count++;
    }
  }
  return count;
}
