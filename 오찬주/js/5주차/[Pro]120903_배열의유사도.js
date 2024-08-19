/*

[배열의 유사도]

문제 설명
두 배열이 얼마나 유사한지 확인해보려고 합니다. 
문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 
solution 함수를 완성해주세요.

제한사항
1 ≤ s1, s2의 길이 ≤ 100
1 ≤ s1, s2의 원소의 길이 ≤ 10
s1과 s2의 원소는 알파벳 소문자로만 이루어져 있습니다
s1과 s2는 각각 중복된 원소를 갖지 않습니다.


*/

//문제 풀이 1
//반복문 활용하기

function solution(s1, s2) {
  var answer = 0;
  for (var i = 0; i < s1.length; i++) {
    for (var j = 0; j < s2.length; j++) {
      if (s1[i] == s2[j]) answer++;
    }
  }
  return answer;
}

// const s1 = ["a", "b", "c"];
// const s2 = ["com", "b", "d", "p", "c"];

// console.log(solution(s1, s2));

/*

문제풀이2
filter 좀 사용하자!!! 이제 반복문은 그만 써보자

*/

function soluton(s1, s2) {
  const intersection = s1.filter((x) => s2.includes(x));
  return intersection;
}
