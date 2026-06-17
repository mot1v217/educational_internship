n, k = list(map(int, input('n k: ').split(' ')))
P = list(map(int, input('перестановка: ').split(' ')))
word = list(input())
result = word
for i in range(k):
    result = [letter for _, letter in sorted(zip(P, result))]
print("".join(result))