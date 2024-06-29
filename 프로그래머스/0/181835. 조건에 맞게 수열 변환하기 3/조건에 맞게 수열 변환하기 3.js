const solution = (arr, k) => {
    // k가 홀수인지 짝수인지 확인
    if (k % 2 === 1) {
        // k가 홀수인 경우, 모든 원소에 k를 곱함
        return arr.map(v => v * k);
    } else {
        // k가 짝수인 경우, 모든 원소에 k를 더함
        return arr.map(v => v + k);
    }
};