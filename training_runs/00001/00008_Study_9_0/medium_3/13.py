def sat(li: List[int]):
    return [chr(i) for i in li] == list(
        "The quick brown fox jumps over the lazy dog".replace(" ", ""))

def sol():
    return chr(120) == chr(118) == chr(105) == chr(108) == chr(101) == 'q' and chr(111) == chr(108) == chr(108) == chr(111) == 'u' and chr(65) == 'T' and chr(97) == 'B' and chr(114) == 'R' and chr(101) == 'F' and chr(114) == 'O' and chr(111) == 'X' and chr(33) == ' '

if __name__ == "__main__":
    assert sat(sol())
