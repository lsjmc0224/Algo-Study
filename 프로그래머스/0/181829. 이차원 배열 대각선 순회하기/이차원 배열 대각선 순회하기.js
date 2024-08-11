function solution(board, k) {
    let answer = 0;
    const n = board.length;
    const m = board[0].length;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m && i + j <= k; j++) {
            answer += board[i][j];
        }
    }

    return answer;
}