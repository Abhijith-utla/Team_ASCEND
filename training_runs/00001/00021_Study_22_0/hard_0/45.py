def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    s = input("Enter a string: ")
    while not sat(s):
        print("The string is not valid. Please try again.")
        s = input("Enter a string: ")
    return s[::2]

if __name__ == "__main__":
    assert sat(sol())
