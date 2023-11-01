def random(seed: float = 0.1, count: int = 1):
    x0 = seed
    for _ in range(count):
        n = len(str(x0)[2:]) // 2
        x0 = float(x0) ** 2
        x0 = f'{x0:.{4*n}f}'
        x1 = f'{x0[:2]}{x0[n + 2:3 * n + 2]}'
        x0 = x1
        yield float(x0)


def random_range(seed: float = 0.1, a: float = 0, b: float = 1, count: int = 1):
    try:
        for num in random(seed, count):
            yield a + (b - a) * num
    except StopIteration:
        pass


x0 = float(input('> '))
count = int(input('> '))
generator = random(x0)
try:
    for i, num in enumerate(random(x0, count)):
        print(f'{i+1}: {num}')
except StopIteration:
    pass

a, b = map(float, input('> ').split())
count = int(input('> '))
try:
    for i, num in enumerate(random_range(x0, a, b, count)):
        print(f'{i+1}: {num}')
except StopIteration:
    pass
