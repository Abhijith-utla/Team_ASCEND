def sat(s: str):
    return str(8 ** 2888).count(s) > 8 and len(s) == 3

def sol():
    ans = []
    s = '8' * 2888
    ans.append(str(s.count('8') > 8 and len(s) == 3))
    s = '1' * 2888
    ans.append(str(s.count('1') > 8 and len(s) == 3))
    s = '0' * 2888
    ans.append(str(s.count('0') > 8 and len(s) == 3))
    return ans

# Test cases
assert sol() == ['True', 'True', 'True']

if __name__ == "__main__":
    assert sat(sol())
