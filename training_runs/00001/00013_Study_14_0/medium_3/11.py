def sat(li: List[int]):
    return all([i == sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))])

def sol():
    li = [2, 3, 5, 1, 4]
    return sat(li)

def sat(li: List[int]):
    return all([i == sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))])

if __name__ == "__main__":
    assert sat(sol())
