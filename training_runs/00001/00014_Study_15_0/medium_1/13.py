def sat(li: List[int]):
    return all(x + 1 == (2 ** x) - 1 for x in range(20))

def sol():
    return {
        'answer': int((2 ** 20) - 1)
    }

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
