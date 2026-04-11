def sat(li: List[int]):
    return all([i == li[j] + li[j+1] for i in range(len(li))])

def sol():
    li = [i for i in range(10)]
    return sat(li)

def sat(li: List[int]):
    return all([i == li[j] + li[j+1] for j in range(len(li)-1)])

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
