/*

[문제 설명]
정수로 이루어진 리스트 num_list가 주어집니다. 
num_list에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

*/

//문제 풀이
function solution(num_list) {
  //sort 활용해서 오름차순 정렬 후 5개 자르기
  return num_list.sort((a, b) => a - b).slice(5);
}
