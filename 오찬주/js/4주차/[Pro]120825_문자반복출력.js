/*

[문자 반복 출력하기]

문제 설명
문자열 my_string과 정수 n이 매개변수로 주어질 때, 
my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 
solution 함수를 완성해보세요.

제한사항
2 ≤ my_string 길이 ≤ 5
2 ≤ n ≤ 10
"my_string"은 영어 대소문자로 이루어져 있습니다.

입출력 예
my_string / n /	result
"hello"	/ 3	/ "hhheeellllllooo"


*/

function solution(my_string, n) {
  var answer = "";
  for (var i = 0; i < my_string.length; i++) {
    for (var j = 0; j < n; j++) {
      answer += my_string.charAt(i);
    }
  }
  return answer;
}

//다른 풀이

function solution(my_string, n) {
  //[...my_string]: 구조 분해 할당
  // map으로 배열의 요소 빼줌
  // repeat으로 각 배열의 요소를 n번 반복
  // join으로 배열요소 사이를 ""로 붙여줌
  var answer = [...my_string].map((v) => v.repeat(n)).join("");
  console.log(answer);
  return answer;
}
