def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    li = [ord(s) for s in "The five boxing wizards jump quickly"]
    return li


# Run the solution with the checker
print(sat(sol()))  # should print: True

if __name__ == "__main__":
    assert sat(sol())
