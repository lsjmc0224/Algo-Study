/*

[중복된 문자 제거]

<문제 설명>
문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 
하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

<제한사항>
1 ≤ my_string ≤ 110
my_string은 대문자, 소문자, 공백으로 구성되어 있습니다.
대문자와 소문자를 구분합니다.
공백(" ")도 하나의 문자로 구분합니다.
중복된 문자 중 가장 앞에 있는 문자를 남깁니다.

*/

//문제 풀이

function solution(my_string) {
  var answer = "";
  for (var i = 0; i < my_string.length; i++) {
    if (i === my_string.indexOf(my_string[i])) {
      answer += my_string[i];
    }
  }
  return answer;
}

//다른 문제 풀이
//set객체는 중복되지 않은 유일한 값들의 집합으로 동일한 값을 중복하여 포함할 수 없다
//set 객체는 생성자 함수로 생성하여 인수를 전달한다. (전달하지 않으면 빈 Set객체 생성)

function solution(my_string) {
  return [...new Set(my_string)].join("");
}
