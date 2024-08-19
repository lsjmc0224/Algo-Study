/*

[아이스아메리카노]

문제 설명
머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 
아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 
머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 
return 하도록 solution 함수를 완성해보세요.

제한사항
0 < money ≤ 1,000,000


*/

//문제 풀이
//잔 수(count)와 남는 돈(remain)을 각각 구한 후 answer에 push해서 구하면 될 듯

function solution(money) {
  var answer = [];
  count = Math.floor(money / 5500);
  remain = money - 5500 * count;
  answer.push(count);
  answer.push(remain);
  return answer;
}

//다른 문제 풀이

function solution(money) {
  return [Math.floor(money / 5500), money % 5500];
}
