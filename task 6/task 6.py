n = int(input())
results = []

for _ in range(n):
    a, b, x, y = map(int, input().split())
    pairs = 0
    # сначала берём b с первым типом
    pairs_with_b = min(b, x)
    pairs += pairs_with_b
    b -= pairs_with_b
    # оставшиеся после первого типа b
    x -= pairs_with_b
    #добираем пары через a и остальные типы моторов
    pairs += min(a, x + y)
    results.append(str(pairs))

print(' '.join(results))