def sat(li: List[int]):
    return all([i == sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))])

def sol():
    li = [1, 2, 3, 4, 5]
    if sat(li):
        return True
    else:
        return False

def sat(li: List[int]):
    return all([i == sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))])

if __name__ == "__main__":
    assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
