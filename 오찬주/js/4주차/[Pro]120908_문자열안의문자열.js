/*

[문자열 안의 문자열]

문제 설명
문자열 str1, str2가 매개변수로 주어집니다. 
str1 안에 str2가 있다면 1을, 없다면 2를 return하도록 
solution 함수를 완성해주세요.

제한사항
1 ≤ str1의 길이 ≤ 100
1 ≤ str2의 길이 ≤ 100
문자열은 알파벳 대문자, 소문자, 숫자로 구성되어 있습니다.

*/

//문제 풀이
//includes 활용

function solution(str1, str2) {
  var answer = 2;
  if (str1.includes(str2)) {
    answer = 1;
  }
  return answer;
}

// var str1 = "poppy";
// var str2 = "po";

// console.log(solution(str1, str2));

//다른 문제 풀이
/*
split() 함수

string.split(separator, limit)


*/

function solution(str1, str2) {
  //str2를 기준으로 str1을 분할
  //만약 분할된게 없다? 즉,str1의 분할된 length가 1 초과다?
  // str2가 str1에 없다!!는 뜻
  return str1.split(str2).length > 1 ? 1 : 2;
}
