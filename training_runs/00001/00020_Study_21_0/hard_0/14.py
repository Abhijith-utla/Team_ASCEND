def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    li = [1, 2, 2, 3, 3, 4, 5, 6, 6, 7]
    return li

# This function checks whether the given list contains 3 unique elements.
def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

# This function calls the above function and prints the output.
def main():
    li = sol()
    assert sat(li)
    print(li)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    assert sat(sol())
