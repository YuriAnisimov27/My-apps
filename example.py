# https://repl.it/@Levashov/test


def max_number(numbers):
    if len(numbers) == 0:
        return

    m = numbers[0]

    for number in numbers:
        if number > m:
            m = number

    return m


print(max_number([1, 3, 2, 1024, 3, 453, 42, 31, 3, 32]))
print(max_number([6, 3, 453, 42, 31, 3, 32]))
print(max_number([]))


def more_then_k(numbers, k):
    result = []

    for number in numbers:
        if number > k:
            result.append(number)

    return result


print(more_then_k([1, 3, 2, 1024, 3, 453, 42, 31, 3, 32], 31))
print(more_then_k([6, 3, 453, 42, 31, 3, 32], 31))


user = {
    'name': 'Jack',
    'surname': 'Black',
    'age': 50
}
# user['age']
