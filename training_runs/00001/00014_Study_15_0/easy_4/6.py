def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

def sol() -> int:
    return 4

# Call the solution function and assert its result
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
