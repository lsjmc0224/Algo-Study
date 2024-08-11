function solution(n) {
    // n x n 크기의 배열을 0으로 초기화
    const arr = Array.from({ length: n }, () => Array(n).fill(0));

    // 대각선 요소를 1로 변경
    for (let i = 0; i < n; i++) {
        arr[i][i] = 1;
    }

    return arr;
}