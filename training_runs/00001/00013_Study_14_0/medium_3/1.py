def sat(li: List[int]):
    return all([i == sum(li[j] for j in range(i+1, len(li))) for i in range(len(li))])

def sol():
    return True

# The function `sat` is already defined by the user.
# We don't need to define another function named `sol`.

if __name__ == "__main__":
    assert sat(sol())
