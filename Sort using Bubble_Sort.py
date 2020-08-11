# How to search a given number using Binary Search approach
print('+++++++ Caution: Enter numbers in Ascending +++++++')
print('Enter 10 list of numbers for which you want to sort using Bubble Sort approach:')
list_of_numbers = []
for i in range(10):
    list_of_numbers.append(int(input()))


def sort():
    start_position = 0
    end_position = len(list_of_numbers) - 1

    for start_position in range(end_position, 0, -1):
        for j in range(start_position):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                temp = list_of_numbers[j + 1]
                list_of_numbers[j + 1] = list_of_numbers[j]
                list_of_numbers[j] = temp


sort()
print('numbers in sorted format:', list_of_numbers)
