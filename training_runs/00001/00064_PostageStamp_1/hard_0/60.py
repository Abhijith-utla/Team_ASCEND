def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# This is to simulate the input provided in the problem
# Please note that this code is not required and can be removed
def input_stamps():
    return [37, 37, 12, 87, 39]

# This is to check if the stamps meet the conditions of the problem
def check_stamps():
    stamps = input_stamps()
    return sat(stamps)

# This is to solve the problem
def sol():
    stamps = input_stamps()
    return stamps

# This is the main block where the program starts
def main():
    if check_stamps():
        print(sol())
    else:
        print("Input stamps do not meet the conditions of the problem.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    assert sat(sol())
