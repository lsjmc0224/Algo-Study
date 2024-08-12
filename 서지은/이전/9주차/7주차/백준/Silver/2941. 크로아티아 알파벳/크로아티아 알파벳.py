arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
  
for i in arr:
    word = word.replace(i, '*') #해당하는 단어를 *로 바꿈
        
print(len(word)) #