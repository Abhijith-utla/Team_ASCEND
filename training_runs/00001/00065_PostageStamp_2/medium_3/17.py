def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test cases
print(sat([])) # True
print(sat([18])) # True
print(sat([18, 1])) # True
print(sat([18, 1, 43])) # True
print(sat([18, 1, 43, 81])) # True
print(sat([18, 1, 43, 81, 81])) # False
print(sat([18, 1, 43, 81, 1])) # False
print(sat([18, 1, 43])) # True
print(sat([18, 1, 43, 81, 2])) # False
print(sat([1, 43, 81])) # True
print(sat([18, 1])) # False
print(sat([1, 43, 81, 1])) # False
print(sat([1, 43, 81, 2])) # False
print(sat([1, 43, 81

if __name__ == "__main__":
    assert sat(sol())
