function solution(num_list, n) {
  // num_list에 n이 포함되어 있는지 확인하고 결과를 반환
  return num_list.includes(n) ? 1 : 0;
}
