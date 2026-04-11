def sat(li: List[int]):
    return li[li[0]] == li[li[1]] and li[li[2]] != li[li[3]]

def sol():
    arr = [1, 2, 3, 4]
    arr[arr[0]] = arr[arr[1]]
    arr[arr[2]] = arr[arr[3]]
    return arr

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())
