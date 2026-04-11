def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol() -> List[int]:
    li = [random.randint(1, 100) for _ in range(10)]  # Generate a random list of 10 integers between 1 and 100
    li[0], li[-1] = li[-1], li[0]  # Swap the first and last elements
    return li

if __name__ == "__main__":
    assert sat(sol())
