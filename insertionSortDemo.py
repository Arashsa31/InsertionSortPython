def print_pass(data, pass_number, index):
    label = f'after pass {pass_number}: '
    print(label, end='')

    print(' '.join(str(d) for d in data[:index]), end=' ' if index != 0 else '')
    print(f'{data[index]}* ', end='')

    print(' '.join(str(d) for d in data[index + 1:len(data)]))

    print(f'{" " * len(label)}{"-- " * pass_number}')


def insertion_sort(data):
    for next in range(1, len(data)):
        insert = data[next]
        move_item = next

        while move_item > 0 and data[move_item - 1] > insert:
            data[move_item] = data[move_item - 1]
            move_item -= 1

            data[move_item] = insert
            print_pass(data, next, move_item)

def main():
    data = [35, 73, 90, 65, 23, 86, 43, 81, 34, 58]
    print(f'Unsorted array: {data}\n')
    insertion_sort(data)
    print(f'\nSorted array: {data}\n')

if __name__ == '__main__':
    main()