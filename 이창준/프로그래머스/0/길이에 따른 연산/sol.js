function solution(num_list) {
  var answer = 0;
  if (num_list.length >= 11) {
    for (const array of num_list) {
      answer += array;
    }
  } else if (num_list.length <= 10) {
    answer = num_list.reduce((a, b) => a * b);
  }
  return answer;
}

/*
다른 사람 풀이
  [0, 1, 2, 3, 4].reduce(function(accumulator, currentValue, currentIndex, array) {
  return accumulator + currentValue;
});
  

*/
