/*

[k의 개수]

<문제 설명>
1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 
정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록
solution 함수를 완성해주세요.

<제한사항>
1 ≤ i < j ≤ 100,000
0 ≤ k ≤ 9


*/

//문제 풀이

function solution(i, j, k) {
  let arr = [];
  var answer = 0;

  for (let a = i; a <= j; a++) {
    arr.push(a.toString());
  }

  for (let b = 0; b < arr.length; b++) {
    let num = arr[b].split("");

    for (let c = 0; c < num.length; c++) {
      if (Number(num[c]) === k) {
        answer++;
      }
    }
  }

  return answer;
}

//다른 사람 풀이
//k를 기준으로 split해서 여집합 구하기

function solution(i, j, k) {
  let a = "";
  for (i; i <= j; i++) {
    a += i;
  }

  return a.split(k).length - 1;
}
