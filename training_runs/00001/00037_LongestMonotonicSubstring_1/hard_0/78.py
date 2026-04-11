def sat(x: List[int], length=193, s="    !!\"\"\"#$$%&&')''((()!))****X**++,,,,---...///0111114445556888::::;s;;<<==,=>>>>ABBBBBCDEEEEEEEFGHIIKKKKLMNOOPPPQQQRRRRASUUUVVVWWXXZZZ[]]]!``aEaabbbccccPcdeeeeefghjjjjkkkllmmooooKpppppqsttwt'$ww=wLwwyyyyzz{"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    x = [4, 0, 2, 3, 1, 5, 6, 7, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    return x

if __name__ == "__main__":
    assert sat(sol())
