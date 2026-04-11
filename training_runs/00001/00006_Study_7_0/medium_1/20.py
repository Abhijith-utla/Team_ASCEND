def sat(s: str):
    return str(int(8 ** 2888)).count(s) > 8 and len(s) == 3

def sol():
    count = 0
    for i in range(2888):
        count += str(8 ** i).count('1')
    return count > 8 and len('{0:b}'.format(count)) == 3

if __name__ == "__main__":
    assert sat(sol())
