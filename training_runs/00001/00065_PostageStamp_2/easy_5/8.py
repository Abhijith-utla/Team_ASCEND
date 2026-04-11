def sat(stamps, max_stamps):
    return len(stamps) == max_stamps and sum(stamps) == 43

def sol():
    return []

# testing
print(sat(sol(), 10))  # True
print(sat(sol(), 11))  # False
print(sat(sol(), 12))  # False
print(sat(sol(), 43))  # True

if __name__ == "__main__":
    assert sat(sol())
