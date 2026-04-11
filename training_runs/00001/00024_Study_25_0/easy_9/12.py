def sat(s: str) -> bool:
    return sorted(s) == sorted('Auipenmtrs') and s == s[::-1]

def sol():
    return ''.join(sorted(input('Enter a string: '))) == ''.join(sorted('Auipenmtrs')) and ''.join(sorted(input('Enter a string: '))) == ''.join(sorted('Auipenmtrs')[::-1])

print(sol())

if __name__ == "__main__":
    assert sat(sol())
