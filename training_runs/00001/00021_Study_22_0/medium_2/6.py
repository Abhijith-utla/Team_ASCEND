def sat(s: str) -> bool:
    if len(s) != 20:
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

def sol():
    s = 'abcde'  # This should be replaced with the actual string from user input
    return sat(s)

# This is used to validate the function with the given string
def main():
    user_input = input("Enter a string: ")
    assert sat(user_input)
    print("The string satisfies the condition.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    assert sat(sol())
