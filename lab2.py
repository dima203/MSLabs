from lab1 import random, random_range


def get_X(sequence, intervals_count: int) -> float:
    intervals = {
        0 + key * (1 / intervals_count): 0 for key in range(intervals_count)
    }

    try:
        for num in sequence:
            insert_key = 0
            for key in intervals:
                if num > key:
                    insert_key = key
                else:
                    break
            intervals[insert_key] += 1
    except StopIteration:
        pass

    p = 1 / intervals_count
    count = sum(intervals.values())
    return sum(map(lambda m: m ** 2 / p, intervals.values())) / count - count


if __name__ == '__main__':
    print(get_X(random(0.784592, 100), 10))
