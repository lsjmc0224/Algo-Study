/*
[평행]

<문제 설명>
점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
주어진 네 개의 점을 두 개씩 이었을 때, 
두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 
solution 함수를 완성해보세요.

<제한사항>
dots의 길이 = 4
dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
0 ≤ x, y ≤ 100
서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.

*/

//문제 풀이

function solution(dots) {
  //평행 = 기울기 같음
  //기울기=y축 증가량 / x축 증가량
  const [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots;

  //1-2, 3-4
  if ((y1 - y2) / (x1 - x2) == (y3 - y4) / (x3 - x4)) return 1;

  //1-3, 2-4
  if ((y1 - y3) / (x1 - x3) == (y2 - y4) / (x2 - x4)) return 1;

  //1-4, 2-3
  if ((y1 - y4) / (x1 - x4) == (y2 - y3) / (x2 - x3)) return 1;

  return 0;
}

//다른 풀이

//함수를 만들어서 반복되는 코드 줄일 수 있음!!

function solution(dots) {
  if (calculateSlope(dots[0], dots[1]) === calculateSlope(dots[2], dots[3]))
    return 1;
  if (calculateSlope(dots[0], dots[2]) === calculateSlope(dots[1], dots[3]))
    return 1;
  if (calculateSlope(dots[0], dots[3]) === calculateSlope(dots[1], dots[2]))
    return 1;
  return 0;
}

function calculateSlope(arr1, arr2) {
  return (arr2[1] - arr1[1]) / (arr2[0] - arr1[0]);
}
