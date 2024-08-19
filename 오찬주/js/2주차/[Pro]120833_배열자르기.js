/*
[배열 자르기]

문제 설명
정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, 
numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 
solution 함수를 완성해보세요.

제한사항
2 ≤ numbers의 길이 ≤ 30
0 ≤ numbers의 원소 ≤ 1,000
0 ≤num1 < num2 < numbers의 길이


*/

//문제 풀이
//slice 함수 활용하기. .slice(배열의 begin부터 end까지) 이때 end는 미포함!!!!

function solution(numbers, num1, num2) {
  let answer = numbers.slice(num1, num2 + 1);
  return answer;
}

//num2+1을 안하고, num2로만 작성해서 오류가 났었다.
//slice는 end를 포함하지 않으므로 유의해야 한다.
