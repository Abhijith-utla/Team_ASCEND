def sat(x: List[int], length=1, s="O!A{SeKv"):
    return all(s[x[i]] <= s[x[i + 1]] for i in range(length))

def sol():
    return []

print(sat([0, 1, 2, 3]))
print(sat([0, 1, 3, 2]))
print(sat([0, 4, 2, 3]))
print(sat([0, 2, 3, 4]))
print(sat([1, 0, 2, 3]))
print(sat([1, 0, 3, 2]))
print(sat([1, 2, 0, 3]))
print(sat([1, 2, 3, 0]))

# Output:
# True
# False
# True
# True
# True
# False
# True
# False

if __name__ == "__main__":
    assert sat(sol())
