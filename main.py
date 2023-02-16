numbers = [23, 24, 25, 26, 27, 28, 29, 30, 31]
find = 29
found = False
startIndex = 0
endIndex = len(numbers) - 1

while startIndex <= endIndex:
    midpoint = endIndex + startIndex // 2

    if numbers[midpoint] == find:
        print('Found at', midpoint)
        found = True
        break

    if numbers[midpoint] > find:
        endIndex = midpoint - 1
    else:
        startIndex = midpoint + 1

if not found:
    print('Not found')