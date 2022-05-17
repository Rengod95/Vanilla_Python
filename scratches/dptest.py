
m,n = map(int,input().split())
apart = list()
for _ in range(5*m+1):
    apart.append(input())

count1, count2, hashcount= 0, 0,0

windows = [0,0,0,0,0]
indexcount = 1
for i in range (5*m+1): #세로
    if '##' in apart[i] :
        continue
    elif '*' not in apart[i]:
        if hashcount != 1:
            windows[0] = windows[0] +1
            hashcount=1
            continue
    elif '*' in apart[i]:
        count1 =apart[i].count('*')//4
        count2 =apart[i+1].count('*')//4
        if '##' not in apart[i+1]:
            windows[indexcount] = windows[indexcount]+count1-count2
            indexcount +=1
        elif '##' in apart[i+1]:
            windows[4]= windows[4]+count1
            indexcount=1
            hashcount=0

print(*windows)

        
        


