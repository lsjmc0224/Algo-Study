/*

[마지막 두 원소]

<문제 설명>
정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서 
그전 원소를 뺀 값을 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.

<제한사항>
2 ≤ num_list의 길이 ≤ 10
1 ≤ num_list의 원소 ≤ 9


*/

function solution(num_list) {
  var answer = [...num_list];

  var last = num_list[num_list.length - 1];
  var second = num_list[num_list.length - 2];

  if (last > second) {
    answer.push(last - second);
  } else {
    answer.push(2 * last);
  }
  return answer;
}

//주의할 점:
// 처음에 var answer = [num_list]로 해서 배열 안의 배열을 또 만들어버렸다.
// 전개식을 활용해 얕은 복사를 한 후 push를 해야 한다. 주의 필요
