/*

[원소들의 합과 곱]

<문제 설명>
정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 
크면 0을 return하도록 solution 함수를 완성해주세요.

<제한사항>
2 ≤ num_list의 길이 ≤ 10
1 ≤ num_list의 원소 ≤ 9

*/

//문제 풀이

function solution(num_list) {
  var multi = 1;
  var plus = 0;

  for (var i = 0; i < num_list.length; i++) {
    multi *= num_list[i];
  }

  for (var i = 0; i < num_list.length; i++) {
    plus += num_list[i];
  }
  plus *= plus;

  if (multi < plus) {
    return 1;
  } else {
    return 0;
  }
}

//주의 사항: 처음에 plus *= plus;를 for문 안에 넣었더니 제대로 답이 나오지 않았다. 처음에 에러 뜨고 코드를 다시 보니 내가 바본가 .. 싶었음
//반복문 안에 plus *= plus;를 넣다니 .. 주의가 필요하다 ..!!

// 다른 풀이 방법

function solution(num_list) {
  let accMul = 1;
  let accSum = 0;
  for (const num of num_list) {
    accMul *= num;
    accSum += num;
  }
  return accMul < accSum ** 2 ? 1 : 0;
}

/*
사실 나와 같은 방식이다. 그런데 코드가 훨씬 알아보기 쉽다.. 더 배워야지
그리고 지수 연산자 ** 를 알게 되었다!! 참고할 것!!

const num of num_list
- for ... of 문법의 일부
- 배열 또는 다른 반복 가능한 객체의 각 요소를 순회(iterate)할 수 있음
- num_list는 배열이고, num은 num_list의 각 요소를 순차적으로 가리킨다.

*/

const num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10];

for (const num of num_list) {
  console.log(num);
}
