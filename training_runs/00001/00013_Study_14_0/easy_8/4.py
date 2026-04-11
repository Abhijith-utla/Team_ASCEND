def sat(li: List[int]):
    return all([i == li[j] + li[j+1] for i in range(len(li))])

def sol():
    return [1, 2, 3, 4, 5]

if __name__ == "__main__":
    assert sat(sol())
