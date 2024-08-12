/*
[피자 나눠먹기(1)]

문제 설명
머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때, 
모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

제한사항
1 ≤ n ≤ 100
*/

//문제 풀이
//Math.floor 사용

function solution(n) {
  return n % 7 === 0 ? Math.floor(n / 7) : Math.floor(n / 7) + 1;
}

//다른 풀이
//Math.ceil() 함수
//Math.ceil() : 소수점 이하를 올림한다.

function solution(n) {
  return Math.ceil(n / 7);
}
