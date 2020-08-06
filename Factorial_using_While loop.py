# Factorial code using WHILE loop
print('enter the number for the factorial you want:')
i_want_fact_for = int(input())
#print(type(i_want_fact_for))
Fact_value = 1
i =1
while i <= i_want_fact_for:
    #print(i)
    Fact_value = Fact_value * i
    i+=1
    #print(Fact_value)
print('Factorial value of {} is: {}'.format(i_want_fact_for, Fact_value))
# End of Factorial code using WHILE loop