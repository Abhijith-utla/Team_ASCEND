def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def is_even(n: int) -> bool:
        return n % 2 == 0

    def is_odd(n: int) -> bool:
        return n % 2 == 1

    max_digit = '9' if is_even(len(str(8 ** 1818))) else '8'
    middle_digits = ''.join([max_digit] * ((len(str(8 ** 1818)) - 2) // 2))
    result = '8' + middle_digits + '8'
    result = int(result) ** 1818

    return str(result) == str(8 ** 1818) and is_palindrome(str(result)) and len(str(result)) > 11

if __name__ == "__main__":
    assert sat(sol())
