def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return {
        'answer': sat(['abcd', 'efgh', 'ijkl', 'mnop', 'abcd'])
    }

if __name__ == "__main__":
    assert sat(sol())
