def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    li = [1, 2, 3]
    while not sat(li):
        li[0] += 1
        if li[0] > 3:
            li[0] = 1
            li[1] += 1
            if li[1] > 3:
                li[1] = 1
                li[2] += 1
                if li[2] > 3:
                    li[2] = 1
    return li

def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

# Testing
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())
