def sat(li: List[int]):
    return all([i == li[j] + li[j+1] for i in range(len(li))])

def sol():
    return [i == sum(li[j:j+2]) for j in range(len(li))]

# Testing the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
