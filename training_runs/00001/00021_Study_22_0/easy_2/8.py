def sat(s: str) -> bool:
    return len(s) == 10 and s.isalpha() and '0' not in s and '1' not in s

def sol():
    s = input("Enter a string of 10 alphabetic characters: ")
    while not sat(s):
        s = input("Invalid input. Please enter a string of 10 alphabetic characters: ")
    return s

if __name__ == "__main__":
    assert sat(sol())
