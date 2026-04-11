def sat(s: str):
    return str(int(8 ** 2888) ** 0.5).count(s) > 8 and len(s) == 3

def sol():
    result = int(8 ** 2888) ** 0.5
    result = round(result, 10)
    result = str(result).replace('.', '')
    return result.count('8') > 8 and len(result) == 3

if __name__ == "__main__":
    assert sat(sol())
