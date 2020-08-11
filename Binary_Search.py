# How to search a given number using Binary Search approach
print('+++++++ Caution: Enter numbers in Ascending +++++++')
print('Enter 10 list of numbers for which you want to perform Binary Search in Ascending Order:')
list_of_numbers = []
for i in range(10):
    list_of_numbers.append(int(input()))
print('Enter the number you want to search:')
search_num = int(input())


def search():
    start_position = 0
    end_position = len(list_of_numbers) - 1
    while start_position <= end_position:
        mid_position = (start_position + end_position) // 2
        if search_num == list_of_numbers[mid_position]:
            return True
        else:
            if search_num < list_of_numbers[mid_position]:
                end_position = mid_position - 1
            elif search_num > list_of_numbers[mid_position]:
                start_position = mid_position + 1


if search():
    print('found')
else:
    print('Not found')
