def sat(x: List[int], length=61, s=" OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return []

# Incorrect solution
def sol_incorrect():
    x = [0, 1, 2]
    s = " OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"
    return [s[i] for i in x]

# Correct solution
def sol_correct():
    x = [0, 1, 2, 3, 4, 5]
    s = " OW##P%T'UW)X+X-YY]^_`bd/044e5egk7lm779:<m?D@ADnnpDEFIpNNOqqwxx"
    return [s[i] for i in x]

print(sat(sol_correct()))
assert sat(sol_correct())

# Incorrect solution
def sol_incorrect():
    x = [0, 3, 2, 5, 4

if __name__ == "__main__":
    assert sat(sol())
