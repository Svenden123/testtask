def search_pairs(array, k):
    result = []
    for i in range(len(array)):
        for j in array[i:]:
            if array[i] + j == k and (array[i], j) not in result and (j, array[i]) not in result:
                result.append((array[i], j))
    return result


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))



file = open('names.txt', 'r', encoding='utf-8')
names = sorted([name[1:-1] for name in file.read().split(',')])
names = [(name, sum([ord(char) - 64 for char in name])) for name in names]
products = [names[i][1] * (i + 1) for i in range(len(names))]
print(sum(products))



def get_zeros(n):
    current = 1
    zeros = 0
    for i in range(1, n + 1):
        current *= i
        next = ''
        for j in str(current)[::-1]:
            if not next and j == '0':
                zeros += 1
            elif j != '0':
                next += j
            else:
                break
        current = int(next[::-1])
    return zeros


print(get_zeros(5))
print(get_zeros(12))