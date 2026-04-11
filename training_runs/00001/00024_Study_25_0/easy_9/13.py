def sat(s: str) -> bool:
    return sorted(s) == sorted('Auipenmtrs') and s == s[::-1]

def sol():
    return ''.join(sorted(s)) == ''.join(sorted('Auipenmtrs')) and ''.join(sorted(s)) == ''.join(sorted('Auipenmtrs')[::-1])

if __name__ == "__main__":
    assert sat(sol())
