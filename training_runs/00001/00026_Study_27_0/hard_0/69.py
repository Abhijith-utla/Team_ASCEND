def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def sol():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    li[li[0]], li[li[1]] = li[li[1]], li[li[0]]
    return li

def main():
    assert sat(sol())

if __name__ == "__main__":
    main()

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    assert sat(sol())
