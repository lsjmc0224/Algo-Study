/*

[문제 설명]
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

[제한사항]
1 ≤ n ≤ 10,000
1 ≤ numlist의 원소 ≤ 10,000
1 ≤ numlist의 길이 ≤ 100
numlist는 중복된 원소를 갖지 않습니다.

[입출력 예 설명]
입출력 예 #1

4에서 가까운 순으로 [4, 5, 3, 6, 2, 1]을 return합니다.
3과 5는 거리가 같으므로 더 큰 5가 앞에 와야 합니다.
2와 6은 거리가 같으므로 더 큰 6이 앞에 와야 합니다.
*/

//n으로부터 가까운 수 정렬
function solution(numlist, n) {
  return numlist.sort((a, b) => {
    const num1 = Math.abs(a - n);
    const num2 = Math.abs(b - n);

    if (num1 === num2) return b - a;
    return num1 - num2;
  });
}

numlist = [1, 2, 3, 4, 5, 6];
let n = 4;
console.log(solution(numlist, n));

//다른 풀이

function solution(numlist, n) {
  return numlist.sort((a, b) => Math.abs(a - n) - Math.abs(b - n) || b - a);
}
