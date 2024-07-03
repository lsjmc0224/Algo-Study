function solution(n) {
    // n x n 크기의 배열을 0으로 초기화
    let ans = Array.from({ length: n }, () => Array(n).fill(0));

    let rowMin = 0, rowMax = n - 1;
    let colMin = 0, colMax = n - 1;
    let num = 1;

    while (rowMin <= rowMax && colMin <= colMax) {
        // 왼쪽에서 오른쪽으로
        for (let col = colMin; col <= colMax; col++) {
            ans[rowMin][col] = num++;
        }
        rowMin++;

        // 위에서 아래로
        for (let row = rowMin; row <= rowMax; row++) {
            ans[row][colMax] = num++;
        }
        colMax--;

        // 오른쪽에서 왼쪽으로
        if (rowMin <= rowMax) {
            for (let col = colMax; col >= colMin; col--) {
                ans[rowMax][col] = num++;
            }
            rowMax--;
        }

        // 아래에서 위로
        if (colMin <= colMax) {
            for (let row = rowMax; row >= rowMin; row--) {
                ans[row][colMin] = num++;
            }
            colMin++;
        }
    }

    return ans;
}