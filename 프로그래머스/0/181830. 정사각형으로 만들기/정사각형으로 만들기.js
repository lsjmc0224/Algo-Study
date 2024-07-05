function solution(arr) {
    const rows = arr.length;
    const cols = arr[0].length;
    const max = Math.max(rows, cols);

    // 행의 수가 더 많으면 각 행의 끝에 0을 추가
    if (rows > cols) {
        for (let i = 0; i < rows; i++) {
            while (arr[i].length < max) {
                arr[i].push(0);
            }
        }
    } 
    // 열의 수가 더 많으면 각 열의 끝에 0을 추가
    else if (cols > rows) {
        for (let i = rows; i < max; i++) {
            arr.push(Array(max).fill(0));
        }
    }

    return arr;
}