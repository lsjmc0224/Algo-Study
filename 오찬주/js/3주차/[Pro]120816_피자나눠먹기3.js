/*

[피자 나눠 먹기 3]

문제 설명
머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다. 
피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, 
n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 
solution 함수를 완성해보세요.

제한사항
2 ≤ slice ≤ 10
1 ≤ n ≤ 100

*/

//문제 풀이
// 나머지, 나누기 활용해 풀기

function solution(slice, n) {
  var answer = 0;
  if (n % slice == 0) {
    answer = n / slice;
  } else if (n % slice !== 0) {
    answer = parseInt(n / slice) + 1;
  }
  return answer;
}

//다른 풀이
//ceil 이용 - 소숫점 올리는 방법

function solution(slice, n) {
  return Math.ceil(n / slice);
}
