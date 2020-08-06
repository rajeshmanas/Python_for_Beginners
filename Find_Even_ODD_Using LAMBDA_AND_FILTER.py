print('For how many numbers you want to count Even and ODD:')
no_of_elements = int(input())
print('Enter the numbers:')
list_of_elements = []
for i in range(no_of_elements):
    list_of_elements.append(int(input()))

even_number = list(filter(lambda n: n % 2 == 0, list_of_elements))
odd_number = list(filter(lambda n: n % 2 == 1, list_of_elements))
print('List of Even numbers are:', even_number)
print('List of Odd numbers are:', odd_number)

