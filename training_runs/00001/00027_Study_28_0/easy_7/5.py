def sat(li):
    for i in li:
        for j in li:
            if abs(i - j) < 10:
                return False
    return len(li) == 100

def sol():
    return {
        'a': [i for i in range(100)],
        'b': [i for i in range(100)],
        'c': [i for i in range(100)],
        'd': [i for i in range(100)],
        'e': [i for i in range(100)],
        'f': [i for i in range(100)],
        'g': [i for i in range(100)],
        'h': [i for i in range(100)],
        'i': [i for i in range(100)],
        'j': [i for i in range(100)]
    }

if __name__ == "__main__":
    assert sat(sol())
