def sat(x: str, puz="549782631_314869275_972561483___1657924838_736542891_489765173_263514987_712894563_458731629_321978546_564129783_741952683_"):
    assert all(c == "_" or c == s for (c, s) in zip(puz, x))
    return True

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
