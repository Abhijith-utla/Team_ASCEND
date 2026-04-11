def sat(ls, idx1=1, idx2=2):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    return [1,2,3,4,5]

print(sat(sol())) # should return True
print(sat(sol(), 1, 3)) # should return True
print(sat(sol(), 1, 4)) # should return False

if __name__ == "__main__":
    assert sat(sol())
