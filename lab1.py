def random(seed: float = 0.1, count: int = 1):
    x0 = seed
    for _ in range(count):
        n = len(str(x0)[2:]) // 2
        x0 = float(x0) ** 2
        x0 = f'{x0:.{4*n}f}'
        x1 = f'{x0[:2]}{x0[n + 2:3 * n + 2]}'
        x0 = x1
        yield float(x0)


x0 = float(input('> '))
count = int(input('> '))
generator = random(x0)
try:
    for i, num in enumerate(random(x0, count)):
        print(f'{i+1}: {num}')
except StopIteration:
    pass
