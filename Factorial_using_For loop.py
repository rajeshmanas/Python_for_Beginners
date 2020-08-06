# Factorial code using FOR loop
print('enter the number for the factorial you want:')
i_want_fact_for = int(input())
#print(type(i_want_fact_for))
Fact_value = 1
for i in range(1,i_want_fact_for+1):
    #print(i)
    Fact_value = Fact_value * i
    #print(Fact_value)
print('Factorial value of {} is: {}'.format(i_want_fact_for,Fact_value))
# End of Factorial code using FOR loop