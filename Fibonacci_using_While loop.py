# Fibonacci Series using WHILE loop
print('enter how many Fibonacci series numbers you want to see:')
i_want_fibonacci_count = int(input())
i = 1
j = 1
count = 0
while count <= i_want_fibonacci_count:
    if count == 0:
        print(i)
        continue
    if count == 1:
        print(j)
        continue
    k = i + j
    i = j
    j = k
    count+= 1
    print(j)
# END of Fibonacci Series using WHILE loop