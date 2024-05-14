function solution(arr, queries) {
  queries.forEach(([s, e]) => {
    while (s <= e) arr[s++]++;
  });
  return arr;
}

/*
다른 풀이

function solution(arr, q) {
    q.map((a)=>{
        for(let i = a[0]; i<=a[1]; i++){
            arr[i]+=1;
        }
    })

    return arr;
}
*/
