def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(8)] and len(set(li)) == 3)

def sol():
    li = [random.randint(1, 100) for _ in range(10)]
    while not sat(li):
        li = [random.randint(1, 100) for _ in range(10)]
    return li

print(sat(sol()))  # It should print True if the solution is correct.

if __name__ == "__main__":
    assert sat(sol())
