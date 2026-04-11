def sat(li: List[int]):
    return all([((123 * li[i] % 1000 < 123 * li[i + 1] % 1000) and (li[i] in range(1000))) for i in range(20)])

def sol():
    return []

Incorrect pattern:
def sol(li: List[int]):
    return []

Incorrect pattern:
def sol(li: List[int]):
    return []

Correct pattern:
def sol():
    return []

Incorrect pattern:
def sol(li: List[int]):
    return []

Correct pattern:
def sol():
    return []

Incorrect pattern:
def sol(li: List[int]):
    return []

Correct pattern:
def sol():
    return []

Incorrect pattern:
def sol(li: List[int]):
    return []

Correct pattern:
def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
