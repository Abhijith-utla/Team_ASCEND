def sat(li):
    return li[li[0]] == li[li[1]] and li[li[1]] != li[li[2]] and li[li[2]] != li[li[0]]

def sol():
    return [1, 2, 3]

print(sat(sol()))  # should return True
print(sat(sol()))  # should return False

if __name__ == "__main__":
    assert sat(sol())
