def sat(ls, idx1=1, idx2=2):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol(ls):
    for idx1 in range(len(ls)):
        for idx2 in range(idx1 + 1, len(ls)):
            if sat(ls, idx1, idx2):
                return True
    return False

def sat(ls, idx1=1, idx2=2):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

# Testing
ls = [1, 2, 3, 4, 5, 6]
print(sol(ls))  # False

ls = [1, 1, 2, 3, 4, 5]
print(sol(ls))  # True

ls = [1, 2, 3, 4, 5, 4]
print(sol(ls))  # True

ls = [1, 2, 3, 4, 5, 6]
print(sol(ls))  # False

if __name__ == "__main__":
    assert sat(sol())
