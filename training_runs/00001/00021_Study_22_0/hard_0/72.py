def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return {
        'result': str(sum(ord(i) % 2 == 0 for i in 'abcde'))
    }

# Test Case
print(sol())

if __name__ == "__main__":
    assert sat(sol())
