//[나이 출력]

//문제 설명
//머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다.
//나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.

//제한사항
// - 0 < age ≤ 120
// - 나이는 태어난 연도에 1살이며 1년마다 1씩 증가합니다.

//문제 풀이

function solution(age) {
  var answer = 0;
  answer = 2022 - age + 1;
  return answer;
}

//다른 문제 풀이
//date.getFullYear() 활용하기

/*

function solution(age) {
  return new Date().getFullYear() - age + 1;
}

*/

//다만 getFullYear는 현재 연도를 기준으로 하기에 2022년을 기준으로 할 때는 맞지 않음
//date.getFullYear() 함수가 있다는 것을 알고 갈 것
