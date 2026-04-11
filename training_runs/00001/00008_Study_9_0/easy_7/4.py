def sat(li: List[int]):
    return [chr(i) for i in li] == list("The quick brown fox jumps over the lazy dog".replace(" ", ""))

def sol():
    return "".join(chr(i) for i in range(32, 127)) == "The quick brown fox jumps over the lazy dog"

def main():
    assert sat(sol)

main()

if __name__ == "__main__":
    assert sat(sol())
