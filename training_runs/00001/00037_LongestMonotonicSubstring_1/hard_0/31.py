def sat(x: List[int], length=193, s="    !!\"\"\"#$$%&&')''((()!))****X**++,,,,---...///0111114445556888::::;s;;<<==,=>>>>ABBBBBCDEEEEEEEFGHIIKKKKLMNOOPPPQQQRRRRASUUUVVVWWXXZZZ[]]]!``aEaabbbccccPcdeeeeefghjjjjkkkllmmooooKpppppqsttwt'$ww=wLwwyyyyzz{"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    return [10, 18, 17, 3, 23, 47, 57, 29, 22, 28, 64, 21, 56, 62, 6, 27, 46, 54, 41, 25, 16, 58, 60, 20, 31, 53, 36, 11, 39, 2, 13, 7, 4, 14, 44, 43, 52, 24, 8, 37, 38, 40, 33, 48, 34, 55, 30, 49, 50, 51, 45, 42, 59, 5, 49, 61, 35, 26, 47, 57, 63, 65, 66, 67,

if __name__ == "__main__":
    assert sat(sol())
