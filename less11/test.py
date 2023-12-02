from homework import task_collatza

print(task_collatza(837799))
print(task_collatza(997823))

a = 0
# num = 837799
num = 997823
while num != 1:

    if num % 2 == 0:
        num = num / 2
    else:
        num = num * 3 + 1
    a += 1

print(a)
