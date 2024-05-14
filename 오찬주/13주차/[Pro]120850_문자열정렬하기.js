/*

[문자열 정렬하기]

<문제 설명>
문자열 my_string이 매개변수로 주어질 때,
my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

<제한사항>
1 ≤ my_string의 길이 ≤ 100
my_string에는 숫자가 한 개 이상 포함되어 있습니다.
my_string은 영어 소문자 또는 0부터 9까지의 숫자로 이루어져 있습니다. 

<입출력 예 #1>
"hi12392"에 있는 숫자 1, 2, 3, 9, 2를 오름차순 정렬한 [1, 2, 2, 3, 9]를 return 합니다.
*/

function solution(my_string) {
  var answer = [];
  //for...of 반복문: 특정 배열 뽑아낼 때 주로 사용
  for (let i of my_string) {
    //charCodeAt(): 주어진 문자열의 인덱스에 대한 유니코드를 나타내는 0부터 65535 사이의 정수를 반환
    // 58 미만인 것을 찾으면 0부터 9사이의 숫자로 된 문자만 걸러낼 수 있음
    if (i.charCodeAt() < 58) answer.push(Number(i));
  }
  return answer.sort();
}

//다른 풀이

//1.정규식 활용
function solution(my_string) {
  //문자열 my_string을 배열로 변경
  return (
    [...my_string]

      //filter 메서드: 배열의 각 요소에 대해 주어진 함수를 호출하여 조건을 만족하는 요소만을 추출
      //isNaN 함수를 사용하여 숫자가 아닌 요소를 걸러냄(숫자가 아닌 요소는 제거됨)
      //map 메서드:  배열의 각 요소에 대해 주어진 함수를 호출하여 새로운 배열을 생성
      .filter((v) => !isNaN(v))
      .map((v) => parseInt(v))
      //숫자 비교하여 정렬
      .sort((a, b) => a - b)
  );
}

//2번째

function solution(my_string) {
  return (
    my_string

      //.match(/\d/g): 정규 표현식 /d를 사용하여 문자열에서 숫자만을 추출
      // match 메서드는 문자열에서 정규 표현식과 일치하는 부분을 추출하여 배열로 반환
      // 여기서 /d는 숫자에 해당하는 문자 클래스를 나타냄.
      ///g 플래그는 문자열 전체에서 모든 일치 항목을 찾도록 함
      .match(/\d/g)
      //map 메서드를 사용하여 각 숫자 문자열을 숫자로 변환
      .map((v) => Number(v))
      .sort()
  );
}
