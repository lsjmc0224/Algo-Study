/*

[대문자와 소문자]

<문제 설명>
문자열 my_string이 매개변수로 주어질 때, 
대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 
solution 함수를 완성해주세요.

<제한사항>
1 ≤ my_string의 길이 ≤ 1,000
my_string은 영어 대문자와 소문자로만 구성되어 있습니다.


*/

/*

[문제 풀이]

toUpperCase
toLowerCase 
사용하기

*/

function solution(my_string) {
  let arr = [];
  for (let i = 0; i < my_string.length; i++) {
    //대문자라면 소문자로 바꿔서 my_string[i]에 push하기
    if (my_string[i] === my_string[i].toUpperCase()) {
      arr.push(my_string[i].toLowerCase());
      //소문자라면 대문자로 바꿔서 my_string[i]에 push하기
    } else {
      arr.push(my_string[i].toUpperCase());
    }
  }
  //바꾼 값 합치기
  return arr.join("");
}
