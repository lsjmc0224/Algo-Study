/*

[flag에 따른 다른 값 반환하기]

<문제 설명>
두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, 
flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.

<제한사항>
-1,000 ≤ a, b ≤ 1,000


*/

function solution(a, b, flag) {
  if (flag) {
    return a + b;
  } else {
    return a - b;
  }
}

//처음에는 조건문에 flag==true를 명시했다. 그런데 생각해보니 .. 굳이 ..?? ㅜㅠㅜㅜㅜ 애초에 if 문이 true면 해당 코드를 실행한다! 이고
//flag 자체가 true or false 값을 가지니 필요가 없다는 것을 .. 깨달았다..

//다른 풀이 1

function solution(a, b, flag) {
  return flag ? a + b : a - b;
}

//다른 풀이 2

const solution = (a, b, flag) => (flag ? a + b : a - b);
