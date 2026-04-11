def sat(x: List[int], length=61, s=" OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"):
    return all(s[x[i]] <= s[x[i + 1]] for i in range(length - 1))

def sol():
    x = [6, 1, 3, 2, 4, 5, 0]
    length = 7
    s = " OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"
    return x, length, s

# Test the function with the given inputs
print(sat(sol()[0], sol()[1], sol()[2]))  # Expected output: True

if __name__ == "__main__":
    assert sat(sol())
