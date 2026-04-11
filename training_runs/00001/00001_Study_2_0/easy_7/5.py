def sat(s: str):
    return s.count('a') == 200 and s.count('aa') == 201 and s.count('aaa') == 198

def sol():
    return {
        'answer': 'Yes' if 200*'a' + 201*'aa' + 198*'aaa' == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' else 'No'
    }

if __name__ == "__main__":
    assert sat(sol())
