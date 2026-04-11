def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    def sat(li: List[int]):
        return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

    def gen():
        # Generate a list with a permutation of integers from 0 to 998
        li = [i % 1000 for i in range(999)]

        # Shuffle the list to make it unsorted
        for i in range(len(li) - 1, 0, -1):
            j = random.randint(0, i)
            li[i], li[j] = li[j], li[i]

        return li

    solution = gen()

    while not sat(solution):
        # If the solution is not correct, try another permutation
        solution = gen()

    return solution

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
