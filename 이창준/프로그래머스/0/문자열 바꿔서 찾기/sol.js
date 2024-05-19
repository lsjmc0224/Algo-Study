function solution(myString, pat) {
  return myString.includes(
    pat.replaceAll("A", "C").replaceAll("B", "A").replaceAll("C", "B")
  )
    ? 1
    : 0;
}
