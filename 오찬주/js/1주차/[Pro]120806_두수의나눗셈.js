//[두 수의 나눗셈]

/*
문제 설명
정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 
1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.
*/

/*
제한 사항 
0 < num1 ≤ 100
0 < num2 ≤ 100
*/

//문제 풀이
//Math.floor 사용하기

function solution(num1, num2) {
  var answer = 0;
  answer = Math.floor((num1 / num2) * 1000);
  return answer;
}

//다른 방법: trunc() 사용가능

/*
Math.floor(): 소수점을 내림한다.
ex) Math.floor(24.4) = 24, Math.floor(-24.4) = 25

Math.trunc(): 소수점 이하는 다 버린다.
*/
