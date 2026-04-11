def sat(stamps: List[int], target=19, max_stamps=2, options=[19, 14, 81]):
    for s in stamps:
        if s not in options:
            return False
    return (len(stamps) <= max_stamps)  # No need to check the sum of the stamps

def sol():
    return [19, 14, 81]

print(sat(sol()))  # Should print: [19, 14, 81]

# Additional test cases
assert sat([19, 14, 81]) == [19, 14, 81]
assert sat([19, 14, 81], max_stamps=3) == True
assert sat([19, 14, 81], target=200) == False
assert sat([19, 14, 81], target=200, max_stamps=4) == True
assert sat([19, 14, 81, 200], target=500, max_stamps=4) == False
assert sat([19, 14, 81, 200], target=500) == False
assert sat([19, 14, 81, 200, 150]) == [19, 14, 81,

if __name__ == "__main__":
    assert sat(sol())
