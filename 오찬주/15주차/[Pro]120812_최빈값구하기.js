/*
[최빈값 구하기]

<문제 설명>
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 
최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

<제한사항>
0 < array의 길이 < 100
0 ≤ array의 원소 < 1000

*/

//최빈값을 return, 만약 최빈값이 여러 개면 -1을 return
//1. 각 원소의 개수를 세기
//2. 각 원소의 개수 비교
//3. 가장 많이 나온 숫자 개수 비교
//4. 비교 후 개수가 유일하다? 그 원소 return
//5. 만약 최빈값이 동일한 것이 2개 이상이면 -1

function solution(array) {
  let maxCount = 0; // 최대 개수
  let mode = 0; // 최빈값
  let isOne = true; // 최빈값이 유일한지

  // 각 원소의 개수를 세기 위한 객체
  let counts = {};

  // 각 원소의 개수를 세기
  array.forEach((element) => {
    counts[element] = (counts[element] || 0) + 1;
  });

  console.log(counts);

  // 최빈값 찾기
  Object.keys(counts).forEach((key) => {
    if (counts[key] > maxCount) {
      maxCount = counts[key];
      //js에서 key는 기본적으로 문자열로 저장되기에 정수형으로 변형해줘야 함
      mode = parseInt(key);
      isOne = true;
    } else if (counts[key] === maxCount) {
      isOne = false;
    }
  });

  return isOne ? mode : -1;
}

let array = [1, 2, 4, 3, 3, 3, 5, 5, 5];
console.log(solution(array)); // 출력: 3

//다른 풀이

function solution(array) {
  let m = new Map();
  for (let n of array) m.set(n, (m.get(n) || 0) + 1);
  m = [...m].sort((a, b) => b[1] - a[1]);
  return m.length === 1 || m[0][1] > m[1][1] ? m[0][0] : -1;
}
