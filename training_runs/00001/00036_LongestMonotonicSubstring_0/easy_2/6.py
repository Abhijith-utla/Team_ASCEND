def sat(x: List[int], length=13):
    return all(x[i] <= x[i + 1] for i in range(length - 1))

def sol():
    return [i for i in range(13) if i % 2 == 0]

print(sol())

if __name__ == "__main__":
    assert sat(sol())
