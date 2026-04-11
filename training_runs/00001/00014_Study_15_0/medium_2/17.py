def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

def sol():
    li = [0, 1]
    while True:
        for x in range(20):
            if not sat(li[:x]):
                break
        else:
            return li
        li.append(li[-1] + li[-2])

if __name__ == "__main__":
    assert sat(sol())
