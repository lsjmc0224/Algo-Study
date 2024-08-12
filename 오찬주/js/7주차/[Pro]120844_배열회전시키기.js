/*

[배열 회전시키기]

<문제 설명>
정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 
배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 
solution 함수를 완성해주세요.

<제한사항>
3 ≤ numbers의 길이 ≤ 20
direction은 "left" 와 "right" 둘 중 하나입니다.


*/

/*

<문제풀이>

pop 메소드: 배열에서 마지막 요소를 제거하고 그 요소를 반환
shift 메소드: 배열에서 첫 번째 요소를 제거하고, 제거된 요소를 반환
unshift 메소드: 추출한 요소를 배열의 맨 앞에 값을 추가



*/

function solution(numbers, direction) {
  if (direction == "right") {
    var n = numbers.pop();
    numbers.unshift(n);
  } else {
    var n = numbers.shift();
    numbers.push(n);
  }
  return numbers;
}
