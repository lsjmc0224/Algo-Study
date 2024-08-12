/*

[배열의 원소 삭제하기]

<문제 설명>
정수 배열 arr과 delete_list가 있습니다. arr의 원소 중
delete_list의 원소를 모두 삭제하고 남은 원소들은 기존의 arr에 있던 순서를 
유지한 배열을 return 하는 solution 함수를 작성해 주세요.

<제한사항>
1 ≤ arr의 길이 ≤ 100
1 ≤ arr의 원소 ≤ 1,000
arr의 원소는 모두 서로 다릅니다.
1 ≤ delete_list의 길이 ≤ 100
1 ≤ delete_list의 원소 ≤ 1,000
delete_list의 원소는 모두 서로 다릅니다.

*/

//문제 풀이

function solution(arr, delete_list) {
  for (var i = 0; i < arr.length; i++) {
    for (var j = 0; j < delete_list.length; j++) {
      if (arr[i] == delete_list[j]) {
        arr.splice(i, 1);
        i--;
      }
    }
  }
  return arr;
}

//주의: 처음에 i--를 안해줘서 .. 계속 틀렸다 ..(눈물)
//배열에서 같은 요소 하나를 발견할 때마다 요소를 삭제한 것이니 arr 배열의 요소도 하나씩 줄어들도록 하는게 중요하다!!

//다른 풀이
//filter로 쓰면 더.. 간단했군 ..

function solution(arr, delete_list) {
  return arr.filter((a) => !delete_list.includes(a));
}
