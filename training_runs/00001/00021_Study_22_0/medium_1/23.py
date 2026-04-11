def sat(s: str) -> bool:
    if len(s) != 10 or not s.isalpha():
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    return "Programming" if sat("Programming") else "Solved"

if __name__ == "__main__":
    answer = sol()
    print(f"The answer is: {answer}")

if __name__ == "__main__":
    assert sat(sol())
