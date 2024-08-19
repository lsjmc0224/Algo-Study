/*

[최댓값 만들기1]

문제 설명정수 
배열 numbers가 매개변수로 주어집니다. 
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 
solution 함수를 완성해주세요.

제한사항
0 ≤ numbers의 원소 ≤ 10,000
2 ≤ numbers의 길이 ≤ 100

*/

/*문제 풀이

처음에는 for문 반복문을 써서 가장 큰 수를 구하고, 그 다음에 큰 수를 구하려고 했으나, 너무 복잡했음
그리하여 든 생각은 numbers를 내림차순으로 정렬하여 index 0번째와 1번째를 곱해버리자!

이를 위해 필요한 함수는
sort()다.
이때 compareFunction(비교 함수)이 제공되는데, function(a, b) { return b - a; } 
이런 형태이다.

a - b를 반환하면, a가 b보다 작을 경우 음수를 반환하여 정렬 (오름차순)
b - a를 반환하면, b가 a보다 작을 경우 음수를 반환하여 정렬 (내림차순)

*/

function solution(numbers) {
  var answer = 0;
  numbers.sort(function (a, b) {
    return b - a;
  });

  answer = numbers[0] * numbers[1];
  return answer;
}
var numbers = [4, 8, 9, 0, 30, 2];
console.log(solution(numbers));

// --------------------------------------------

//더 간단하게 쓰는 방법 (arrow function 활용)

function solution(numbers) {
  numbers.sort((a, b) => b - a);
  return numbers[0] * numbers[1];
}
