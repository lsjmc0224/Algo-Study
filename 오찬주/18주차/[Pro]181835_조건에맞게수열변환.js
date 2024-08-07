/*
[조건에 맞게 수열 변환하기 3]

<문제 설명>
정수 배열 arr와 자연수 k가 주어집니다.

만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, k가 짝수라면 arr의 모든 원소에 
k를 더합니다.

이러한 변환을 마친 후의 arr를 return 하는 solution 함수를 완성해 주세요.

<제한사항>
1 ≤ arr의 길이 ≤ 1,000,000
1 ≤ arr의 원소의 값 ≤ 100
1 ≤ k ≤ 100

*/

//문제 풀이

function solution(arr, k) {
  var answer = [];
  if (k % 2 == 1) {
    for (i = 0; i < arr.length; i++) {
      answer.push(arr[i] * k);
    }
  } else {
    for (i = 0; i < arr.length; i++) {
      answer.push(arr[i] + k);
    }
  }
  return answer;
}

//다른 풀이

const solution = (arr, k) => arr.map((v) => (k % 2 ? v * k : v + k));
