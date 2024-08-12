/*

[가까운 수]

<문제 설명>
정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 
정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

<제한사항>
1 ≤ array의 길이 ≤ 100
1 ≤ array의 원소 ≤ 100
1 ≤ n ≤ 100
가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.

*/

//문제 풀이

function solution(array, n) {
  //[3, 10, 28], 20
  array.sort((x, y) => x - y);
  let differ = Infinity;
  let num = 0;

  for (let i of array) {
    if (Math.abs(n - i) < differ) {
      differ = Math.abs(n - i);
      num = i;
    }
  }
  return num;
}
