function solution(myString) {
    var answer = '';
    let al = "abcdefghijklmnopqrstuvwxyz";

    for (let i of myString) {
        if (al.indexOf(i) < al.indexOf("l")) {
            answer += "l";
        } else {
            answer += i;
        }
    }

    return answer;
}