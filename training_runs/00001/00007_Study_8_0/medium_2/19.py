def sat(ls, idx1=1234, idx2=1235):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    return 1234567890

# Testing the solution
print(sat(list(map(str, [1,2,3,4,5,6,7,8,9,0]))))  # This should print: False
print(sat(list(map(str, [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]))))  # This should print: True

if __name__ == "__main__":
    assert sat(sol())
