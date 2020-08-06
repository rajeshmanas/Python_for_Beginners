# Fibonacci Series using FOR loop
print('enter how many Fibonacci series numbers you want to see:')
i_want_fibonacci_count = int(input())
i = 1
j = 1
for count in range(i_want_fibonacci_count):
    #print('count is', count)
    if count == 0:
        print(i)
        continue
    if count == 1:
        print(j)
        continue
    k = i + j
    i = j
    j = k
    print(j)
# END of Fibonacci Series using FOR loop