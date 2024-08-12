/*

[숨어있는 숫자의 덧셈 1]

<문제 설명>
문자열 my_string이 매개변수로 주어집니다. 
my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

<제한사항>
1 ≤ my_string의 길이 ≤ 1,000
my_string은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.


<입출력 예>
my_string	/ result
"aAb1B2cC34oOp"	/ 10
"1a2b3c4d123"	/ 16


*/

/*

문제 풀이

1. 숫자를 제외한 문자를 찾는다.
2. 찾은 문자를 "" 빈 것으로 바꾸기
3. 숫자를 split 함수를 사용하여 문자 단위로 분할한 후 
배열 numberSplit에 할당
4. numberSplit을 순회하며 정수로 바꿔(parseInt) answer에 더함.

*/

//생각: 이게 맞나 ..? 너무 코드가 더러워지는 느낌...

function solution(my_string) {
  var answer = 0;
  var regex = /[^0-9]/g;
  var numbers = my_string.replace(regex, "");
  const numberSplit = numbers.split("");
  for (var i = 0; i < numberSplit.length; i++) {
    answer += parseInt(numberSplit[i]);
  }
  return answer;
}

//다른 풀이 방법

/*정규식을 사용하는 방법
reduce 함수: 배열의 각 요소를 순회하며 callback 함수의 실행 값을 누적하여 하나의 결과값을 반환

acc: accumulator(누산기)로서, 이전까지의 계산 결과를 나타냄. 
각 요소를 처리할 때마다 누적된 값이 여기에 저장됨

curr: 현재 요소를 나타냄. 배열을 순회하면서 현재 요소가 여기에 전달

.reduce((acc, curr) => acc + Number(curr), 0); 자세한 설명
1. 배열의 각 요소를 순회하면서, 현재 요소를 숫자로 변환한 후 누적된 값(acc)에 더함
2. 초기값이 0이므로 첫 번째 요소부터 시작
3. 순회가 완료되면 누적된 값이 최종 결과가 되어 반환

*/

function solution(my_string) {
  const answer = my_string
    .replace(/[^0-9]/g, "")
    .split("")

    .reduce((acc, curr) => acc + Number(curr), 0);
  return answer;
}
