/*

[가장 큰 수 찾기]

<문제 설명>
정수 배열 array가 매개변수로 주어질 때, 
가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 
solution 함수를 완성해보세요.

<제한사항>
1 ≤ array의 길이 ≤ 100
0 ≤ array 원소 ≤ 1,000
array에 중복된 숫자는 없습니다.


*/

/*

문제 풀이

Math.max()
: 가장 큰 수 찾는 메소드
:배열을 인수로 받지 않기 때문에 ...전개연산자를 사용해 배열을 각각의 값으로 분리해야 한다.

ndexOf()
: 인덱스 찾는 메소드
: array.indexOf(찾고싶은값)의 형태로 사용

*/

function solution(array) {
  return [Math.max(...array), array.indexOf(Math.max(...array))];
}
