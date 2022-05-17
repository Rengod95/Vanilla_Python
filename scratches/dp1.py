import time
n,k = map(int,input().split())
#n 은 행 k는 열
pascal=[1,1]
templist=[]
if (n==1 or n==2 or n==k) or k==1:
    print("1")
    exit()
else:
    start = time.time()
    for count in range(n-2): #행 반복 n-2번
        templist.append(1)
        for _ in range(1,count+3): #열 반복 n번
            if _ == count+2 :
                templist.append(1)
                pascal = templist[:]
                templist = []
                break
            else:
                templist.append(pascal[_-1]+pascal[_])

print(round(time.time()-start,3),'sec\n')
print(pascal[k-1])
    


