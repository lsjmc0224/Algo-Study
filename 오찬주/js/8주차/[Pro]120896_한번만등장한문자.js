/*

[한 번만 등장한 문자]

<문제 설명>
문자열 s가 매개변수로 주어집니다. 
s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 
solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

<제한사항>
0 < s의 길이 < 1,000
s는 소문자로만 이루어져 있습니다.


*/

/*

[문제 풀이]

- 문자열을 쪼개주기 
- 쪼갠 문자열을 반복 순회하며 같은 문자가 있는지 찾기
- 있으면 배열에 추가
- 사전 순으로 정렬 후 문자열로 합치기

*/

function solution(s) {
  //결과 저장할 곳 배열로 선언
  var answer = [];

  //문자열 쪼개기

  var arr = s.split();

  //item을 반복 순회하며 처음 발견한 위치와 마지막으로 발견한 위치가 같다면, 즉 발견을 한번만 했다면 결과에 추가

  arr.forEach((item) => {
    if (s.indexOf() == s.lastIndexOf()) {
      answer.push(item);
    }
  });

  return answer.sort().join("");
}
