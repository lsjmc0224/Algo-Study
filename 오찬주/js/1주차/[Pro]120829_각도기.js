//[각도기]

/*
문제설명

각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 
각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.

예각 : 0 < angle < 90
직각 : angle = 90
둔각 : 90 < angle < 180
평각 : angle = 180

제한사항
0 < angle ≤ 180
angle은 정수입니다.

*/

//문제 풀이
//if, else if문 사용

function solution(angle) {
  var answer = 0;
  if (0 < angle && angle < 90) {
    answer = 1;
  } else if (angle == 90) {
    answer = 2;
  } else if (90 < angle && angle < 180) {
    answer = 3;
  } else if (angle == 180) {
    answer = 4;
  }
  return answer;
}

//다른 풀이: filter 함수
//filter함수를 사용해 배열의 각 요소에 대해 주어진 조건을 만족하는 요소만 남김

function solution(angle) {
  return [0, 90, 91, 180].filter((x) => angle >= x).length;
}

//주어진 각도 angle이 배열의 각 요소 x보다 크거나 같은 경우를 필터링함
//즉, 각 요소 중에서 주어진 각도 이상인 값만 남기게 됨
