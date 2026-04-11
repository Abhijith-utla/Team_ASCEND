def sat(s: str):
    return s.count('yy') == 100 and s.count('yo') == 101 and s.count('y') == 98

def sol():
    return {
        "result": "success" if sat("yyyyyyyyyyyoyoyo") else "failure",
        "count_yy": "yyyyyyyyyyyyyy",
        "count_yo": "yyyyyyyyyyyoyo"
    }

def sat(s: str):
    return s.count('yy') == 100 and s.count('yo') == 101 and s.count('y') == 98

if __name__ == "__main__":
    assert sat(sol())
