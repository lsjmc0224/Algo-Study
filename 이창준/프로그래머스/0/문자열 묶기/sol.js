function solution(strArr) {
  const mappingTable = {};

  // strArr에서 가장 길이가 긴문자열의 길이
  const max_len = Math.max(...strArr.map((item) => item.length));

  // 1 ~ max_len까지 filter를 걸러서 해당 문자열길이에 해당하는 문자열이 몇개있는가 mappingTable에 저장
  for (let i = 1; i <= max_len; i++) {
    const data = strArr.filter((item) => item.length === i);

    mappingTable[i] = data.length;
  }

  // values 배열이 나오면 가장큰거 return 하면됩니다.
  return Math.max(...Object.values(mappingTable));
}
