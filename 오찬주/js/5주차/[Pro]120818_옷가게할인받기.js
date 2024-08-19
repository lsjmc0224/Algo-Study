/*

[옷가게 할인받기]

문제 설명
머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 
50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때, 
지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

제한사항
10 ≤ price ≤ 1,000,000
price는 10원 단위로(1의 자리가 0) 주어집니다.
소수점 이하를 버린 정수를 return합니다.


*/

//문제 풀이
//엄청나게 .. 더럽게 풀었다 ...

function solution(price) {
  var answer = 0;
  if (0 < price && price < 100000) {
    answer = price;
  } else if (300000 > price && price >= 100000) {
    answer = Math.floor(price - price * 0.05);
  } else if (500000 > price && price >= 300000) {
    answer = Math.floor(price - price * 0.1);
  } else if (price >= 500000) {
    answer = Math.floor(price - price * 0.2);
  }
  return answer;
}

//다른 문제 풀이
// 같은 반복문이어도 이렇게 풀면 후ㅓ어ㅓ어얼씬 깔끔하다...
// 가장 먼저 어떤 반복문을 돌리는지도 중요 포인트!!

function solution(price) {
  var answer = price;
  if (answer >= 500000) {
    answer *= 0.8;
  } else if (answer >= 300000) {
    answer *= 0.9;
  } else if (answer >= 100000) {
    answer *= 0.95;
  }

  return parseInt(answer);
}

//다른 문제 풀이

const discounts = [
  [500000, 20],
  [300000, 10],
  [100000, 5],
];

const solution = (price) => {
  for (const discount of discounts)
    if (price >= discount[0])
      return Math.floor(price - (price * discount[1]) / 100);
  return price;
};
