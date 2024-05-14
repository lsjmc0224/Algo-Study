function solution(n) {
  const arrN = [...n];
  const res = [];

  while (arrN.length !== 0) {
    res.push(arrN.splice(0, 5)[0]);
  }

  return res;
}

// 다른 사람 풀이
/*
const solution = (names) => names.filter((v, idx) => idx % 5 === 0);

filter()를 사용해서 풀었음
해당 배열에서, index를 5로 나눴을 때 나머지가 0인 index에 해당하는 요소들만 반환하는 것
그럼 자동으로 index 0번 5번 10번 15번 ... 의 요소들이 뽑힘.

filter()메서드는 애초에 새 배열을 만들어 반환해주기 때문에, 원 배열에 영향을 주지 않는다.

*/
