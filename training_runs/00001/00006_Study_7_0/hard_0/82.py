def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    return '888'

# This function will always return '888' as the answer.

if __name__ == "__main__":
    assert sat(sol())
