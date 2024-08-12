/*

문제 설명
문자열 배열 strlist가 매개변수로 주어집니다. 
strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ strlist 원소의 길이 ≤ 100
strlist는 알파벳 소문자, 대문자, 특수문자로 구성되어 있습니다.

입출력 예
strlist	result
["We", "are", "the", "world!"]	[2, 3, 3, 6]
["I", "Love", "Programmers."]	[1, 4, 12]

*/

//문제 풀이
//배열의 원소들의 길이를 answer에 계속 추가해주기. (length, push 사용)

function solution(strlist) {
  //정답은 배열로 되어있음
  var answer = [];
  for (var i = 0; i < strlist.length; i++) {
    answer.push(strlist[i].length);
  }
  return answer;
}
console.log(solution(["We", "are", "the", "world!"]));

//다른 풀이

/*

map함수 쓰기(배열 돌면서 특정행위 하기 때문)
:배열을 처리해서 새로운 배열로 반환하기 위한 함수
:배열을 순회하며 지정된 콜백 함수를 적용하여 각 요소를 변환하고, 
그 변환된 값을 모아서 새로운 배열로 반환하는 역할을 수행

forEach() 함수와 비슷함

 */

function solution(strlist) {
  return strlist.map((world) => world.length);
}
