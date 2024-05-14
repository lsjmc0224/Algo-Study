function solution(num_list, n) {
  return num_list.filter((_, index) => index % n === 0);
}

// 수정 전 내 코드
/*
function solution(num_list, n) {
  let result = [];

  for (let i = 0; i < num_list.length; i++) {
    if (i % n == 0) {
      result.push(num_list[i]);
    }
  }

  return result;
}
*/
