number = 0
sum_all = 0
cub_number = list(range(1,1001,2))
for i in cub_number:
# для  b задания в i надо просто прибавить 17 
    i = i ** 3
    cub_number[number] = i
    sum = 0
    while i != 0:
        sum += i % 10
        i //= 10
    if not sum % 7:
        sum_all += cub_number[number] 
    number+=1
print (sum_all)