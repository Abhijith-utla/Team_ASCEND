def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(1, len(li) + 1))

def sol():
    return {
        "sum": sum(range(10)),
        "max": max(range(10)),
        "min": min(range(10)),
        "average": sum(range(10)) / 10,
        "product": reduce(lambda x, y: x * y, range(10))
    }

if __name__ == "__main__":
    assert sat(sol())
