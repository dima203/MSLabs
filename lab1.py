from copy import copy


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


def get_math_expectation(sequence, count: int) -> float:
    return sum(sequence) / count


def get_dispersion(sequence, count: int, math_expectation: float) -> float:
    return sum(map(lambda x: (x - math_expectation) ** 2, sequence)) / (count - 1)


if __name__ == '__main__':
    x0 = float(input('> '))
    count = int(input('> '))
    generator = random(x0)
    try:
        s = 0
        for i, num in enumerate(random(x0, count)):
            print(f'{i+1}: {num}')
            s += num
    except StopIteration:
        pass

    print(math_expectation := get_math_expectation(random(x0, count), count))
    print(dispersion := get_dispersion(random(x0, count), count, math_expectation))
    print(dispersion ** 0.5)

    a, b = map(float, input('> ').split())
    count = int(input('> '))
    try:
        s = 0
        for i, num in enumerate(random_range(x0, a, b, count)):
            print(f'{i+1}: {num}')
            s += num
    except StopIteration:
        pass

    print(math_expectation := s / count)
    print(dispersion := sum(map(lambda x: (x - math_expectation) ** 2, random_range(x0, a, b, count))) / count)
    print(dispersion ** 0.5)
