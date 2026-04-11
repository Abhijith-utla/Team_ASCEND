def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return {
        "answer": bool(sat([
            "abcdefg", 
            "bcdefgh", 
            "cdefghi", 
            "defghij", 
            "efghijk", 
            "fghijkl", 
            "ghijklm", 
            "hijklmn", 
            "ijklmno", 
            "jklmnop", 
            "klmnopq", 
            "lmnopqr", 
            "mnopqrs", 
            "nopqrst", 
            "opqrstu", 
            "pqrstuv", 
            "qrstuvw", 
            "rstuvwx", 
            "stuvwxy", 
            "tuvwxyz"
        ]))
    }

if __name__ == "__main__":
    assert sat(sol())
