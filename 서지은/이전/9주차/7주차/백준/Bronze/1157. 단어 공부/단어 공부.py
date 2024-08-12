word = input().lower() #애초에 전부 소문자로 변환
word_list = list(set(word)) #단어를 한 글자씩 뜯어서 리스트에 저장
cnt = []

for i in word_list:
    count = word.count(i) #그 전에 들어온 문자가 몇 번 있었는 지 count로 세주는 거
    cnt.append(count)
#만약 가장 많이 사용된 알파벳이 여러 개일 경우
if cnt.count(max(cnt)) >=2 :
    print("?")
else :
    print(word_list[(cnt.index(max(cnt)))].upper())
    