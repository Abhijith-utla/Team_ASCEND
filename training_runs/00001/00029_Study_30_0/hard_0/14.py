def sat(li: List[int]):
    return all([123 * li[i] % 1000 < 123 * li[i + 1] % 1000 and li[i] in range(1000) for i in range(20)])

def sol():
    return []

# Add your solution here

if __name__ == "__main__":
    assert sat(sol())
