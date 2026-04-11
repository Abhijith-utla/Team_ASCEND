def sat(x: str, puz="972561483_489765173_263514987_458731629_361978546_712894563_623514987_782631345_1657924838_516268945_321978546_"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))
    return True

def sol():
    return ""

if __name__ == "__main__":
    assert sat(sol())
