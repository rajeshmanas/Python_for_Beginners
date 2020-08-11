# How to search a given number using Linear Search approach
print('Enter 10 list of numbers from which you want to perform Linear Search:')
list_of_numbers = []
for i in range(10):
    list_of_numbers.append(int(input()))
print('Enter the number you want to search:')
search_num = int(input())


def search():
    for i in range(10):
        if list_of_numbers[i] == search_num:
            return True


if search():
    print('found')
else:
    print('Not found')
