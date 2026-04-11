def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    # Assuming ls is a list with at least two elements
    ls = [1, 2, 3, 4, 5]
    idx1 = 1
    idx2 = 3
    value = 2
    return ls[idx1] in ls[idx2] and ls[idx1] != value

print(sol())

if __name__ == "__main__":
    assert sat(sol())
