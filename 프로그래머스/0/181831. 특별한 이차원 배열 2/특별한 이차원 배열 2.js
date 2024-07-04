function solution(arr) {
    let n = arr.length;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (arr[i][j] !== arr[j][i]) {
                return 0; // 대칭이 아닌 경우 0 반환
            }
        }
    }

    return 1; // 모든 요소가 대칭인 경우 1 반환
}