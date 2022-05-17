
n = int(input())
total = [0, True,False,True,True] + [0]*(n-4)

for _ in range(5,n+1):
    if True in [total[_-1],total[_-3],total[_-4]]:
        total[_]= True
    else:
        total[_]=False

if total[n]:
    print("SK")
else:
    print("CY")

