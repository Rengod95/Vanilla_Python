listcount, standard_sum= map(int, input().split())

end_P, interval_sum, sumcount = 0, 0, 0

num_list = list(map(int, input().split()))

for start in range(listcount):
    
    while end_P < listcount and standard_sum > interval_sum:
        interval_sum += num_list[end_P]
        end_P += 1

    if standard_sum == interval_sum:
        sumcount += 1
    interval_sum -= num_list[start]
        
print(sumcount)