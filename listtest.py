#   1  2  3  4  5  6  7  8
#A  1  2  3  4  5  6  7  8
#B  9 10 11 12 13 14 15 16
#C 17 18 19 20 21 22 23 24
#D 25 26 27 28 29 30 31 32
list1=["A","B","C","D"]
list2=["1","2","3","4","5","6","7","8"]
enter=input()
count=1
for i in list1:
    for j in list2:
        if(enter==i+j):
            print(count*8+int(j)-8)
    count+=1
