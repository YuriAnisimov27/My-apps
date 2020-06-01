import datetime

def maxNumber(numbers):
    if len(numbers) == 0:
        return
    else:
        a = numbers[0]
        for i in numbers:
            if a < i:
                a = i
        return a


def morethenK(numbers, k):
    result = []
    for i in numbers:
        if i > k:
            result.append(i)
    return result


l = [1, 234, 34, 43, 43, 34, 43, 4]
l1 = []
print(maxNumber(l1))
print(morethenK(l, 34))


user = {
    'name': 'Jack',
    'surname': 'Jones',
    'age': 28
}
print(datetime.date.today())