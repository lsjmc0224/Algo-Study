/*

[글자 이어 붙여 문자열 만들기 ]

<문제 설명>
문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다. my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 
순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

<제한사항>
1 ≤ my_string의 길이 ≤ 1,000
my_string의 원소는 영소문자로 이루어져 있습니다.
1 ≤ index_list의 길이 ≤ 1,000
0 ≤ index_list의 원소 < my_string의 길이

<입출력 예>
my_string	index_list	result
"cvsgiorszzzmrpaqpe"	[16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]	"programmers"
"zpiaz"	[1, 2, 0, 0, 3]	"pizza"

*/

//문제 풀이

function solution(my_string, index_list) {
  const result = index_list.map((a) => my_string[a]).join("");
  return result;
}

//알게 된 것 및 깨달은 것
//처음에는 index_list가 아닌 my_string을 순회하면서 index_list에 맞는 인덱스를 찾아 새로운 배열을 만들려고 했다.(push)
//하지만 index_list를 순회하면서 my_string에 해당하는 인덱스 찾아 map으로 뿌려주면 된다!!
