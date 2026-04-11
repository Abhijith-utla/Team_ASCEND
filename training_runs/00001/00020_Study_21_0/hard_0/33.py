def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    import random
    random_list = [random.randint(1, 10) for _ in range(10)]
    while not sat(random_list):
        random_list = [random.randint(1, 10) for _ in range(10)]
    return random_list

def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

# Testing the solution
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
