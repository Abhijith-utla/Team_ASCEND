def sat(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

def sol() -> List[int]:
    result = []
    for i in range(20):
        if sum(result) + 2 ** i - 1 > 2 ** i:
            break
        result.append(2 ** i - 1)
    return result

# Checker
def sat(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

if __name__ == "__main__":
    assert sat(sol())
